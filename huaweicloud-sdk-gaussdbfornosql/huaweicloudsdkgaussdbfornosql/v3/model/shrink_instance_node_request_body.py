# coding: utf-8

import re
import six





class ShrinkInstanceNodeRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'num': 'int',
        'node_list': 'list[str]'
    }

    attribute_map = {
        'num': 'num',
        'node_list': 'node_list'
    }

    def __init__(self, num=None, node_list=None):
        """ShrinkInstanceNodeRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._num = None
        self._node_list = None
        self.discriminator = None

        if num is not None:
            self.num = num
        if node_list is not None:
            self.node_list = node_list

    @property
    def num(self):
        """Gets the num of this ShrinkInstanceNodeRequestBody.

        随机缩减的节点数量。该字段取值为1。说明：如果客户端采用直连节点方式，不推荐使用随机节点缩容。

        :return: The num of this ShrinkInstanceNodeRequestBody.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this ShrinkInstanceNodeRequestBody.

        随机缩减的节点数量。该字段取值为1。说明：如果客户端采用直连节点方式，不推荐使用随机节点缩容。

        :param num: The num of this ShrinkInstanceNodeRequestBody.
        :type: int
        """
        self._num = num

    @property
    def node_list(self):
        """Gets the node_list of this ShrinkInstanceNodeRequestBody.

        指定缩容节点的ID，且该节点必须支持节点缩容。如果该字段不传指定缩减的节点ID，将根据系统内部策略缩减指定个数的节点。说明： - num与node_list必须有一个字段传值。   - 如果num传值时，取值必须为1。   - 如果node_list传值时，其长度必须为1。   - 如果num与node_list同时传值时，则以node_list的值为主。 - 如果node_list取值为空时，缩容以随机节点缩容进行；node_list字段取值不为空，缩容以指定节点ID进行。 - 节点缩容前，请避免直连节点，以防该节点缩容导致业务中断。

        :return: The node_list of this ShrinkInstanceNodeRequestBody.
        :rtype: list[str]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        """Sets the node_list of this ShrinkInstanceNodeRequestBody.

        指定缩容节点的ID，且该节点必须支持节点缩容。如果该字段不传指定缩减的节点ID，将根据系统内部策略缩减指定个数的节点。说明： - num与node_list必须有一个字段传值。   - 如果num传值时，取值必须为1。   - 如果node_list传值时，其长度必须为1。   - 如果num与node_list同时传值时，则以node_list的值为主。 - 如果node_list取值为空时，缩容以随机节点缩容进行；node_list字段取值不为空，缩容以指定节点ID进行。 - 节点缩容前，请避免直连节点，以防该节点缩容导致业务中断。

        :param node_list: The node_list of this ShrinkInstanceNodeRequestBody.
        :type: list[str]
        """
        self._node_list = node_list

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
        if not isinstance(other, ShrinkInstanceNodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
