# coding: utf-8

import re
import six





class ListenerIpGroup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ipgroup_id': 'str',
        'enable_ipgroup': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'ipgroup_id': 'ipgroup_id',
        'enable_ipgroup': 'enable_ipgroup',
        'type': 'type'
    }

    def __init__(self, ipgroup_id=None, enable_ipgroup=None, type=None):
        """ListenerIpGroup - a model defined in huaweicloud sdk"""
        
        

        self._ipgroup_id = None
        self._enable_ipgroup = None
        self._type = None
        self.discriminator = None

        self.ipgroup_id = ipgroup_id
        self.enable_ipgroup = enable_ipgroup
        self.type = type

    @property
    def ipgroup_id(self):
        """Gets the ipgroup_id of this ListenerIpGroup.

        监听器关联的访问控制组的id。 创建时必选，更新时非必选。 指定的ipgroup必须已存在，不能指定为null，否则与enable_ipgroup冲突。 

        :return: The ipgroup_id of this ListenerIpGroup.
        :rtype: str
        """
        return self._ipgroup_id

    @ipgroup_id.setter
    def ipgroup_id(self, ipgroup_id):
        """Sets the ipgroup_id of this ListenerIpGroup.

        监听器关联的访问控制组的id。 创建时必选，更新时非必选。 指定的ipgroup必须已存在，不能指定为null，否则与enable_ipgroup冲突。 

        :param ipgroup_id: The ipgroup_id of this ListenerIpGroup.
        :type: str
        """
        self._ipgroup_id = ipgroup_id

    @property
    def enable_ipgroup(self):
        """Gets the enable_ipgroup of this ListenerIpGroup.

        访问控制组的状态。 True:开启访问控制； Flase：关闭访问控制； 开启访问控制的监听器，允许直接删除。

        :return: The enable_ipgroup of this ListenerIpGroup.
        :rtype: bool
        """
        return self._enable_ipgroup

    @enable_ipgroup.setter
    def enable_ipgroup(self, enable_ipgroup):
        """Sets the enable_ipgroup of this ListenerIpGroup.

        访问控制组的状态。 True:开启访问控制； Flase：关闭访问控制； 开启访问控制的监听器，允许直接删除。

        :param enable_ipgroup: The enable_ipgroup of this ListenerIpGroup.
        :type: bool
        """
        self._enable_ipgroup = enable_ipgroup

    @property
    def type(self):
        """Gets the type of this ListenerIpGroup.

        访问控制组的类型。 white:白名单，只允许指定ip访问； black:黑名单，不允许指定ip访问； 

        :return: The type of this ListenerIpGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListenerIpGroup.

        访问控制组的类型。 white:白名单，只允许指定ip访问； black:黑名单，不允许指定ip访问； 

        :param type: The type of this ListenerIpGroup.
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
        if not isinstance(other, ListenerIpGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
