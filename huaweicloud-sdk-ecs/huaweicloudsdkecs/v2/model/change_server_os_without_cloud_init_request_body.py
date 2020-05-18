# coding: utf-8

import pprint
import re

import six


class ChangeServerOsWithoutCloudInitRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'os_change': 'ChangeServerOsWithoutCloudInitOption'
    }

    attribute_map = {
        'os_change': 'os-change'
    }

    def __init__(self, os_change=None):  # noqa: E501
        """ChangeServerOsWithoutCloudInitRequestBody - a model defined in huaweicloud sdk"""

        self._os_change = None
        self.discriminator = None

        self.os_change = os_change

    @property
    def os_change(self):
        """Gets the os_change of this ChangeServerOsWithoutCloudInitRequestBody.


        :return: The os_change of this ChangeServerOsWithoutCloudInitRequestBody.
        :rtype: ChangeServerOsWithoutCloudInitOption
        """
        return self._os_change

    @os_change.setter
    def os_change(self, os_change):
        """Sets the os_change of this ChangeServerOsWithoutCloudInitRequestBody.


        :param os_change: The os_change of this ChangeServerOsWithoutCloudInitRequestBody.
        :type: ChangeServerOsWithoutCloudInitOption
        """
        self._os_change = os_change

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
        if not isinstance(other, ChangeServerOsWithoutCloudInitRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
