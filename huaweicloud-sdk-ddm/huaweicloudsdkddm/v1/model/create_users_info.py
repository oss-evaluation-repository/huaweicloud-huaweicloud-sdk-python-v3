# coding: utf-8

import re
import six





class CreateUsersInfo:


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
        'password': 'str',
        'base_authority': 'list[str]',
        'extend_authority': 'list[str]',
        'description': 'str',
        'databases': 'list[CreateUsersDatabases]'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password',
        'base_authority': 'base_authority',
        'extend_authority': 'extend_authority',
        'description': 'description',
        'databases': 'databases'
    }

    def __init__(self, name=None, password=None, base_authority=None, extend_authority=None, description=None, databases=None):
        """CreateUsersInfo - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._password = None
        self._base_authority = None
        self._extend_authority = None
        self._description = None
        self._databases = None
        self.discriminator = None

        self.name = name
        self.password = password
        self.base_authority = base_authority
        if extend_authority is not None:
            self.extend_authority = extend_authority
        if description is not None:
            self.description = description
        if databases is not None:
            self.databases = databases

    @property
    def name(self):
        """Gets the name of this CreateUsersInfo.

        DDM实例帐号名称，命名要求如下。  - 长度为6-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。

        :return: The name of this CreateUsersInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateUsersInfo.

        DDM实例帐号名称，命名要求如下。  - 长度为6-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。

        :param name: The name of this CreateUsersInfo.
        :type: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this CreateUsersInfo.

        DDM实例帐号密码。

        :return: The password of this CreateUsersInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateUsersInfo.

        DDM实例帐号密码。

        :param password: The password of this CreateUsersInfo.
        :type: str
        """
        self._password = password

    @property
    def base_authority(self):
        """Gets the base_authority of this CreateUsersInfo.

        DDM实例帐号的基础权限。  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT

        :return: The base_authority of this CreateUsersInfo.
        :rtype: list[str]
        """
        return self._base_authority

    @base_authority.setter
    def base_authority(self, base_authority):
        """Sets the base_authority of this CreateUsersInfo.

        DDM实例帐号的基础权限。  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT

        :param base_authority: The base_authority of this CreateUsersInfo.
        :type: list[str]
        """
        self._base_authority = base_authority

    @property
    def extend_authority(self):
        """Gets the extend_authority of this CreateUsersInfo.

        DDM实例帐号的扩展权限，默认值为空。  取值范围为：fulltableDelete、fulltableSelect、fulltableUpdate。  说明： 权限配置应该遵循如下原则：  请至少选择一个基础权限，且扩展权限对应的基础权限必须选择，对应关系如下：   - “fulltableSelect”对应“SELECT”   - “fulltableDelete”对应“DELETE”   - “fulltableUpdate”对应“UPDATE”

        :return: The extend_authority of this CreateUsersInfo.
        :rtype: list[str]
        """
        return self._extend_authority

    @extend_authority.setter
    def extend_authority(self, extend_authority):
        """Sets the extend_authority of this CreateUsersInfo.

        DDM实例帐号的扩展权限，默认值为空。  取值范围为：fulltableDelete、fulltableSelect、fulltableUpdate。  说明： 权限配置应该遵循如下原则：  请至少选择一个基础权限，且扩展权限对应的基础权限必须选择，对应关系如下：   - “fulltableSelect”对应“SELECT”   - “fulltableDelete”对应“DELETE”   - “fulltableUpdate”对应“UPDATE”

        :param extend_authority: The extend_authority of this CreateUsersInfo.
        :type: list[str]
        """
        self._extend_authority = extend_authority

    @property
    def description(self):
        """Gets the description of this CreateUsersInfo.

        DDM实例帐号的描述，最大长度不能超过256。默认值为空。

        :return: The description of this CreateUsersInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateUsersInfo.

        DDM实例帐号的描述，最大长度不能超过256。默认值为空。

        :param description: The description of this CreateUsersInfo.
        :type: str
        """
        self._description = description

    @property
    def databases(self):
        """Gets the databases of this CreateUsersInfo.

        关联的逻辑库的集合。 databases字段可以省略，即创建用户时可以不关联逻辑库。

        :return: The databases of this CreateUsersInfo.
        :rtype: list[CreateUsersDatabases]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this CreateUsersInfo.

        关联的逻辑库的集合。 databases字段可以省略，即创建用户时可以不关联逻辑库。

        :param databases: The databases of this CreateUsersInfo.
        :type: list[CreateUsersDatabases]
        """
        self._databases = databases

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
        if not isinstance(other, CreateUsersInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other