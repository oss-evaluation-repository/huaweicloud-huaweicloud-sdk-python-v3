# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Configs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'origin_request_header': 'list[OriginRequestHeader]',
        'http_response_header': 'list[HttpResponseHeader]',
        'url_auth': 'UrlAuth',
        'https': 'HttpPutBody',
        'sources': 'list[SourcesConfig]',
        'origin_protocol': 'str',
        'force_redirect': 'ForceRedirectConfig',
        'compress': 'Compress',
        'cache_url_parameter_filter': 'CacheUrlParameterFilter',
        'ipv6_accelerate': 'int'
    }

    attribute_map = {
        'origin_request_header': 'origin_request_header',
        'http_response_header': 'http_response_header',
        'url_auth': 'url_auth',
        'https': 'https',
        'sources': 'sources',
        'origin_protocol': 'origin_protocol',
        'force_redirect': 'force_redirect',
        'compress': 'compress',
        'cache_url_parameter_filter': 'cache_url_parameter_filter',
        'ipv6_accelerate': 'ipv6_accelerate'
    }

    def __init__(self, origin_request_header=None, http_response_header=None, url_auth=None, https=None, sources=None, origin_protocol=None, force_redirect=None, compress=None, cache_url_parameter_filter=None, ipv6_accelerate=None):
        """Configs

        The model defined in huaweicloud sdk

        :param origin_request_header: 回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。
        :type origin_request_header: list[:class:`huaweicloudsdkcdn.v1.OriginRequestHeader`]
        :param http_response_header: http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v1.HttpResponseHeader`]
        :param url_auth: 
        :type url_auth: :class:`huaweicloudsdkcdn.v1.UrlAuth`
        :param https: 
        :type https: :class:`huaweicloudsdkcdn.v1.HttpPutBody`
        :param sources: 源站配置。
        :type sources: list[:class:`huaweicloudsdkcdn.v1.SourcesConfig`]
        :param origin_protocol: 回源协议（follow：协议跟随回源，http：HTTP回源(默认)，https：https回源）。
        :type origin_protocol: str
        :param force_redirect: 
        :type force_redirect: :class:`huaweicloudsdkcdn.v1.ForceRedirectConfig`
        :param compress: 
        :type compress: :class:`huaweicloudsdkcdn.v1.Compress`
        :param cache_url_parameter_filter: 
        :type cache_url_parameter_filter: :class:`huaweicloudsdkcdn.v1.CacheUrlParameterFilter`
        :param ipv6_accelerate: ipv6设置（1：打开；0：关闭）
        :type ipv6_accelerate: int
        """
        
        

        self._origin_request_header = None
        self._http_response_header = None
        self._url_auth = None
        self._https = None
        self._sources = None
        self._origin_protocol = None
        self._force_redirect = None
        self._compress = None
        self._cache_url_parameter_filter = None
        self._ipv6_accelerate = None
        self.discriminator = None

        if origin_request_header is not None:
            self.origin_request_header = origin_request_header
        if http_response_header is not None:
            self.http_response_header = http_response_header
        if url_auth is not None:
            self.url_auth = url_auth
        if https is not None:
            self.https = https
        if sources is not None:
            self.sources = sources
        if origin_protocol is not None:
            self.origin_protocol = origin_protocol
        if force_redirect is not None:
            self.force_redirect = force_redirect
        if compress is not None:
            self.compress = compress
        if cache_url_parameter_filter is not None:
            self.cache_url_parameter_filter = cache_url_parameter_filter
        if ipv6_accelerate is not None:
            self.ipv6_accelerate = ipv6_accelerate

    @property
    def origin_request_header(self):
        """Gets the origin_request_header of this Configs.

        回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :return: The origin_request_header of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.OriginRequestHeader`]
        """
        return self._origin_request_header

    @origin_request_header.setter
    def origin_request_header(self, origin_request_header):
        """Sets the origin_request_header of this Configs.

        回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :param origin_request_header: The origin_request_header of this Configs.
        :type origin_request_header: list[:class:`huaweicloudsdkcdn.v1.OriginRequestHeader`]
        """
        self._origin_request_header = origin_request_header

    @property
    def http_response_header(self):
        """Gets the http_response_header of this Configs.

        http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :return: The http_response_header of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.HttpResponseHeader`]
        """
        return self._http_response_header

    @http_response_header.setter
    def http_response_header(self, http_response_header):
        """Sets the http_response_header of this Configs.

        http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :param http_response_header: The http_response_header of this Configs.
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v1.HttpResponseHeader`]
        """
        self._http_response_header = http_response_header

    @property
    def url_auth(self):
        """Gets the url_auth of this Configs.


        :return: The url_auth of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.UrlAuth`
        """
        return self._url_auth

    @url_auth.setter
    def url_auth(self, url_auth):
        """Sets the url_auth of this Configs.


        :param url_auth: The url_auth of this Configs.
        :type url_auth: :class:`huaweicloudsdkcdn.v1.UrlAuth`
        """
        self._url_auth = url_auth

    @property
    def https(self):
        """Gets the https of this Configs.


        :return: The https of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.HttpPutBody`
        """
        return self._https

    @https.setter
    def https(self, https):
        """Sets the https of this Configs.


        :param https: The https of this Configs.
        :type https: :class:`huaweicloudsdkcdn.v1.HttpPutBody`
        """
        self._https = https

    @property
    def sources(self):
        """Gets the sources of this Configs.

        源站配置。

        :return: The sources of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.SourcesConfig`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Configs.

        源站配置。

        :param sources: The sources of this Configs.
        :type sources: list[:class:`huaweicloudsdkcdn.v1.SourcesConfig`]
        """
        self._sources = sources

    @property
    def origin_protocol(self):
        """Gets the origin_protocol of this Configs.

        回源协议（follow：协议跟随回源，http：HTTP回源(默认)，https：https回源）。

        :return: The origin_protocol of this Configs.
        :rtype: str
        """
        return self._origin_protocol

    @origin_protocol.setter
    def origin_protocol(self, origin_protocol):
        """Sets the origin_protocol of this Configs.

        回源协议（follow：协议跟随回源，http：HTTP回源(默认)，https：https回源）。

        :param origin_protocol: The origin_protocol of this Configs.
        :type origin_protocol: str
        """
        self._origin_protocol = origin_protocol

    @property
    def force_redirect(self):
        """Gets the force_redirect of this Configs.


        :return: The force_redirect of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.ForceRedirectConfig`
        """
        return self._force_redirect

    @force_redirect.setter
    def force_redirect(self, force_redirect):
        """Sets the force_redirect of this Configs.


        :param force_redirect: The force_redirect of this Configs.
        :type force_redirect: :class:`huaweicloudsdkcdn.v1.ForceRedirectConfig`
        """
        self._force_redirect = force_redirect

    @property
    def compress(self):
        """Gets the compress of this Configs.


        :return: The compress of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.Compress`
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        """Sets the compress of this Configs.


        :param compress: The compress of this Configs.
        :type compress: :class:`huaweicloudsdkcdn.v1.Compress`
        """
        self._compress = compress

    @property
    def cache_url_parameter_filter(self):
        """Gets the cache_url_parameter_filter of this Configs.


        :return: The cache_url_parameter_filter of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.CacheUrlParameterFilter`
        """
        return self._cache_url_parameter_filter

    @cache_url_parameter_filter.setter
    def cache_url_parameter_filter(self, cache_url_parameter_filter):
        """Sets the cache_url_parameter_filter of this Configs.


        :param cache_url_parameter_filter: The cache_url_parameter_filter of this Configs.
        :type cache_url_parameter_filter: :class:`huaweicloudsdkcdn.v1.CacheUrlParameterFilter`
        """
        self._cache_url_parameter_filter = cache_url_parameter_filter

    @property
    def ipv6_accelerate(self):
        """Gets the ipv6_accelerate of this Configs.

        ipv6设置（1：打开；0：关闭）

        :return: The ipv6_accelerate of this Configs.
        :rtype: int
        """
        return self._ipv6_accelerate

    @ipv6_accelerate.setter
    def ipv6_accelerate(self, ipv6_accelerate):
        """Sets the ipv6_accelerate of this Configs.

        ipv6设置（1：打开；0：关闭）

        :param ipv6_accelerate: The ipv6_accelerate of this Configs.
        :type ipv6_accelerate: int
        """
        self._ipv6_accelerate = ipv6_accelerate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Configs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
