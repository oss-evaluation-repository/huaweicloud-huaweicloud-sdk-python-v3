# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMqsInstanceTopicAccessPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'topic_name': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'topic_name': 'topic_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, topic_name=None, offset=None, limit=None):
        """ShowMqsInstanceTopicAccessPolicyRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param topic_name: topic名称。
        :type topic_name: str
        :param offset: 分页查询偏移量。
        :type offset: str
        :param limit: 分页查询大小。
        :type limit: str
        """
        
        

        self._instance_id = None
        self._topic_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.topic_name = topic_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowMqsInstanceTopicAccessPolicyRequest.

        实例ID。

        :return: The instance_id of this ShowMqsInstanceTopicAccessPolicyRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowMqsInstanceTopicAccessPolicyRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowMqsInstanceTopicAccessPolicyRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic_name(self):
        """Gets the topic_name of this ShowMqsInstanceTopicAccessPolicyRequest.

        topic名称。

        :return: The topic_name of this ShowMqsInstanceTopicAccessPolicyRequest.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this ShowMqsInstanceTopicAccessPolicyRequest.

        topic名称。

        :param topic_name: The topic_name of this ShowMqsInstanceTopicAccessPolicyRequest.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def offset(self):
        """Gets the offset of this ShowMqsInstanceTopicAccessPolicyRequest.

        分页查询偏移量。

        :return: The offset of this ShowMqsInstanceTopicAccessPolicyRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMqsInstanceTopicAccessPolicyRequest.

        分页查询偏移量。

        :param offset: The offset of this ShowMqsInstanceTopicAccessPolicyRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowMqsInstanceTopicAccessPolicyRequest.

        分页查询大小。

        :return: The limit of this ShowMqsInstanceTopicAccessPolicyRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowMqsInstanceTopicAccessPolicyRequest.

        分页查询大小。

        :param limit: The limit of this ShowMqsInstanceTopicAccessPolicyRequest.
        :type limit: str
        """
        self._limit = limit

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowMqsInstanceTopicAccessPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
