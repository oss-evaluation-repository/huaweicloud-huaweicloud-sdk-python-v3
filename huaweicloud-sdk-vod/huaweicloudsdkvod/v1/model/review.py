# coding: utf-8

import pprint
import re

import six





class Review:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_id': 'str'
    }

    attribute_map = {
        'template_id': 'template_id'
    }

    def __init__(self, template_id=None):
        """Review - a model defined in huaweicloud sdk"""
        
        

        self._template_id = None
        self.discriminator = None

        self.template_id = template_id

    @property
    def template_id(self):
        """Gets the template_id of this Review.

        审核模板ID。您可以在视频点播控制台配置审核模板后获取，具体请参见[审核设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0057.html)。

        :return: The template_id of this Review.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this Review.

        审核模板ID。您可以在视频点播控制台配置审核模板后获取，具体请参见[审核设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0057.html)。

        :param template_id: The template_id of this Review.
        :type: str
        """
        self._template_id = template_id

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
        if not isinstance(other, Review):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other