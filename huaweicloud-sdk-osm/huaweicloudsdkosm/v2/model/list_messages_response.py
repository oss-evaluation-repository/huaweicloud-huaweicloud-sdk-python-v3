# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListMessagesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'message_list': 'list[QueryMessageInfoV2]'
    }

    attribute_map = {
        'count': 'count',
        'message_list': 'message_list'
    }

    def __init__(self, count=None, message_list=None):
        """ListMessagesResponse - a model defined in huaweicloud sdk"""
        
        super(ListMessagesResponse, self).__init__()

        self._count = None
        self._message_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if message_list is not None:
            self.message_list = message_list

    @property
    def count(self):
        """Gets the count of this ListMessagesResponse.

        总数

        :return: The count of this ListMessagesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListMessagesResponse.

        总数

        :param count: The count of this ListMessagesResponse.
        :type: int
        """
        self._count = count

    @property
    def message_list(self):
        """Gets the message_list of this ListMessagesResponse.

        留言列表

        :return: The message_list of this ListMessagesResponse.
        :rtype: list[QueryMessageInfoV2]
        """
        return self._message_list

    @message_list.setter
    def message_list(self, message_list):
        """Sets the message_list of this ListMessagesResponse.

        留言列表

        :param message_list: The message_list of this ListMessagesResponse.
        :type: list[QueryMessageInfoV2]
        """
        self._message_list = message_list

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
        if not isinstance(other, ListMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other