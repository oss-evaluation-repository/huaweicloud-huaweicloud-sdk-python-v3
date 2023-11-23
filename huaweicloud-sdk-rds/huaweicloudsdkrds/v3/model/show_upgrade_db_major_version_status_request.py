# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUpgradeDbMajorVersionStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'action': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'action': 'action',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, action=None, x_language=None):
        """ShowUpgradeDbMajorVersionStatusRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param action: 要查询的状态 check：查询升级预检查的状态。 upgrade：查询大板本升级的状态。
        :type action: str
        :param x_language: 语言。默认en-us。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._action = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.action = action
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowUpgradeDbMajorVersionStatusRequest.

        实例ID

        :return: The instance_id of this ShowUpgradeDbMajorVersionStatusRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowUpgradeDbMajorVersionStatusRequest.

        实例ID

        :param instance_id: The instance_id of this ShowUpgradeDbMajorVersionStatusRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def action(self):
        """Gets the action of this ShowUpgradeDbMajorVersionStatusRequest.

        要查询的状态 check：查询升级预检查的状态。 upgrade：查询大板本升级的状态。

        :return: The action of this ShowUpgradeDbMajorVersionStatusRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowUpgradeDbMajorVersionStatusRequest.

        要查询的状态 check：查询升级预检查的状态。 upgrade：查询大板本升级的状态。

        :param action: The action of this ShowUpgradeDbMajorVersionStatusRequest.
        :type action: str
        """
        self._action = action

    @property
    def x_language(self):
        """Gets the x_language of this ShowUpgradeDbMajorVersionStatusRequest.

        语言。默认en-us。

        :return: The x_language of this ShowUpgradeDbMajorVersionStatusRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowUpgradeDbMajorVersionStatusRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ShowUpgradeDbMajorVersionStatusRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowUpgradeDbMajorVersionStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other