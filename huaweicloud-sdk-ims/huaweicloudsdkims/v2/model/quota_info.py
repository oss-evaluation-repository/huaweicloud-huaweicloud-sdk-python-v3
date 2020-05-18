# coding: utf-8

import pprint
import re

import six


class QuotaInfo(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'type': 'str',
        'used': 'int',
        'quota': 'int',
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'quota': 'quota',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, type=None, used=None, quota=None, min=None, max=None):  # noqa: E501
        """QuotaInfo - a model defined in huaweicloud sdk"""

        self._type = None
        self._used = None
        self._quota = None
        self._min = None
        self._max = None
        self.discriminator = None

        self.type = type
        self.used = used
        self.quota = quota
        self.min = min
        self.max = max

    @property
    def type(self):
        """Gets the type of this QuotaInfo.

        查询的资源类型。

        :return: The type of this QuotaInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaInfo.

        查询的资源类型。

        :param type: The type of this QuotaInfo.
        :type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this QuotaInfo.

        已使用的资源配额。

        :return: The used of this QuotaInfo.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this QuotaInfo.

        已使用的资源配额。

        :param used: The used of this QuotaInfo.
        :type: int
        """
        self._used = used

    @property
    def quota(self):
        """Gets the quota of this QuotaInfo.

        查询出的资源的总配额。

        :return: The quota of this QuotaInfo.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this QuotaInfo.

        查询出的资源的总配额。

        :param quota: The quota of this QuotaInfo.
        :type: int
        """
        self._quota = quota

    @property
    def min(self):
        """Gets the min of this QuotaInfo.

        资源的最小配额。

        :return: The min of this QuotaInfo.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this QuotaInfo.

        资源的最小配额。

        :param min: The min of this QuotaInfo.
        :type: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this QuotaInfo.

        资源的最大配额。

        :return: The max of this QuotaInfo.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this QuotaInfo.

        资源的最大配额。

        :param max: The max of this QuotaInfo.
        :type: int
        """
        self._max = max

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
        if not isinstance(other, QuotaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
