# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistableModelSaveAllDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'creator': 'int',
        'id': 'int',
        'last_update_time': 'str',
        'modifier': 'str',
        'need_set_null_attrs': 'list[str]',
        'rdm_extension_type': 'str',
        'tenant': 'ObjectReferenceParamDTO',
        'unique_key': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'creator': 'creator',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'modifier': 'modifier',
        'need_set_null_attrs': 'needSetNullAttrs',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'unique_key': 'uniqueKey'
    }

    def __init__(self, create_time=None, creator=None, id=None, last_update_time=None, modifier=None, need_set_null_attrs=None, rdm_extension_type=None, tenant=None, unique_key=None):
        """PersistableModelSaveAllDTO

        The model defined in huaweicloud sdk

        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: int
        :param id: 唯一标识。
        :type id: int
        :param last_update_time: 最后更新时间。
        :type last_update_time: str
        :param modifier: 更新者。
        :type modifier: str
        :param need_set_null_attrs: 设置NULL值的属性名称。
        :type need_set_null_attrs: list[str]
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param unique_key: 示例模型的唯一键属性。
        :type unique_key: str
        """
        
        

        self._create_time = None
        self._creator = None
        self._id = None
        self._last_update_time = None
        self._modifier = None
        self._need_set_null_attrs = None
        self._rdm_extension_type = None
        self._tenant = None
        self._unique_key = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if modifier is not None:
            self.modifier = modifier
        if need_set_null_attrs is not None:
            self.need_set_null_attrs = need_set_null_attrs
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant
        if unique_key is not None:
            self.unique_key = unique_key

    @property
    def create_time(self):
        """Gets the create_time of this PersistableModelSaveAllDTO.

        创建时间。

        :return: The create_time of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PersistableModelSaveAllDTO.

        创建时间。

        :param create_time: The create_time of this PersistableModelSaveAllDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this PersistableModelSaveAllDTO.

        创建者。

        :return: The creator of this PersistableModelSaveAllDTO.
        :rtype: int
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PersistableModelSaveAllDTO.

        创建者。

        :param creator: The creator of this PersistableModelSaveAllDTO.
        :type creator: int
        """
        self._creator = creator

    @property
    def id(self):
        """Gets the id of this PersistableModelSaveAllDTO.

        唯一标识。

        :return: The id of this PersistableModelSaveAllDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PersistableModelSaveAllDTO.

        唯一标识。

        :param id: The id of this PersistableModelSaveAllDTO.
        :type id: int
        """
        self._id = id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this PersistableModelSaveAllDTO.

        最后更新时间。

        :return: The last_update_time of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this PersistableModelSaveAllDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this PersistableModelSaveAllDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        """Gets the modifier of this PersistableModelSaveAllDTO.

        更新者。

        :return: The modifier of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this PersistableModelSaveAllDTO.

        更新者。

        :param modifier: The modifier of this PersistableModelSaveAllDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def need_set_null_attrs(self):
        """Gets the need_set_null_attrs of this PersistableModelSaveAllDTO.

        设置NULL值的属性名称。

        :return: The need_set_null_attrs of this PersistableModelSaveAllDTO.
        :rtype: list[str]
        """
        return self._need_set_null_attrs

    @need_set_null_attrs.setter
    def need_set_null_attrs(self, need_set_null_attrs):
        """Sets the need_set_null_attrs of this PersistableModelSaveAllDTO.

        设置NULL值的属性名称。

        :param need_set_null_attrs: The need_set_null_attrs of this PersistableModelSaveAllDTO.
        :type need_set_null_attrs: list[str]
        """
        self._need_set_null_attrs = need_set_null_attrs

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this PersistableModelSaveAllDTO.

        扩展类型。

        :return: The rdm_extension_type of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this PersistableModelSaveAllDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this PersistableModelSaveAllDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        """Gets the tenant of this PersistableModelSaveAllDTO.

        :return: The tenant of this PersistableModelSaveAllDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this PersistableModelSaveAllDTO.

        :param tenant: The tenant of this PersistableModelSaveAllDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._tenant = tenant

    @property
    def unique_key(self):
        """Gets the unique_key of this PersistableModelSaveAllDTO.

        示例模型的唯一键属性。

        :return: The unique_key of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        """Sets the unique_key of this PersistableModelSaveAllDTO.

        示例模型的唯一键属性。

        :param unique_key: The unique_key of this PersistableModelSaveAllDTO.
        :type unique_key: str
        """
        self._unique_key = unique_key

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
        if not isinstance(other, PersistableModelSaveAllDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
