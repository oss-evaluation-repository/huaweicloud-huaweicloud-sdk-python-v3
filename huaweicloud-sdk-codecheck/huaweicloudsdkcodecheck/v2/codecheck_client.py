# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CodeCheckClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(CodeCheckClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodecheck.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CodeCheckClient":
            raise TypeError("client type error, support client type is CodeCheckClient")

        return ClientBuilder(clazz)

    def check_parameters(self, request):
        """查询任务规则集的检查参数

        查询任务规则集的检查参数

        :param CheckParametersRequest request
        :return: CheckParametersResponse
        """
        return self.check_parameters_with_http_info(request)

    def check_parameters_with_http_info(self, request):
        """查询任务规则集的检查参数

        查询任务规则集的检查参数

        :param CheckParametersRequest request
        :return: CheckParametersResponse
        """

        all_params = ['project_id', 'task_id', 'ruleset_id', 'language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']

        query_params = []
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/ruleset/{ruleset_id}/check-parameters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckParametersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_ruleset(self, request):
        """创建自定义规则集

        可根据需求灵活的组合规则。

        :param CreateRulesetRequest request
        :return: CreateRulesetResponse
        """
        return self.create_ruleset_with_http_info(request)

    def create_ruleset_with_http_info(self, request):
        """创建自定义规则集

        可根据需求灵活的组合规则。

        :param CreateRulesetRequest request
        :return: CreateRulesetResponse
        """

        all_params = ['create_ruleset_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/ruleset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRulesetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_task(self, request):
        """新建检查任务

        新建检查任务但是不执行。

        :param CreateTaskRequest request
        :return: CreateTaskResponse
        """
        return self.create_task_with_http_info(request)

    def create_task_with_http_info(self, request):
        """新建检查任务

        新建检查任务但是不执行。

        :param CreateTaskRequest request
        :return: CreateTaskResponse
        """

        all_params = ['project_id', 'create_task_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_ruleset(self, request):
        """删除自定义规则集

        删除自定义规则集，正在使用中的或默认规则集不能删除

        :param DeleteRulesetRequest request
        :return: DeleteRulesetResponse
        """
        return self.delete_ruleset_with_http_info(request)

    def delete_ruleset_with_http_info(self, request):
        """删除自定义规则集

        删除自定义规则集，正在使用中的或默认规则集不能删除

        :param DeleteRulesetRequest request
        :return: DeleteRulesetResponse
        """

        all_params = ['project_id', 'ruleset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/ruleset/{ruleset_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRulesetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_task(self, request):
        """删除检查任务

        删除检查任务，执行中的任务删除无法再查看

        :param DeleteTaskRequest request
        :return: DeleteTaskResponse
        """
        return self.delete_task_with_http_info(request)

    def delete_task_with_http_info(self, request):
        """删除检查任务

        删除检查任务，执行中的任务删除无法再查看

        :param DeleteTaskRequest request
        :return: DeleteTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_rules(self, request):
        """获取规则列表接口

        根据语言、问题级别等条件查询规则列表。

        :param ListRulesRequest request
        :return: ListRulesResponse
        """
        return self.list_rules_with_http_info(request)

    def list_rules_with_http_info(self, request):
        """获取规则列表接口

        根据语言、问题级别等条件查询规则列表。

        :param ListRulesRequest request
        :return: ListRulesResponse
        """

        all_params = ['rule_languages', 'rule_severity', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rule_languages' in local_var_params:
            query_params.append(('rule_languages', local_var_params['rule_languages']))
        if 'rule_severity' in local_var_params:
            query_params.append(('rule_severity', local_var_params['rule_severity']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_rulesets(self, request):
        """查询规则集列表

        根据项目ID、语言等条件查询规则集列表。

        :param ListRulesetsRequest request
        :return: ListRulesetsResponse
        """
        return self.list_rulesets_with_http_info(request)

    def list_rulesets_with_http_info(self, request):
        """查询规则集列表

        根据项目ID、语言等条件查询规则集列表。

        :param ListRulesetsRequest request
        :return: ListRulesetsResponse
        """

        all_params = ['project_id', 'category', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/rulesets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRulesetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_task_parameter(self, request):
        """任务配置检查参数

        任务配置检查参数

        :param ListTaskParameterRequest request
        :return: ListTaskParameterResponse
        """
        return self.list_task_parameter_with_http_info(request)

    def list_task_parameter_with_http_info(self, request):
        """任务配置检查参数

        任务配置检查参数

        :param ListTaskParameterRequest request
        :return: ListTaskParameterResponse
        """

        all_params = ['project_id', 'task_id', 'list_task_parameter_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/config-parameters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTaskParameterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_task_ruleset(self, request):
        """查询任务的已选规则集列表

        查询任务的已选规则集列表。

        :param ListTaskRulesetRequest request
        :return: ListTaskRulesetResponse
        """
        return self.list_task_ruleset_with_http_info(request)

    def list_task_ruleset_with_http_info(self, request):
        """查询任务的已选规则集列表

        查询任务的已选规则集列表。

        :param ListTaskRulesetRequest request
        :return: ListTaskRulesetResponse
        """

        all_params = ['project_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/rulesets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTaskRulesetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_template_rules(self, request):
        """查看规则集的规则列表

        根据项目ID、规则集ID等条件查询规则列表。

        :param ListTemplateRulesRequest request
        :return: ListTemplateRulesResponse
        """
        return self.list_template_rules_with_http_info(request)

    def list_template_rules_with_http_info(self, request):
        """查看规则集的规则列表

        根据项目ID、规则集ID等条件查询规则列表。

        :param ListTemplateRulesRequest request
        :return: ListTemplateRulesResponse
        """

        all_params = ['project_id', 'ruleset_id', 'types', 'languages', 'tags', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']

        query_params = []
        if 'types' in local_var_params:
            query_params.append(('types', local_var_params['types']))
        if 'languages' in local_var_params:
            query_params.append(('languages', local_var_params['languages']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/ruleset/{ruleset_id}/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplateRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def run_task(self, request):
        """执行检查任务

        执行检查任务。

        :param RunTaskRequest request
        :return: RunTaskResponse
        """
        return self.run_task_with_http_info(request)

    def run_task_with_http_info(self, request):
        """执行检查任务

        执行检查任务。

        :param RunTaskRequest request
        :return: RunTaskResponse
        """

        all_params = ['task_id', 'run_task_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/run',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_defaul_template(self, request):
        """设置每个项目对应语言的默认规则集配置

        设置每个项目对应语言的默认规则集配置。

        :param SetDefaulTemplateRequest request
        :return: SetDefaulTemplateResponse
        """
        return self.set_defaul_template_with_http_info(request)

    def set_defaul_template_with_http_info(self, request):
        """设置每个项目对应语言的默认规则集配置

        设置每个项目对应语言的默认规则集配置。

        :param SetDefaulTemplateRequest request
        :return: SetDefaulTemplateResponse
        """

        all_params = ['project_id', 'ruleset_id', 'language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'ruleset_id' in local_var_params:
            path_params['ruleset_id'] = local_var_params['ruleset_id']
        if 'language' in local_var_params:
            path_params['language'] = local_var_params['language']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/ruleset/{ruleset_id}/{language}/default',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetDefaulTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_progress_detail(self, request):
        """查询任务执行状态

        根据任务ID查询任务执行状态。任务状态：0表示检查中，1表示检查失败，2表示检查成功，3表示任务中止。只有正在检查中才有进度的详细信息。

        :param ShowProgressDetailRequest request
        :return: ShowProgressDetailResponse
        """
        return self.show_progress_detail_with_http_info(request)

    def show_progress_detail_with_http_info(self, request):
        """查询任务执行状态

        根据任务ID查询任务执行状态。任务状态：0表示检查中，1表示检查失败，2表示检查成功，3表示任务中止。只有正在检查中才有进度的详细信息。

        :param ShowProgressDetailRequest request
        :return: ShowProgressDetailResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProgressDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_task_cmetrics(self, request):
        """查询cmertrics缺陷概要

        根据检查任务ID查询cmertrics缺陷概要。

        :param ShowTaskCmetricsRequest request
        :return: ShowTaskCmetricsResponse
        """
        return self.show_task_cmetrics_with_http_info(request)

    def show_task_cmetrics_with_http_info(self, request):
        """查询cmertrics缺陷概要

        根据检查任务ID查询cmertrics缺陷概要。

        :param ShowTaskCmetricsRequest request
        :return: ShowTaskCmetricsResponse
        """

        all_params = ['project_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/metrics-summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskCmetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_task_defects(self, request):
        """查询缺陷详情

        根据检查任务ID分页查询缺陷结果详情。

        :param ShowTaskDefectsRequest request
        :return: ShowTaskDefectsResponse
        """
        return self.show_task_defects_with_http_info(request)

    def show_task_defects_with_http_info(self, request):
        """查询缺陷详情

        根据检查任务ID分页查询缺陷结果详情。

        :param ShowTaskDefectsRequest request
        :return: ShowTaskDefectsResponse
        """

        all_params = ['task_id', 'offset', 'limit', 'status_ids', 'severity']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status_ids' in local_var_params:
            query_params.append(('status_ids', local_var_params['status_ids']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/defects-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskDefectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_task_defects_statistic(self, request):
        """查询缺陷详情的统计

        根据检查任务ID查询缺陷详情的统计

        :param ShowTaskDefectsStatisticRequest request
        :return: ShowTaskDefectsStatisticResponse
        """
        return self.show_task_defects_statistic_with_http_info(request)

    def show_task_defects_statistic_with_http_info(self, request):
        """查询缺陷详情的统计

        根据检查任务ID查询缺陷详情的统计

        :param ShowTaskDefectsStatisticRequest request
        :return: ShowTaskDefectsStatisticResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/defects-statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskDefectsStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_task_detail(self, request):
        """查询缺陷概要

        根据检查任务ID查询缺陷结果的概要。包括问题概述、问题状态、圈复杂度、代码重复率等。

        :param ShowTaskDetailRequest request
        :return: ShowTaskDetailResponse
        """
        return self.show_task_detail_with_http_info(request)

    def show_task_detail_with_http_info(self, request):
        """查询缺陷概要

        根据检查任务ID查询缺陷结果的概要。包括问题概述、问题状态、圈复杂度、代码重复率等。

        :param ShowTaskDetailRequest request
        :return: ShowTaskDetailResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/defects-summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_task_list_by_project_id(self, request):
        """查询任务列表

        根据DEVCLOUD_PROJECT_UUID查询该项目下的任务列表。

        :param ShowTaskListByProjectIdRequest request
        :return: ShowTaskListByProjectIdResponse
        """
        return self.show_task_list_by_project_id_with_http_info(request)

    def show_task_list_by_project_id_with_http_info(self, request):
        """查询任务列表

        根据DEVCLOUD_PROJECT_UUID查询该项目下的任务列表。

        :param ShowTaskListByProjectIdRequest request
        :return: ShowTaskListByProjectIdResponse
        """

        all_params = ['project_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskListByProjectIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_tasklog(self, request):
        """查询任务检查失败日志

        查询任务检查失败日志，不传execute_id则查询最近一次的检查日志

        :param ShowTasklogRequest request
        :return: ShowTasklogResponse
        """
        return self.show_tasklog_with_http_info(request)

    def show_tasklog_with_http_info(self, request):
        """查询任务检查失败日志

        查询任务检查失败日志，不传execute_id则查询最近一次的检查日志

        :param ShowTasklogRequest request
        :return: ShowTasklogResponse
        """

        all_params = ['project_id', 'task_id', 'execute_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'execute_id' in local_var_params:
            query_params.append(('execute_id', local_var_params['execute_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/log-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTasklogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_task_by_id(self, request):
        """终止检查任务

        根据任务ID终止检查任务。

        :param StopTaskByIdRequest request
        :return: StopTaskByIdResponse
        """
        return self.stop_task_by_id_with_http_info(request)

    def stop_task_by_id_with_http_info(self, request):
        """终止检查任务

        根据任务ID终止检查任务。

        :param StopTaskByIdRequest request
        :return: StopTaskByIdResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopTaskByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_defect_status(self, request):
        """修改缺陷状态

        修改检查出的缺陷的状态为已解决、已忽略

        :param UpdateDefectStatusRequest request
        :return: UpdateDefectStatusResponse
        """
        return self.update_defect_status_with_http_info(request)

    def update_defect_status_with_http_info(self, request):
        """修改缺陷状态

        修改检查出的缺陷的状态为已解决、已忽略

        :param UpdateDefectStatusRequest request
        :return: UpdateDefectStatusResponse
        """

        all_params = ['task_id', 'update_defect_status_v2_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/defect-status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDefectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_task_ruleset(self, request):
        """修改任务规则集

        修改任务规则集。

        :param UpdateTaskRulesetRequest request
        :return: UpdateTaskRulesetResponse
        """
        return self.update_task_ruleset_with_http_info(request)

    def update_task_ruleset_with_http_info(self, request):
        """修改任务规则集

        修改任务规则集。

        :param UpdateTaskRulesetRequest request
        :return: UpdateTaskRulesetResponse
        """

        all_params = ['task_id', 'update_task_ruleset_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/tasks/{task_id}/ruleset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTaskRulesetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)