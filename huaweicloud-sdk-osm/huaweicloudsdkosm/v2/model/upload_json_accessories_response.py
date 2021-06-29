# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UploadJsonAccessoriesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'accessory_id': 'str'
    }

    attribute_map = {
        'accessory_id': 'accessory_id'
    }

    def __init__(self, accessory_id=None):
        """UploadJsonAccessoriesResponse - a model defined in huaweicloud sdk"""
        
        super(UploadJsonAccessoriesResponse, self).__init__()

        self._accessory_id = None
        self.discriminator = None

        if accessory_id is not None:
            self.accessory_id = accessory_id

    @property
    def accessory_id(self):
        """Gets the accessory_id of this UploadJsonAccessoriesResponse.

        附件id

        :return: The accessory_id of this UploadJsonAccessoriesResponse.
        :rtype: str
        """
        return self._accessory_id

    @accessory_id.setter
    def accessory_id(self, accessory_id):
        """Sets the accessory_id of this UploadJsonAccessoriesResponse.

        附件id

        :param accessory_id: The accessory_id of this UploadJsonAccessoriesResponse.
        :type: str
        """
        self._accessory_id = accessory_id

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
        if not isinstance(other, UploadJsonAccessoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other