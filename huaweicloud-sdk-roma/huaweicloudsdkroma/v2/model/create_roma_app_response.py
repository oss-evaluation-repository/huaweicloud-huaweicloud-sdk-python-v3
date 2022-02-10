# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRomaAppResponse(SdkResponse):


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
        'name': 'str',
        'remark': 'str',
        'roles': 'list[str]',
        'create_time': 'str',
        'update_time': 'str',
        'created_user': 'ServerAppInfoCreatedUser',
        'last_updated_user': 'ServerAppInfoLastUpdatedUser',
        'owner': 'bool',
        'key': 'str',
        'favorite': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'remark': 'remark',
        'roles': 'roles',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'created_user': 'created_user',
        'last_updated_user': 'last_updated_user',
        'owner': 'owner',
        'key': 'key',
        'favorite': 'favorite'
    }

    def __init__(self, id=None, name=None, remark=None, roles=None, create_time=None, update_time=None, created_user=None, last_updated_user=None, owner=None, key=None, favorite=None):
        """CreateRomaAppResponse - a model defined in huaweicloud sdk"""
        
        super(CreateRomaAppResponse, self).__init__()

        self._id = None
        self._name = None
        self._remark = None
        self._roles = None
        self._create_time = None
        self._update_time = None
        self._created_user = None
        self._last_updated_user = None
        self._owner = None
        self._key = None
        self._favorite = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if roles is not None:
            self.roles = roles
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if created_user is not None:
            self.created_user = created_user
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user
        if owner is not None:
            self.owner = owner
        if key is not None:
            self.key = key
        if favorite is not None:
            self.favorite = favorite

    @property
    def id(self):
        """Gets the id of this CreateRomaAppResponse.

        应用ID

        :return: The id of this CreateRomaAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRomaAppResponse.

        应用ID

        :param id: The id of this CreateRomaAppResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateRomaAppResponse.

        应用名称 - 字符集：支持中文、英文字母、数字、中划线、下划线、点、空格和中英文圆括号 - 约束：实例下唯一

        :return: The name of this CreateRomaAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRomaAppResponse.

        应用名称 - 字符集：支持中文、英文字母、数字、中划线、下划线、点、空格和中英文圆括号 - 约束：实例下唯一

        :param name: The name of this CreateRomaAppResponse.
        :type: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this CreateRomaAppResponse.

        应用描述

        :return: The remark of this CreateRomaAppResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateRomaAppResponse.

        应用描述

        :param remark: The remark of this CreateRomaAppResponse.
        :type: str
        """
        self._remark = remark

    @property
    def roles(self):
        """Gets the roles of this CreateRomaAppResponse.

        应用权限角色 - read：应用下资源只读权限，至少要存在此权限，包括API调试 - access：应用下资源的访问管理权限 - delete：应用下资源的删除权限 - modify：应用下资源的修改权限，包括API发布、下线 - admin：应用和应用下资源的权限 - 仅提供admin时，会自动应用其它所有权限 - 未提供read时会自动应用read权限

        :return: The roles of this CreateRomaAppResponse.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CreateRomaAppResponse.

        应用权限角色 - read：应用下资源只读权限，至少要存在此权限，包括API调试 - access：应用下资源的访问管理权限 - delete：应用下资源的删除权限 - modify：应用下资源的修改权限，包括API发布、下线 - admin：应用和应用下资源的权限 - 仅提供admin时，会自动应用其它所有权限 - 未提供read时会自动应用read权限

        :param roles: The roles of this CreateRomaAppResponse.
        :type: list[str]
        """
        self._roles = roles

    @property
    def create_time(self):
        """Gets the create_time of this CreateRomaAppResponse.

        创建UTC时间

        :return: The create_time of this CreateRomaAppResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateRomaAppResponse.

        创建UTC时间

        :param create_time: The create_time of this CreateRomaAppResponse.
        :type: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateRomaAppResponse.

        创建UTC时间

        :return: The update_time of this CreateRomaAppResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateRomaAppResponse.

        创建UTC时间

        :param update_time: The update_time of this CreateRomaAppResponse.
        :type: str
        """
        self._update_time = update_time

    @property
    def created_user(self):
        """Gets the created_user of this CreateRomaAppResponse.


        :return: The created_user of this CreateRomaAppResponse.
        :rtype: ServerAppInfoCreatedUser
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        """Sets the created_user of this CreateRomaAppResponse.


        :param created_user: The created_user of this CreateRomaAppResponse.
        :type: ServerAppInfoCreatedUser
        """
        self._created_user = created_user

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this CreateRomaAppResponse.


        :return: The last_updated_user of this CreateRomaAppResponse.
        :rtype: ServerAppInfoLastUpdatedUser
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this CreateRomaAppResponse.


        :param last_updated_user: The last_updated_user of this CreateRomaAppResponse.
        :type: ServerAppInfoLastUpdatedUser
        """
        self._last_updated_user = last_updated_user

    @property
    def owner(self):
        """Gets the owner of this CreateRomaAppResponse.

        是否是应用拥有者

        :return: The owner of this CreateRomaAppResponse.
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateRomaAppResponse.

        是否是应用拥有者

        :param owner: The owner of this CreateRomaAppResponse.
        :type: bool
        """
        self._owner = owner

    @property
    def key(self):
        """Gets the key of this CreateRomaAppResponse.

        应用认证访问KEY,未提供时随机生成 - 字符集：支持中文、英文字母、数字、中划线、下划线、@号和点，以字母或中文或数字开头 - 约束：实例下唯一

        :return: The key of this CreateRomaAppResponse.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateRomaAppResponse.

        应用认证访问KEY,未提供时随机生成 - 字符集：支持中文、英文字母、数字、中划线、下划线、@号和点，以字母或中文或数字开头 - 约束：实例下唯一

        :param key: The key of this CreateRomaAppResponse.
        :type: str
        """
        self._key = key

    @property
    def favorite(self):
        """Gets the favorite of this CreateRomaAppResponse.

        是否收藏应用，收藏的应用会在列表里优先显示

        :return: The favorite of this CreateRomaAppResponse.
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this CreateRomaAppResponse.

        是否收藏应用，收藏的应用会在列表里优先显示

        :param favorite: The favorite of this CreateRomaAppResponse.
        :type: bool
        """
        self._favorite = favorite

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
        if not isinstance(other, CreateRomaAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other