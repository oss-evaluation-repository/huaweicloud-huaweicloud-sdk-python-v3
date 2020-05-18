# coding: utf-8

import pprint
import re

import six


class NovaResizeServerRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'resize': 'NovaResizeServerOption'
    }

    attribute_map = {
        'resize': 'resize'
    }

    def __init__(self, resize=None):  # noqa: E501
        """NovaResizeServerRequestBody - a model defined in huaweicloud sdk"""

        self._resize = None
        self.discriminator = None

        self.resize = resize

    @property
    def resize(self):
        """Gets the resize of this NovaResizeServerRequestBody.


        :return: The resize of this NovaResizeServerRequestBody.
        :rtype: NovaResizeServerOption
        """
        return self._resize

    @resize.setter
    def resize(self, resize):
        """Sets the resize of this NovaResizeServerRequestBody.


        :param resize: The resize of this NovaResizeServerRequestBody.
        :type: NovaResizeServerOption
        """
        self._resize = resize

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
        if not isinstance(other, NovaResizeServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
