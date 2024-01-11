# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteJobAuthInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_info_name': 'str'
    }

    attribute_map = {
        'auth_info_name': 'auth_info_name'
    }

    def __init__(self, auth_info_name=None):
        """DeleteJobAuthInfoRequest

        The model defined in huaweicloud sdk

        :param auth_info_name: 即将删除的认证信息名
        :type auth_info_name: str
        """
        
        

        self._auth_info_name = None
        self.discriminator = None

        self.auth_info_name = auth_info_name

    @property
    def auth_info_name(self):
        """Gets the auth_info_name of this DeleteJobAuthInfoRequest.

        即将删除的认证信息名

        :return: The auth_info_name of this DeleteJobAuthInfoRequest.
        :rtype: str
        """
        return self._auth_info_name

    @auth_info_name.setter
    def auth_info_name(self, auth_info_name):
        """Sets the auth_info_name of this DeleteJobAuthInfoRequest.

        即将删除的认证信息名

        :param auth_info_name: The auth_info_name of this DeleteJobAuthInfoRequest.
        :type auth_info_name: str
        """
        self._auth_info_name = auth_info_name

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
        if not isinstance(other, DeleteJobAuthInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other