# coding: utf-8

import pprint
import re

import six


class ResizeVolumeRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'bss_param': 'BssParamForResizeVolume',
        'os_extend': 'OsExtend'
    }

    attribute_map = {
        'bss_param': 'bssParam',
        'os_extend': 'os-extend'
    }

    def __init__(self, bss_param=None, os_extend=None):  # noqa: E501
        """ResizeVolumeRequestBody - a model defined in huaweicloud sdk"""

        self._bss_param = None
        self._os_extend = None
        self.discriminator = None

        if bss_param is not None:
            self.bss_param = bss_param
        self.os_extend = os_extend

    @property
    def bss_param(self):
        """Gets the bss_param of this ResizeVolumeRequestBody.


        :return: The bss_param of this ResizeVolumeRequestBody.
        :rtype: BssParamForResizeVolume
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        """Sets the bss_param of this ResizeVolumeRequestBody.


        :param bss_param: The bss_param of this ResizeVolumeRequestBody.
        :type: BssParamForResizeVolume
        """
        self._bss_param = bss_param

    @property
    def os_extend(self):
        """Gets the os_extend of this ResizeVolumeRequestBody.


        :return: The os_extend of this ResizeVolumeRequestBody.
        :rtype: OsExtend
        """
        return self._os_extend

    @os_extend.setter
    def os_extend(self, os_extend):
        """Sets the os_extend of this ResizeVolumeRequestBody.


        :param os_extend: The os_extend of this ResizeVolumeRequestBody.
        :type: OsExtend
        """
        self._os_extend = os_extend

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
        if not isinstance(other, ResizeVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
