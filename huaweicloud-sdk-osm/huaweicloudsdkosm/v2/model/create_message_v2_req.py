# coding: utf-8

import pprint
import re

import six





class CreateMessageV2Req:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message': 'CreateMessageDoV2',
        'group_id': 'str'
    }

    attribute_map = {
        'message': 'message',
        'group_id': 'group_id'
    }

    def __init__(self, message=None, group_id=None):
        """CreateMessageV2Req - a model defined in huaweicloud sdk"""
        
        

        self._message = None
        self._group_id = None
        self.discriminator = None

        self.message = message
        if group_id is not None:
            self.group_id = group_id

    @property
    def message(self):
        """Gets the message of this CreateMessageV2Req.


        :return: The message of this CreateMessageV2Req.
        :rtype: CreateMessageDoV2
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateMessageV2Req.


        :param message: The message of this CreateMessageV2Req.
        :type: CreateMessageDoV2
        """
        self._message = message

    @property
    def group_id(self):
        """Gets the group_id of this CreateMessageV2Req.

        组id

        :return: The group_id of this CreateMessageV2Req.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateMessageV2Req.

        组id

        :param group_id: The group_id of this CreateMessageV2Req.
        :type: str
        """
        self._group_id = group_id

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
        if not isinstance(other, CreateMessageV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other