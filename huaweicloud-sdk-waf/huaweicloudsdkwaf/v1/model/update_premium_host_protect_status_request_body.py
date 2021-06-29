# coding: utf-8

import pprint
import re

import six





class UpdatePremiumHostProtectStatusRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'protect_status': 'int'
    }

    attribute_map = {
        'protect_status': 'protect_status'
    }

    def __init__(self, protect_status=None):
        """UpdatePremiumHostProtectStatusRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._protect_status = None
        self.discriminator = None

        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def protect_status(self):
        """Gets the protect_status of this UpdatePremiumHostProtectStatusRequestBody.

        防护状态

        :return: The protect_status of this UpdatePremiumHostProtectStatusRequestBody.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this UpdatePremiumHostProtectStatusRequestBody.

        防护状态

        :param protect_status: The protect_status of this UpdatePremiumHostProtectStatusRequestBody.
        :type: int
        """
        self._protect_status = protect_status

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
        if not isinstance(other, UpdatePremiumHostProtectStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other