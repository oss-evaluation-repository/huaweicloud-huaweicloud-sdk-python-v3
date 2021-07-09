# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateInstanceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'order_id': 'order_id'
    }

    def __init__(self, id=None, order_id=None):
        """CreateInstanceResponse - a model defined in huaweicloud sdk"""
        
        super(CreateInstanceResponse, self).__init__()

        self._id = None
        self._order_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if order_id is not None:
            self.order_id = order_id

    @property
    def id(self):
        """Gets the id of this CreateInstanceResponse.

        实例ID。创建按需付费实例时返回该参数。

        :return: The id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateInstanceResponse.

        实例ID。创建按需付费实例时返回该参数。

        :param id: The id of this CreateInstanceResponse.
        :type: str
        """
        self._id = id

    @property
    def order_id(self):
        """Gets the order_id of this CreateInstanceResponse.

        订单号，创建包年/包月实例时返回该参数。

        :return: The order_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateInstanceResponse.

        订单号，创建包年/包月实例时返回该参数。

        :param order_id: The order_id of this CreateInstanceResponse.
        :type: str
        """
        self._order_id = order_id

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
        if not isinstance(other, CreateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
