# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListKmsTagsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'tags': 'tags'
    }

    def __init__(self, tags=None):
        """ListKmsTagsResponse - a model defined in huaweicloud sdk"""
        
        super(ListKmsTagsResponse, self).__init__()

        self._tags = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags

    @property
    def tags(self):
        """Gets the tags of this ListKmsTagsResponse.

        标签列表，key和value键值对的集合。  - key：表示标签键，一个密钥下最多包含10个key，key不能为空，不能重复，同一个key中value不能重复。key最大长度为36个字符。  - value：表示标签值。每个值最大长度43个字符，value之间为“与”的关系。

        :return: The tags of this ListKmsTagsResponse.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListKmsTagsResponse.

        标签列表，key和value键值对的集合。  - key：表示标签键，一个密钥下最多包含10个key，key不能为空，不能重复，同一个key中value不能重复。key最大长度为36个字符。  - value：表示标签值。每个值最大长度43个字符，value之间为“与”的关系。

        :param tags: The tags of this ListKmsTagsResponse.
        :type: list[Tag]
        """
        self._tags = tags

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
        if not isinstance(other, ListKmsTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
