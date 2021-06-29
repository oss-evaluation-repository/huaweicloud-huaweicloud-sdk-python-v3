# coding: utf-8

import pprint
import re

import six





class DatabaseInfo:


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
        'parent_id': 'str',
        'object_type': 'str',
        'object_name': 'str',
        'object_alias_name': 'str',
        'select': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'object_type': 'object_type',
        'object_name': 'object_name',
        'object_alias_name': 'object_alias_name',
        'select': 'select'
    }

    def __init__(self, id=None, parent_id=None, object_type=None, object_name=None, object_alias_name=None, select=None):
        """DatabaseInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._parent_id = None
        self._object_type = None
        self._object_name = None
        self._object_alias_name = None
        self._select = None
        self.discriminator = None

        self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        self.object_type = object_type
        self.object_name = object_name
        if object_alias_name is not None:
            self.object_alias_name = object_alias_name
        if select is not None:
            self.select = select

    @property
    def id(self):
        """Gets the id of this DatabaseInfo.

        object_type为database时，为库名；object_type为table或者view时，字段值参考示例。

        :return: The id of this DatabaseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseInfo.

        object_type为database时，为库名；object_type为table或者view时，字段值参考示例。

        :param id: The id of this DatabaseInfo.
        :type: str
        """
        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this DatabaseInfo.

        object_type为table或view时需要填写，为库名

        :return: The parent_id of this DatabaseInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this DatabaseInfo.

        object_type为table或view时需要填写，为库名

        :param parent_id: The parent_id of this DatabaseInfo.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def object_type(self):
        """Gets the object_type of this DatabaseInfo.

        类型

        :return: The object_type of this DatabaseInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this DatabaseInfo.

        类型

        :param object_type: The object_type of this DatabaseInfo.
        :type: str
        """
        self._object_type = object_type

    @property
    def object_name(self):
        """Gets the object_name of this DatabaseInfo.

        数据库对象名称，库名、表名、视图名

        :return: The object_name of this DatabaseInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this DatabaseInfo.

        数据库对象名称，库名、表名、视图名

        :param object_name: The object_name of this DatabaseInfo.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_alias_name(self):
        """Gets the object_alias_name of this DatabaseInfo.

        别名，映射的新名称。

        :return: The object_alias_name of this DatabaseInfo.
        :rtype: str
        """
        return self._object_alias_name

    @object_alias_name.setter
    def object_alias_name(self, object_alias_name):
        """Sets the object_alias_name of this DatabaseInfo.

        别名，映射的新名称。

        :param object_alias_name: The object_alias_name of this DatabaseInfo.
        :type: str
        """
        self._object_alias_name = object_alias_name

    @property
    def select(self):
        """Gets the select of this DatabaseInfo.

        是否选中，值为true会进行迁移，false该数据库对象不会迁移，partial为迁移库下面的部分表，不填默认为false

        :return: The select of this DatabaseInfo.
        :rtype: str
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this DatabaseInfo.

        是否选中，值为true会进行迁移，false该数据库对象不会迁移，partial为迁移库下面的部分表，不填默认为false

        :param select: The select of this DatabaseInfo.
        :type: str
        """
        self._select = select

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
        if not isinstance(other, DatabaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other