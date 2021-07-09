# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateIpGroupResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ipgroup': 'IpGroup',
        'request_id': 'str'
    }

    attribute_map = {
        'ipgroup': 'ipgroup',
        'request_id': 'request_id'
    }

    def __init__(self, ipgroup=None, request_id=None):
        """CreateIpGroupResponse - a model defined in huaweicloud sdk"""
        
        super(CreateIpGroupResponse, self).__init__()

        self._ipgroup = None
        self._request_id = None
        self.discriminator = None

        if ipgroup is not None:
            self.ipgroup = ipgroup
        if request_id is not None:
            self.request_id = request_id

    @property
    def ipgroup(self):
        """Gets the ipgroup of this CreateIpGroupResponse.


        :return: The ipgroup of this CreateIpGroupResponse.
        :rtype: IpGroup
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this CreateIpGroupResponse.


        :param ipgroup: The ipgroup of this CreateIpGroupResponse.
        :type: IpGroup
        """
        self._ipgroup = ipgroup

    @property
    def request_id(self):
        """Gets the request_id of this CreateIpGroupResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this CreateIpGroupResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateIpGroupResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this CreateIpGroupResponse.
        :type: str
        """
        self._request_id = request_id

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateIpGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
