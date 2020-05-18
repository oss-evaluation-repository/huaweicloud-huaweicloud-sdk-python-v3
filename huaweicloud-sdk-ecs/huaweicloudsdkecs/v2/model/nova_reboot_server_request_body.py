# coding: utf-8

import pprint
import re

import six


class NovaRebootServerRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'reboot': 'NovaRebootServerOption'
    }

    attribute_map = {
        'reboot': 'reboot'
    }

    def __init__(self, reboot=None):  # noqa: E501
        """NovaRebootServerRequestBody - a model defined in huaweicloud sdk"""

        self._reboot = None
        self.discriminator = None

        self.reboot = reboot

    @property
    def reboot(self):
        """Gets the reboot of this NovaRebootServerRequestBody.


        :return: The reboot of this NovaRebootServerRequestBody.
        :rtype: NovaRebootServerOption
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        """Sets the reboot of this NovaRebootServerRequestBody.


        :param reboot: The reboot of this NovaRebootServerRequestBody.
        :type: NovaRebootServerOption
        """
        self._reboot = reboot

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
        if not isinstance(other, NovaRebootServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
