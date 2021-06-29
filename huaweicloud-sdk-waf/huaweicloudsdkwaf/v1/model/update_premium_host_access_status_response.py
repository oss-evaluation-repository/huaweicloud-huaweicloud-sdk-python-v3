# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdatePremiumHostAccessStatusResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_status': 'int'
    }

    attribute_map = {
        'access_status': 'access_status'
    }

    def __init__(self, access_status=None):
        """UpdatePremiumHostAccessStatusResponse - a model defined in huaweicloud sdk"""
        
        super(UpdatePremiumHostAccessStatusResponse, self).__init__()

        self._access_status = None
        self.discriminator = None

        if access_status is not None:
            self.access_status = access_status

    @property
    def access_status(self):
        """Gets the access_status of this UpdatePremiumHostAccessStatusResponse.

        域名接入状态

        :return: The access_status of this UpdatePremiumHostAccessStatusResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this UpdatePremiumHostAccessStatusResponse.

        域名接入状态

        :param access_status: The access_status of this UpdatePremiumHostAccessStatusResponse.
        :type: int
        """
        self._access_status = access_status

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
        if not isinstance(other, UpdatePremiumHostAccessStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other