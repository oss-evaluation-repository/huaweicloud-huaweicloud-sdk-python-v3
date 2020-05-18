# coding: utf-8

import pprint
import re

import six


class TextDetectionItemsReq(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'text': 'str',
        'type': 'str'
    }

    attribute_map = {
        'text': 'text',
        'type': 'type'
    }

    def __init__(self, text=None, type=None):  # noqa: E501
        """TextDetectionItemsReq - a model defined in huaweicloud sdk"""

        self._text = None
        self._type = None
        self.discriminator = None

        self.text = text
        if type is not None:
            self.type = type

    @property
    def text(self):
        """Gets the text of this TextDetectionItemsReq.

        待检测文本，编码格式为“utf-8”，限定5000个字符以内，文本长度超过5000个字符时，只检测前5000个字符。

        :return: The text of this TextDetectionItemsReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextDetectionItemsReq.

        待检测文本，编码格式为“utf-8”，限定5000个字符以内，文本长度超过5000个字符时，只检测前5000个字符。

        :param text: The text of this TextDetectionItemsReq.
        :type: str
        """
        self._text = text

    @property
    def type(self):
        """Gets the type of this TextDetectionItemsReq.

        文本类型，默认为“content”，即正文内容，当前只支持“content”类型，未来会扩大支持类型范围。

        :return: The type of this TextDetectionItemsReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TextDetectionItemsReq.

        文本类型，默认为“content”，即正文内容，当前只支持“content”类型，未来会扩大支持类型范围。

        :param type: The type of this TextDetectionItemsReq.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, TextDetectionItemsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
