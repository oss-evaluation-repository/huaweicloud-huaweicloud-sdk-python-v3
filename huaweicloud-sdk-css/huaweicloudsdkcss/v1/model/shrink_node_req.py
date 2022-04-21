# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShrinkNodeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'reduced_node_num': 'int',
        'type': 'str'
    }

    attribute_map = {
        'reduced_node_num': 'reducedNodeNum',
        'type': 'type'
    }

    def __init__(self, reduced_node_num=None, type=None):
        """ShrinkNodeReq

        The model defined in huaweicloud sdk

        :param reduced_node_num: 下线节点个数。 没有Master节点的集群，缩容后剩余的数据节点个数(包含冷数据节点和其他类型节点)须大于之前的一半。 有Master节点的集群，缩容后Master节点的总数须为大于等于3的奇数。 跨AZ的集群，缩容后须确保剩余的节点个数大等于AZ个数。
        :type reduced_node_num: int
        :param type: 下线节点类型。（ess、ess-master、ess-client、ess-cold、lgs）
        :type type: str
        """
        
        

        self._reduced_node_num = None
        self._type = None
        self.discriminator = None

        self.reduced_node_num = reduced_node_num
        self.type = type

    @property
    def reduced_node_num(self):
        """Gets the reduced_node_num of this ShrinkNodeReq.

        下线节点个数。 没有Master节点的集群，缩容后剩余的数据节点个数(包含冷数据节点和其他类型节点)须大于之前的一半。 有Master节点的集群，缩容后Master节点的总数须为大于等于3的奇数。 跨AZ的集群，缩容后须确保剩余的节点个数大等于AZ个数。

        :return: The reduced_node_num of this ShrinkNodeReq.
        :rtype: int
        """
        return self._reduced_node_num

    @reduced_node_num.setter
    def reduced_node_num(self, reduced_node_num):
        """Sets the reduced_node_num of this ShrinkNodeReq.

        下线节点个数。 没有Master节点的集群，缩容后剩余的数据节点个数(包含冷数据节点和其他类型节点)须大于之前的一半。 有Master节点的集群，缩容后Master节点的总数须为大于等于3的奇数。 跨AZ的集群，缩容后须确保剩余的节点个数大等于AZ个数。

        :param reduced_node_num: The reduced_node_num of this ShrinkNodeReq.
        :type reduced_node_num: int
        """
        self._reduced_node_num = reduced_node_num

    @property
    def type(self):
        """Gets the type of this ShrinkNodeReq.

        下线节点类型。（ess、ess-master、ess-client、ess-cold、lgs）

        :return: The type of this ShrinkNodeReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShrinkNodeReq.

        下线节点类型。（ess、ess-master、ess-client、ess-cold、lgs）

        :param type: The type of this ShrinkNodeReq.
        :type type: str
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
        if not isinstance(other, ShrinkNodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
