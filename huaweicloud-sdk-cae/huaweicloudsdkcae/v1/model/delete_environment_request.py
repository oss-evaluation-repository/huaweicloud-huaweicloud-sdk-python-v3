# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEnvironmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'environment_id': 'str',
        'x_enterprise_project_id': 'str'
    }

    attribute_map = {
        'environment_id': 'environment_id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID'
    }

    def __init__(self, environment_id=None, x_enterprise_project_id=None):
        """DeleteEnvironmentRequest

        The model defined in huaweicloud sdk

        :param environment_id: 环境id。
        :type environment_id: str
        :param x_enterprise_project_id: 租户的企业项目id。
        :type x_enterprise_project_id: str
        """
        
        

        self._environment_id = None
        self._x_enterprise_project_id = None
        self.discriminator = None

        self.environment_id = environment_id
        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id

    @property
    def environment_id(self):
        """Gets the environment_id of this DeleteEnvironmentRequest.

        环境id。

        :return: The environment_id of this DeleteEnvironmentRequest.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this DeleteEnvironmentRequest.

        环境id。

        :param environment_id: The environment_id of this DeleteEnvironmentRequest.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this DeleteEnvironmentRequest.

        租户的企业项目id。

        :return: The x_enterprise_project_id of this DeleteEnvironmentRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this DeleteEnvironmentRequest.

        租户的企业项目id。

        :param x_enterprise_project_id: The x_enterprise_project_id of this DeleteEnvironmentRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

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
        if not isinstance(other, DeleteEnvironmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
