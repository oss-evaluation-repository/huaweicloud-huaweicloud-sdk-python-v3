# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FreezeSubCustomersReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_ids': 'list[str]',
        'reason': 'str'
    }

    attribute_map = {
        'customer_ids': 'customer_ids',
        'reason': 'reason'
    }

    def __init__(self, customer_ids=None, reason=None):
        """FreezeSubCustomersReq - a model defined in huaweicloud sdk"""
        
        

        self._customer_ids = None
        self._reason = None
        self.discriminator = None

        self.customer_ids = customer_ids
        self.reason = reason

    @property
    def customer_ids(self):
        """Gets the customer_ids of this FreezeSubCustomersReq.

        需要冻结的客户账号ID列表。 您可以调用查询客户列表接口获取customer_id。

        :return: The customer_ids of this FreezeSubCustomersReq.
        :rtype: list[str]
        """
        return self._customer_ids

    @customer_ids.setter
    def customer_ids(self, customer_ids):
        """Sets the customer_ids of this FreezeSubCustomersReq.

        需要冻结的客户账号ID列表。 您可以调用查询客户列表接口获取customer_id。

        :param customer_ids: The customer_ids of this FreezeSubCustomersReq.
        :type: list[str]
        """
        self._customer_ids = customer_ids

    @property
    def reason(self):
        """Gets the reason of this FreezeSubCustomersReq.

        冻结原因。

        :return: The reason of this FreezeSubCustomersReq.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this FreezeSubCustomersReq.

        冻结原因。

        :param reason: The reason of this FreezeSubCustomersReq.
        :type: str
        """
        self._reason = reason

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
        if not isinstance(other, FreezeSubCustomersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
