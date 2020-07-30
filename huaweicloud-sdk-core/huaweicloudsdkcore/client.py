# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import datetime
import importlib
import json
import logging
import os
import re
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from logging.handlers import RotatingFileHandler
from typing import Mapping

import six
from six.moves.urllib.parse import quote, urlparse

from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.http_handler import HttpHandler
from huaweicloudsdkcore.http.primitive_types import native_types_mapping
from huaweicloudsdkcore.http.primitive_types import primitive_types
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.sdk_response import FutureSdkResponse
from huaweicloudsdkcore.sdk_stream_response import SdkStreamResponse
from huaweicloudsdkcore.utils import http_utils, core_utils


class ClientBuilder:
    def __init__(self, client_type, credential_type=BasicCredentials.__name__):
        self._client_class = client_type
        self._credential_type = credential_type
        self._config = None
        self._credentials = None
        self._endpoint = None

        self._http_handler = None
        self._file_logger_handler = None
        self._stream_logger_handler = None

    def with_http_config(self, config: HttpConfig):
        self._config = config
        return self

    def with_credentials(self, credentials):
        self._credentials = credentials
        return self

    def with_endpoint(self, endpoint):
        self._endpoint = endpoint
        return self

    def with_http_handler(self, http_handler):
        self._http_handler = http_handler
        return self

    def with_file_log(self, path, log_level=logging.INFO, max_bytes=10485760, backup_count=5, format_string=None):
        self._file_logger_handler = {
            "path": path,
            "log_level": log_level,
            "max_bytes": max_bytes,
            "backup_count": backup_count,
            "format_string": format_string
        }
        return self

    def with_stream_log(self, stream=sys.stdout, log_level=logging.INFO, format_string=None):
        self._stream_logger_handler = {
            "stream": stream,
            "log_level": log_level,
            "format_string": format_string
        }
        return self

    def build(self):
        if self._credentials is None:
            self._credentials = self.get_credential_from_environment_variables()

        if self._credentials.__class__.__name__ != self._credential_type:
            raise TypeError("Need credential type is %s, actually is %s" % (
                self._credential_type, self._credentials.__class__.__name__))

        client = self._client_class() \
            .with_endpoint(self._endpoint) \
            .with_credentials(self._credentials) \
            .with_config(self._config) \
            .with_http_handler(self._http_handler)

        if self._file_logger_handler is not None:
            client.add_file_logger(**self._file_logger_handler)
        if self._stream_logger_handler is not None:
            client.add_stream_logger(**self._stream_logger_handler)

        client.init_http_client()
        return client

    def get_credential_from_environment_variables(self):
        ak = os.environ.get("HUAWEICLOUD_SDK_AK")
        sk = os.environ.get("HUAWEICLOUD_SDK_SK")
        project_id = os.environ.get("HUAWEICLOUD_SDK_PROJECT_ID")
        domain_id = os.environ.get("HUAWEICLOUD_SDK_DOMAIN_ID")

        if self._credential_type == BasicCredentials.__name__:
            return BasicCredentials(ak, sk, project_id)
        elif self._credential_type == GlobalCredentials.__name__:
            return GlobalCredentials(ak, sk, domain_id)
        else:
            return None


