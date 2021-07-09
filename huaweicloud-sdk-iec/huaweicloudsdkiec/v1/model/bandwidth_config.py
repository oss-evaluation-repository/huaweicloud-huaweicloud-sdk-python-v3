# coding: utf-8

import re
import six





class BandwidthConfig:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sharetype': 'str',
        'size': 'int'
    }

    attribute_map = {
        'sharetype': 'sharetype',
        'size': 'size'
    }

    def __init__(self, sharetype=None, size=None):
        """BandwidthConfig - a model defined in huaweicloud sdk"""
        
        

        self._sharetype = None
        self._size = None
        self.discriminator = None

        self.sharetype = sharetype
        if size is not None:
            self.size = size

    @property
    def sharetype(self):
        """Gets the sharetype of this BandwidthConfig.

        带宽类型，现支持WHOLE类型，即共享带宽，其他类型不支持。

        :return: The sharetype of this BandwidthConfig.
        :rtype: str
        """
        return self._sharetype

    @sharetype.setter
    def sharetype(self, sharetype):
        """Sets the sharetype of this BandwidthConfig.

        带宽类型，现支持WHOLE类型，即共享带宽，其他类型不支持。

        :param sharetype: The sharetype of this BandwidthConfig.
        :type: str
        """
        self._sharetype = sharetype

    @property
    def size(self):
        """Gets the size of this BandwidthConfig.

        带宽（Mbit/s）。 

        :return: The size of this BandwidthConfig.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BandwidthConfig.

        带宽（Mbit/s）。 

        :param size: The size of this BandwidthConfig.
        :type: int
        """
        self._size = size

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
        if not isinstance(other, BandwidthConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
