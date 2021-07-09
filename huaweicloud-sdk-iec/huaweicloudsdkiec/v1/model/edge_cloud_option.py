# coding: utf-8

import re
import six





class EdgeCloudOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'description': 'str',
        'coverage': 'Coverage',
        'stack': 'Stack'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'coverage': 'coverage',
        'stack': 'stack'
    }

    def __init__(self, name=None, id=None, description=None, coverage=None, stack=None):
        """EdgeCloudOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._id = None
        self._description = None
        self._coverage = None
        self._stack = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        self.coverage = coverage
        self.stack = stack

    @property
    def name(self):
        """Gets the name of this EdgeCloudOption.

        边缘业务名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-32]个字符。

        :return: The name of this EdgeCloudOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeCloudOption.

        边缘业务名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-32]个字符。

        :param name: The name of this EdgeCloudOption.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this EdgeCloudOption.

        已有边缘业务ID，该参数用于扩容边缘业务场景。 >-  id与name不可同时为空，同时有值时部署计划无效； - 通过id扩容场景要求区域分布层级与原边缘业务一致； - 区域分布层级为站点级的边缘业务不支持扩容。

        :return: The id of this EdgeCloudOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgeCloudOption.

        已有边缘业务ID，该参数用于扩容边缘业务场景。 >-  id与name不可同时为空，同时有值时部署计划无效； - 通过id扩容场景要求区域分布层级与原边缘业务一致； - 区域分布层级为站点级的边缘业务不支持扩容。

        :param id: The id of this EdgeCloudOption.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this EdgeCloudOption.

        描述，缺省值为空字符串。

        :return: The description of this EdgeCloudOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgeCloudOption.

        描述，缺省值为空字符串。

        :param description: The description of this EdgeCloudOption.
        :type: str
        """
        self._description = description

    @property
    def coverage(self):
        """Gets the coverage of this EdgeCloudOption.


        :return: The coverage of this EdgeCloudOption.
        :rtype: Coverage
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """Sets the coverage of this EdgeCloudOption.


        :param coverage: The coverage of this EdgeCloudOption.
        :type: Coverage
        """
        self._coverage = coverage

    @property
    def stack(self):
        """Gets the stack of this EdgeCloudOption.


        :return: The stack of this EdgeCloudOption.
        :rtype: Stack
        """
        return self._stack

    @stack.setter
    def stack(self, stack):
        """Sets the stack of this EdgeCloudOption.


        :param stack: The stack of this EdgeCloudOption.
        :type: Stack
        """
        self._stack = stack

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
        if not isinstance(other, EdgeCloudOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
