# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoints': 'list[EndpointResp]',
        'metadata': 'Metedata'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'metadata': 'metadata'
    }

    def __init__(self, endpoints=None, metadata=None):
        """ListEndpointsResponse

        The model defined in huaweicloud sdk

        :param endpoints: 查询公网Zone的列表响应。
        :type endpoints: list[:class:`huaweicloudsdkdns.v2.EndpointResp`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metedata`
        """
        
        super(ListEndpointsResponse, self).__init__()

        self._endpoints = None
        self._metadata = None
        self.discriminator = None

        if endpoints is not None:
            self.endpoints = endpoints
        if metadata is not None:
            self.metadata = metadata

    @property
    def endpoints(self):
        """Gets the endpoints of this ListEndpointsResponse.

        查询公网Zone的列表响应。

        :return: The endpoints of this ListEndpointsResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.EndpointResp`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this ListEndpointsResponse.

        查询公网Zone的列表响应。

        :param endpoints: The endpoints of this ListEndpointsResponse.
        :type endpoints: list[:class:`huaweicloudsdkdns.v2.EndpointResp`]
        """
        self._endpoints = endpoints

    @property
    def metadata(self):
        """Gets the metadata of this ListEndpointsResponse.

        :return: The metadata of this ListEndpointsResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metedata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ListEndpointsResponse.

        :param metadata: The metadata of this ListEndpointsResponse.
        :type metadata: :class:`huaweicloudsdkdns.v2.Metedata`
        """
        self._metadata = metadata

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
        if not isinstance(other, ListEndpointsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
