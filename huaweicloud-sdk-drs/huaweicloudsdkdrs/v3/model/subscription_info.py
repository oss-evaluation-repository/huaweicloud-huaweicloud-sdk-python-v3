# coding: utf-8

import pprint
import re

import six





class SubscriptionInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'endpoints': 'list[str]',
        'protocol': 'str'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'protocol': 'protocol'
    }

    def __init__(self, endpoints=None, protocol=None):
        """SubscriptionInfo - a model defined in huaweicloud sdk"""
        
        

        self._endpoints = None
        self._protocol = None
        self.discriminator = None

        self.endpoints = endpoints
        self.protocol = protocol

    @property
    def endpoints(self):
        """Gets the endpoints of this SubscriptionInfo.

        短信或者邮件列表

        :return: The endpoints of this SubscriptionInfo.
        :rtype: list[str]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this SubscriptionInfo.

        短信或者邮件列表

        :param endpoints: The endpoints of this SubscriptionInfo.
        :type: list[str]
        """
        self._endpoints = endpoints

    @property
    def protocol(self):
        """Gets the protocol of this SubscriptionInfo.

        收件方式，sms：短信,email：邮件

        :return: The protocol of this SubscriptionInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SubscriptionInfo.

        收件方式，sms：短信,email：邮件

        :param protocol: The protocol of this SubscriptionInfo.
        :type: str
        """
        self._protocol = protocol

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
        if not isinstance(other, SubscriptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other