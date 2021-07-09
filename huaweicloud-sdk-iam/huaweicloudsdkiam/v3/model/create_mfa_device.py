# coding: utf-8

import re
import six





class CreateMfaDevice:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'user_id': 'user_id'
    }

    def __init__(self, name=None, user_id=None):
        """CreateMfaDevice - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._user_id = None
        self.discriminator = None

        self.name = name
        self.user_id = user_id

    @property
    def name(self):
        """Gets the name of this CreateMfaDevice.

        设备名称。

        :return: The name of this CreateMfaDevice.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMfaDevice.

        设备名称。

        :param name: The name of this CreateMfaDevice.
        :type: str
        """
        self._name = name

    @property
    def user_id(self):
        """Gets the user_id of this CreateMfaDevice.

        创建MFA设备的IAM用户ID。

        :return: The user_id of this CreateMfaDevice.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateMfaDevice.

        创建MFA设备的IAM用户ID。

        :param user_id: The user_id of this CreateMfaDevice.
        :type: str
        """
        self._user_id = user_id

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
        if not isinstance(other, CreateMfaDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
