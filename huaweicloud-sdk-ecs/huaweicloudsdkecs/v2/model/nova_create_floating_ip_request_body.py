# coding: utf-8

import pprint
import re

import six


class NovaCreateFloatingIpRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'pool': 'str'
    }

    attribute_map = {
        'pool': 'pool'
    }

    def __init__(self, pool=None):  # noqa: E501
        """NovaCreateFloatingIpRequestBody - a model defined in huaweicloud sdk"""

        self._pool = None
        self.discriminator = None

        if pool is not None:
            self.pool = pool

    @property
    def pool(self):
        """Gets the pool of this NovaCreateFloatingIpRequestBody.

        用于分配浮动IP的资源池的名字，如果不指定，则使用默认资源池。

        :return: The pool of this NovaCreateFloatingIpRequestBody.
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this NovaCreateFloatingIpRequestBody.

        用于分配浮动IP的资源池的名字，如果不指定，则使用默认资源池。

        :param pool: The pool of this NovaCreateFloatingIpRequestBody.
        :type: str
        """
        self._pool = pool

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
        if not isinstance(other, NovaCreateFloatingIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