class Client:
    def __init__(self):
        self.preset_headers = {}

        self._agent = {"User-Agent": "huaweicloud-sdk-pythons/3.0"}
        self._logger = self._init_logger()

        self._credentials = None
        self._config = None
        self._endpoint = None

        self._http_client = None
        self._http_handler = None

        self.model_package = None
        try:
            exception_handler_model_name = "%s.exception_handler" % self.__module__[:self.__module__.rindex('.')]
            self.exception_handler_model = importlib.import_module(exception_handler_model_name)
        except ImportError:
            self.exception_handler_model = None

    @classmethod
    def _init_logger(cls):
        logger_name = 'HuaweiCloud-SDK-%s' % cls.__name__
        logger = logging.getLogger(logger_name)
        logger.propagate = False
        return logger

    def with_config(self, config):
        self._config = config
        return self

    def with_credentials(self, credentials):
        self._credentials = credentials
        return self

    def with_endpoint(self, endpoint):
        self._endpoint = endpoint
        return self

    def with_http_handler(self, http_handler):
        self._http_handler = http_handler if http_handler is not None else HttpHandler()
        return self

    def init_http_client(self):
        exception_handler = None \
            if self.exception_handler_model is None else getattr(self.exception_handler_model, "handle_exception")
        self._http_client = HttpClient(self._config, self._http_handler, exception_handler, self._logger)

    def add_stream_logger(self, stream, log_level, format_string):
        self._logger.setLevel(log_level)
        stream_handler = logging.StreamHandler(stream)
        stream_handler.setLevel(log_level)
        formatter = logging.Formatter(format_string if format_string is not None else core_utils.LOG_FORMAT)
        stream_handler.setFormatter(formatter)

        if stream_handler not in self._logger.handlers:
            self._logger.addHandler(stream_handler)

    def add_file_logger(self, path, log_level, max_bytes, backup_count, format_string):
        self._logger.setLevel(log_level)
        file_handler = RotatingFileHandler(path, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setLevel(log_level)
        formatter = logging.Formatter(format_string if format_string is not None else core_utils.LOG_FORMAT)
        file_handler.setFormatter(formatter)

        if file_handler not in self._logger.handlers:
            self._logger.addHandler(file_handler)

    def get_agent(self):
        return self._agent

    def get_credentials(self):
        return self._credentials

    def get_http_client(self):
        return self._http_client

    def _parse_header_params(self, collection_formats, header_params):
        header_params = self.post_process_params(header_params) or {}
        header_params.update(self.preset_headers)
        if header_params:
            header_params = http_utils.sanitize_for_serialization(header_params)
            header_params = dict(http_utils.parameters_to_tuples(header_params, collection_formats))
        header_params.update(self._agent)
        return header_params

    def _parse_path_params(self, collection_formats, path_params, resource_path, update_path_params):
        path_params = self.post_process_params(path_params) or {}
        if update_path_params is not None:
            path_params.update(update_path_params)
        if path_params:
            path_params = http_utils.sanitize_for_serialization(path_params)
            path_params = http_utils.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe=''))
        return resource_path

    def _parse_query_params(self, collection_formats, query_params):
        query_params = self.post_process_params(query_params) or []
        if query_params:
            query_params = http_utils.sanitize_for_serialization(query_params)
            query_params = http_utils.parameters_to_tuples(query_params, collection_formats)
        return query_params

    def _parse_post_params(self, collection_formats, post_params):
        post_params = self.post_process_params(post_params) if post_params else {}
        if post_params:
            post_params = http_utils.sanitize_for_serialization(post_params)
            post_params = http_utils.parameters_to_tuples(post_params, collection_formats)
        return post_params

    @classmethod
    def _parse_body(cls, body, post_params):
        if body:
            if all([hasattr(body, '__iter__'), not isinstance(body, (str, bytes, list, tuple, Mapping))]):
                return body
            body = http_utils.sanitize_for_serialization(body)
            body = json.dumps(body)
        elif len(post_params) != 0:
            body = post_params
        else:
            body = ""
        return body

    def _is_stream(self, response_type):
        if type(response_type) == str and hasattr(self.model_package, response_type):
            klass = getattr(self.model_package, response_type)
            if issubclass(klass, SdkStreamResponse):
                return True
        return False

    @classmethod
    def post_process_params(cls, params):
        if type(params) == dict:
            for key in list(params.keys()):
                if params[key] is None:
                    del [params[key]]
            return params
        elif type(params) == list:
            list_filter = filter(lambda x: type(x) == tuple and len(x) == 2 and x[1] is not None, params)
            return [i for i in list_filter]

    def do_http_request(self, method, resource_path, path_params=None, query_params=None, header_params=None, body=None,
                        post_params=None, response_type=None, collection_formats=None, request_type=None,
                        async_request=False):
        url_parse_result = urlparse(self._endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc

        header_params = self._parse_header_params(collection_formats, header_params)
        resource_path = self._parse_path_params(collection_formats, path_params, resource_path,
                                                self._credentials.get_update_path_params())
        query_params = self._parse_query_params(collection_formats, query_params)
        post_params = self._parse_post_params(collection_formats, post_params)
        body = self._parse_body(body, post_params)

        stream = self._is_stream(response_type)
        sdk_request = SdkRequest(method=method, schema=schema, host=host, resource_path=resource_path,
                                 query_params=query_params, header_params=header_params, body=body, stream=stream)
        future_request = self._credentials.process_auth_request(sdk_request, self._http_client)
        if async_request:
            executor = ThreadPoolExecutor(max_workers=8)
            future_response = executor.submit(self._do_http_request_async, future_request, response_type)
            return FutureSdkResponse(future_response, self._logger)
        else:
            request = future_request.result()
            response = self._do_http_request_sync(request)
            return self.sync_response_handler(response, response_type)

    def _do_http_request_sync(self, request):
        response = self._http_client.do_request_sync(request)
        return response

    def _do_http_request_async(self, future_request, response_type):
        request = future_request.result()
        future_response = self._http_client.do_request_async(
            request=request, hooks=[self.async_response_hook_factory(response_type)]
        )
        return future_response

    def sync_response_handler(self, response, response_type):
        return_data = self.deserialize(response, response_type)
        return_data.status_code = response.status_code
        return_data.header_params = response.headers
        return return_data

    def async_response_hook_factory(self, response_type):
        def response_hook(resp, *args, **kwargs):
            resp.data = self.sync_response_handler(resp, response_type)

        return response_hook

    def deserialize(self, response, response_type):
        if type(response_type) == str and hasattr(self.model_package, response_type):
            klass = getattr(self.model_package, response_type)
            if issubclass(klass, SdkStreamResponse):
                return klass(response)

        try:
            data = json.loads(response.text)
        except ValueError:
            data = response.text
        return self._deserialize(data, response_type)

    def _deserialize(self, data, klass):
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self._deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self._deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            if klass in native_types_mapping:
                klass = native_types_mapping[klass]
            else:
                klass = getattr(self.model_package, klass)

        if klass in primitive_types:
            return self._deserialize_primitive(data, klass)
        elif klass == object:
            return self._deserialize_object(data)
        elif klass == datetime.date:
            return self._deserialize_date(data)
        elif klass == datetime.datetime:
            return self._deserialize_data_time(data)
        else:
            return self._deserialize_model(data, klass)

    @classmethod
    def _deserialize_primitive(cls, data, klass):
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    @classmethod
    def _deserialize_object(cls, value):
        return value

    @classmethod
    def _deserialize_date(cls, string):
        try:
            from dateutil.parser import parse
            return parse(string if string.endswith("Z") else string + "Z").date()
        except ImportError:
            return string
        except ValueError:
            return string

    @classmethod
    def _deserialize_data_time(cls, string):
        try:
            from dateutil.parser import parse
            return parse(string if string.endswith("Z") else string + "Z")
        except ImportError:
            return string
        except ValueError:
            return string

    def _deserialize_model(self, data, klass):
        if not klass.openapi_types and not hasattr(klass, 'get_real_child_model'):
            return klass()

        kwargs = {}
        if klass.openapi_types is not None:
            for attr, attr_type in six.iteritems(klass.openapi_types):
                if data is not None and isinstance(data, (list, dict)):
                    if klass.attribute_map[attr] in data:
                        value = data[klass.attribute_map[attr]]
                        kwargs[attr] = self._deserialize(value, attr_type)
                    if klass.attribute_map[attr] == "body":
                        kwargs[attr] = self._deserialize(data, attr_type)

        instance = klass(**kwargs)

        if hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self._deserialize(data, klass_name)
        return instance
