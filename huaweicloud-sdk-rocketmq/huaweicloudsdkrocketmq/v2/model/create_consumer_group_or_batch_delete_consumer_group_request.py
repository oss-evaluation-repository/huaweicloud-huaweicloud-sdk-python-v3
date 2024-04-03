# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConsumerGroupOrBatchDeleteConsumerGroupRequest:

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
        'action': 'str',
        'body': 'CreateConsumerGroupOrBatchDeleteConsumerGroupReq'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, instance_id=None, action=None, body=None):
        """CreateConsumerGroupOrBatchDeleteConsumerGroupRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param action: 批量删除消费组时使用，不配置则为创建接口。删除操作：delete。
        :type action: str
        :param body: Body of the CreateConsumerGroupOrBatchDeleteConsumerGroupRequest
        :type body: :class:`huaweicloudsdkrocketmq.v2.CreateConsumerGroupOrBatchDeleteConsumerGroupReq`
        """
        
        

        self._instance_id = None
        self._action = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        if action is not None:
            self.action = action
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.

        实例ID。

        :return: The instance_id of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.

        实例ID。

        :param instance_id: The instance_id of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def action(self):
        """Gets the action of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.

        批量删除消费组时使用，不配置则为创建接口。删除操作：delete。

        :return: The action of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.

        批量删除消费组时使用，不配置则为创建接口。删除操作：delete。

        :param action: The action of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        """Gets the body of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.

        :return: The body of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.
        :rtype: :class:`huaweicloudsdkrocketmq.v2.CreateConsumerGroupOrBatchDeleteConsumerGroupReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.

        :param body: The body of this CreateConsumerGroupOrBatchDeleteConsumerGroupRequest.
        :type body: :class:`huaweicloudsdkrocketmq.v2.CreateConsumerGroupOrBatchDeleteConsumerGroupReq`
        """
        self._body = body

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
        if not isinstance(other, CreateConsumerGroupOrBatchDeleteConsumerGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
