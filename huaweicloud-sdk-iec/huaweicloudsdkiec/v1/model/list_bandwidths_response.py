# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListBandwidthsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bandwidths': 'list[Bandwidth]',
        'count': 'int'
    }

    attribute_map = {
        'bandwidths': 'bandwidths',
        'count': 'count'
    }

    def __init__(self, bandwidths=None, count=None):
        """ListBandwidthsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._bandwidths = None
        self._count = None
        self.discriminator = None

        if bandwidths is not None:
            self.bandwidths = bandwidths
        if count is not None:
            self.count = count

    @property
    def bandwidths(self):
        """Gets the bandwidths of this ListBandwidthsResponse.

        带宽列表对象。

        :return: The bandwidths of this ListBandwidthsResponse.
        :rtype: list[Bandwidth]
        """
        return self._bandwidths

    @bandwidths.setter
    def bandwidths(self, bandwidths):
        """Sets the bandwidths of this ListBandwidthsResponse.

        带宽列表对象。

        :param bandwidths: The bandwidths of this ListBandwidthsResponse.
        :type: list[Bandwidth]
        """
        self._bandwidths = bandwidths

    @property
    def count(self):
        """Gets the count of this ListBandwidthsResponse.

        带宽数量。

        :return: The count of this ListBandwidthsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListBandwidthsResponse.

        带宽数量。

        :param count: The count of this ListBandwidthsResponse.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, ListBandwidthsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other