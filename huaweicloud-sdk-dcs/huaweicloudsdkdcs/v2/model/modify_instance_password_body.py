# coding: utf-8

import pprint
import re

import six





class ModifyInstancePasswordBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'old_password': 'str',
        'new_password': 'str'
    }

    attribute_map = {
        'old_password': 'old_password',
        'new_password': 'new_password'
    }

    def __init__(self, old_password=None, new_password=None):
        """ModifyInstancePasswordBody - a model defined in huaweicloud sdk"""
        
        

        self._old_password = None
        self._new_password = None
        self.discriminator = None

        if old_password is not None:
            self.old_password = old_password
        if new_password is not None:
            self.new_password = new_password

    @property
    def old_password(self):
        """Gets the old_password of this ModifyInstancePasswordBody.

        旧密码

        :return: The old_password of this ModifyInstancePasswordBody.
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this ModifyInstancePasswordBody.

        旧密码

        :param old_password: The old_password of this ModifyInstancePasswordBody.
        :type: str
        """
        self._old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this ModifyInstancePasswordBody.

        新密码

        :return: The new_password of this ModifyInstancePasswordBody.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ModifyInstancePasswordBody.

        新密码

        :param new_password: The new_password of this ModifyInstancePasswordBody.
        :type: str
        """
        self._new_password = new_password

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifyInstancePasswordBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
