# coding: utf-8

import pprint
import re

import six





class TrafficMark:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sip': 'list[str]',
        'cookie': 'str',
        'params': 'str'
    }

    attribute_map = {
        'sip': 'sip',
        'cookie': 'cookie',
        'params': 'params'
    }

    def __init__(self, sip=None, cookie=None, params=None):
        """TrafficMark - a model defined in huaweicloud sdk"""
        
        

        self._sip = None
        self._cookie = None
        self._params = None
        self.discriminator = None

        if sip is not None:
            self.sip = sip
        if cookie is not None:
            self.cookie = cookie
        if params is not None:
            self.params = params

    @property
    def sip(self):
        """Gets the sip of this TrafficMark.

        惩罚ip

        :return: The sip of this TrafficMark.
        :rtype: list[str]
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        """Sets the sip of this TrafficMark.

        惩罚ip

        :param sip: The sip of this TrafficMark.
        :type: list[str]
        """
        self._sip = sip

    @property
    def cookie(self):
        """Gets the cookie of this TrafficMark.

        cookie

        :return: The cookie of this TrafficMark.
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this TrafficMark.

        cookie

        :param cookie: The cookie of this TrafficMark.
        :type: str
        """
        self._cookie = cookie

    @property
    def params(self):
        """Gets the params of this TrafficMark.

        参数

        :return: The params of this TrafficMark.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this TrafficMark.

        参数

        :param params: The params of this TrafficMark.
        :type: str
        """
        self._params = params

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
        if not isinstance(other, TrafficMark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other