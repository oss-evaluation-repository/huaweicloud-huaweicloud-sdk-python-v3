# coding: utf-8

import pprint
import re

import six


class ListInstanceTagsResult(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):  # noqa: E501
        """ListInstanceTagsResult - a model defined in huaweicloud sdk"""

        self._key = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this ListInstanceTagsResult.

        标签键。最大长度36个unicode字符，key不能为空。 字符集：0-9，A-Z，a-z，“_”，“-”，中文。

        :return: The key of this ListInstanceTagsResult.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ListInstanceTagsResult.

        标签键。最大长度36个unicode字符，key不能为空。 字符集：0-9，A-Z，a-z，“_”，“-”，中文。

        :param key: The key of this ListInstanceTagsResult.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this ListInstanceTagsResult.

        标签值。最大长度43个unicode字符，可以为空字符串。 字符集：0-9，A-Z，a-z，“_”，“.”，“-”，中文。

        :return: The value of this ListInstanceTagsResult.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListInstanceTagsResult.

        标签值。最大长度43个unicode字符，可以为空字符串。 字符集：0-9，A-Z，a-z，“_”，“.”，“-”，中文。

        :param value: The value of this ListInstanceTagsResult.
        :type: str
        """
        self._value = value

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
        if not isinstance(other, ListInstanceTagsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
