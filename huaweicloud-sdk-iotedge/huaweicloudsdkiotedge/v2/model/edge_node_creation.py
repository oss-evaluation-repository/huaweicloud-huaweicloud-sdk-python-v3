# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeNodeCreation:

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
        'type': 'str',
        'instance_id': 'str',
        'space_id': 'str',
        'resource_ids': 'list[str]',
        'security_level': 'str',
        'storage_period': 'int',
        'ai_card_type': 'str',
        'log_configs': 'list[LogConfigDTO]',
        'apps': 'list[EdgeAppInstanceDTO]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'instance_id': 'instance_id',
        'space_id': 'space_id',
        'resource_ids': 'resource_ids',
        'security_level': 'security_level',
        'storage_period': 'storage_period',
        'ai_card_type': 'ai_card_type',
        'log_configs': 'log_configs',
        'apps': 'apps'
    }

    def __init__(self, name=None, type=None, instance_id=None, space_id=None, resource_ids=None, security_level=None, storage_period=None, ai_card_type=None, log_configs=None, apps=None):
        """EdgeNodeCreation

        The model defined in huaweicloud sdk

        :param name: 边缘节点名称，只允许中、数字、英文大小写、中划线、下划线
        :type name: str
        :param type: 节点所属资源类型：advanced|standard
        :type type: str
        :param instance_id: 实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param space_id: 资源空间id，对应IOTDA云服务接口参数中的app_id。
        :type space_id: str
        :param resource_ids: 资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。
        :type resource_ids: list[str]
        :param security_level: 节点的安全等级，MEDIUM边缘节数据上报不进行加密，HIGH对数据上报进行加密。
        :type security_level: str
        :param storage_period: 节点的存储周期，默认0天，取值范围0~7天，0天则不存储。
        :type storage_period: int
        :param ai_card_type: 华为AI加速卡类型，如NPU、GPU
        :type ai_card_type: str
        :param log_configs: 边缘节点在IEF日志配置参数
        :type log_configs: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        :param apps: 用户预置第三方边缘应用
        :type apps: list[:class:`huaweicloudsdkiotedge.v2.EdgeAppInstanceDTO`]
        """
        
        

        self._name = None
        self._type = None
        self._instance_id = None
        self._space_id = None
        self._resource_ids = None
        self._security_level = None
        self._storage_period = None
        self._ai_card_type = None
        self._log_configs = None
        self._apps = None
        self.discriminator = None

        self.name = name
        self.type = type
        if instance_id is not None:
            self.instance_id = instance_id
        if space_id is not None:
            self.space_id = space_id
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if security_level is not None:
            self.security_level = security_level
        if storage_period is not None:
            self.storage_period = storage_period
        if ai_card_type is not None:
            self.ai_card_type = ai_card_type
        if log_configs is not None:
            self.log_configs = log_configs
        if apps is not None:
            self.apps = apps

    @property
    def name(self):
        """Gets the name of this EdgeNodeCreation.

        边缘节点名称，只允许中、数字、英文大小写、中划线、下划线

        :return: The name of this EdgeNodeCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeNodeCreation.

        边缘节点名称，只允许中、数字、英文大小写、中划线、下划线

        :param name: The name of this EdgeNodeCreation.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this EdgeNodeCreation.

        节点所属资源类型：advanced|standard

        :return: The type of this EdgeNodeCreation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EdgeNodeCreation.

        节点所属资源类型：advanced|standard

        :param type: The type of this EdgeNodeCreation.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        """Gets the instance_id of this EdgeNodeCreation.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this EdgeNodeCreation.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this EdgeNodeCreation.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this EdgeNodeCreation.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def space_id(self):
        """Gets the space_id of this EdgeNodeCreation.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :return: The space_id of this EdgeNodeCreation.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this EdgeNodeCreation.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :param space_id: The space_id of this EdgeNodeCreation.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def resource_ids(self):
        """Gets the resource_ids of this EdgeNodeCreation.

        资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。

        :return: The resource_ids of this EdgeNodeCreation.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this EdgeNodeCreation.

        资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。

        :param resource_ids: The resource_ids of this EdgeNodeCreation.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def security_level(self):
        """Gets the security_level of this EdgeNodeCreation.

        节点的安全等级，MEDIUM边缘节数据上报不进行加密，HIGH对数据上报进行加密。

        :return: The security_level of this EdgeNodeCreation.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this EdgeNodeCreation.

        节点的安全等级，MEDIUM边缘节数据上报不进行加密，HIGH对数据上报进行加密。

        :param security_level: The security_level of this EdgeNodeCreation.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def storage_period(self):
        """Gets the storage_period of this EdgeNodeCreation.

        节点的存储周期，默认0天，取值范围0~7天，0天则不存储。

        :return: The storage_period of this EdgeNodeCreation.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        """Sets the storage_period of this EdgeNodeCreation.

        节点的存储周期，默认0天，取值范围0~7天，0天则不存储。

        :param storage_period: The storage_period of this EdgeNodeCreation.
        :type storage_period: int
        """
        self._storage_period = storage_period

    @property
    def ai_card_type(self):
        """Gets the ai_card_type of this EdgeNodeCreation.

        华为AI加速卡类型，如NPU、GPU

        :return: The ai_card_type of this EdgeNodeCreation.
        :rtype: str
        """
        return self._ai_card_type

    @ai_card_type.setter
    def ai_card_type(self, ai_card_type):
        """Sets the ai_card_type of this EdgeNodeCreation.

        华为AI加速卡类型，如NPU、GPU

        :param ai_card_type: The ai_card_type of this EdgeNodeCreation.
        :type ai_card_type: str
        """
        self._ai_card_type = ai_card_type

    @property
    def log_configs(self):
        """Gets the log_configs of this EdgeNodeCreation.

        边缘节点在IEF日志配置参数

        :return: The log_configs of this EdgeNodeCreation.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        """Sets the log_configs of this EdgeNodeCreation.

        边缘节点在IEF日志配置参数

        :param log_configs: The log_configs of this EdgeNodeCreation.
        :type log_configs: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        """
        self._log_configs = log_configs

    @property
    def apps(self):
        """Gets the apps of this EdgeNodeCreation.

        用户预置第三方边缘应用

        :return: The apps of this EdgeNodeCreation.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.EdgeAppInstanceDTO`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this EdgeNodeCreation.

        用户预置第三方边缘应用

        :param apps: The apps of this EdgeNodeCreation.
        :type apps: list[:class:`huaweicloudsdkiotedge.v2.EdgeAppInstanceDTO`]
        """
        self._apps = apps

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
        if not isinstance(other, EdgeNodeCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
