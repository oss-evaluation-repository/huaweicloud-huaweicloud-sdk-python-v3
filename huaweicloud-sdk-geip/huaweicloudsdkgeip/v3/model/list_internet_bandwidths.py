# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternetBandwidths:

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
        'isp': 'str',
        'ingress_size': 'int',
        'access_site': 'str',
        'size': 'int',
        'description': 'str',
        'charge_mode': 'str',
        'ratio_95peak': 'int',
        'billing_info': 'str',
        'freezen_info': 'str',
        'domain_id': 'str',
        'status': 'str',
        'geip_count': 'int',
        'geip_segment_count': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'is_pre_paid': 'bool',
        'tags': 'list[Tag]',
        'sys_tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'type': 'str',
        'lock_infos': 'list[LockInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'isp': 'isp',
        'ingress_size': 'ingress_size',
        'access_site': 'access_site',
        'size': 'size',
        'description': 'description',
        'charge_mode': 'charge_mode',
        'ratio_95peak': 'ratio_95peak',
        'billing_info': 'billing_info',
        'freezen_info': 'freezen_info',
        'domain_id': 'domain_id',
        'status': 'status',
        'geip_count': 'geip_count',
        'geip_segment_count': 'geip_segment_count',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'is_pre_paid': 'is_pre_paid',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'lock_infos': 'lock_infos'
    }

    def __init__(self, id=None, name=None, isp=None, ingress_size=None, access_site=None, size=None, description=None, charge_mode=None, ratio_95peak=None, billing_info=None, freezen_info=None, domain_id=None, status=None, geip_count=None, geip_segment_count=None, created_at=None, updated_at=None, is_pre_paid=None, tags=None, sys_tags=None, enterprise_project_id=None, type=None, lock_infos=None):
        """ListInternetBandwidths

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param name: 资源名称
        :type name: str
        :param isp: 线路
        :type isp: str
        :param ingress_size: 全域公网带宽大小（入云方向）
        :type ingress_size: int
        :param access_site: 接入点信息
        :type access_site: str
        :param size: 全域公网带宽大小（出云方向）
        :type size: int
        :param description: 用户自定义的资源描述
        :type description: str
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param ratio_95peak: 增强95保底率
        :type ratio_95peak: int
        :param billing_info: 订单信息
        :type billing_info: str
        :param freezen_info: 冻结原因
        :type freezen_info: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param status: 状态
        :type status: str
        :param geip_count: 全域弹性公网IP个数
        :type geip_count: int
        :param geip_segment_count: 全域弹性公网IP段个数
        :type geip_segment_count: int
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param is_pre_paid: 是否包周期
        :type is_pre_paid: bool
        :param tags: 全域公网带宽标签
        :type tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        :param sys_tags: 系统标签
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        :param enterprise_project_id: 资源的企业项目id
        :type enterprise_project_id: str
        :param type: 全域公网带宽类型
        :type type: str
        :param lock_infos: 全域公网带宽资源的锁状态
        :type lock_infos: list[:class:`huaweicloudsdkgeip.v3.LockInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._isp = None
        self._ingress_size = None
        self._access_site = None
        self._size = None
        self._description = None
        self._charge_mode = None
        self._ratio_95peak = None
        self._billing_info = None
        self._freezen_info = None
        self._domain_id = None
        self._status = None
        self._geip_count = None
        self._geip_segment_count = None
        self._created_at = None
        self._updated_at = None
        self._is_pre_paid = None
        self._tags = None
        self._sys_tags = None
        self._enterprise_project_id = None
        self._type = None
        self._lock_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if isp is not None:
            self.isp = isp
        if ingress_size is not None:
            self.ingress_size = ingress_size
        if access_site is not None:
            self.access_site = access_site
        if size is not None:
            self.size = size
        if description is not None:
            self.description = description
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if ratio_95peak is not None:
            self.ratio_95peak = ratio_95peak
        if billing_info is not None:
            self.billing_info = billing_info
        if freezen_info is not None:
            self.freezen_info = freezen_info
        if domain_id is not None:
            self.domain_id = domain_id
        if status is not None:
            self.status = status
        if geip_count is not None:
            self.geip_count = geip_count
        if geip_segment_count is not None:
            self.geip_segment_count = geip_segment_count
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if is_pre_paid is not None:
            self.is_pre_paid = is_pre_paid
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if lock_infos is not None:
            self.lock_infos = lock_infos

    @property
    def id(self):
        """Gets the id of this ListInternetBandwidths.

        ID

        :return: The id of this ListInternetBandwidths.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInternetBandwidths.

        ID

        :param id: The id of this ListInternetBandwidths.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListInternetBandwidths.

        资源名称

        :return: The name of this ListInternetBandwidths.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInternetBandwidths.

        资源名称

        :param name: The name of this ListInternetBandwidths.
        :type name: str
        """
        self._name = name

    @property
    def isp(self):
        """Gets the isp of this ListInternetBandwidths.

        线路

        :return: The isp of this ListInternetBandwidths.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListInternetBandwidths.

        线路

        :param isp: The isp of this ListInternetBandwidths.
        :type isp: str
        """
        self._isp = isp

    @property
    def ingress_size(self):
        """Gets the ingress_size of this ListInternetBandwidths.

        全域公网带宽大小（入云方向）

        :return: The ingress_size of this ListInternetBandwidths.
        :rtype: int
        """
        return self._ingress_size

    @ingress_size.setter
    def ingress_size(self, ingress_size):
        """Sets the ingress_size of this ListInternetBandwidths.

        全域公网带宽大小（入云方向）

        :param ingress_size: The ingress_size of this ListInternetBandwidths.
        :type ingress_size: int
        """
        self._ingress_size = ingress_size

    @property
    def access_site(self):
        """Gets the access_site of this ListInternetBandwidths.

        接入点信息

        :return: The access_site of this ListInternetBandwidths.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this ListInternetBandwidths.

        接入点信息

        :param access_site: The access_site of this ListInternetBandwidths.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def size(self):
        """Gets the size of this ListInternetBandwidths.

        全域公网带宽大小（出云方向）

        :return: The size of this ListInternetBandwidths.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListInternetBandwidths.

        全域公网带宽大小（出云方向）

        :param size: The size of this ListInternetBandwidths.
        :type size: int
        """
        self._size = size

    @property
    def description(self):
        """Gets the description of this ListInternetBandwidths.

        用户自定义的资源描述

        :return: The description of this ListInternetBandwidths.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListInternetBandwidths.

        用户自定义的资源描述

        :param description: The description of this ListInternetBandwidths.
        :type description: str
        """
        self._description = description

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListInternetBandwidths.

        计费模式

        :return: The charge_mode of this ListInternetBandwidths.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListInternetBandwidths.

        计费模式

        :param charge_mode: The charge_mode of this ListInternetBandwidths.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def ratio_95peak(self):
        """Gets the ratio_95peak of this ListInternetBandwidths.

        增强95保底率

        :return: The ratio_95peak of this ListInternetBandwidths.
        :rtype: int
        """
        return self._ratio_95peak

    @ratio_95peak.setter
    def ratio_95peak(self, ratio_95peak):
        """Sets the ratio_95peak of this ListInternetBandwidths.

        增强95保底率

        :param ratio_95peak: The ratio_95peak of this ListInternetBandwidths.
        :type ratio_95peak: int
        """
        self._ratio_95peak = ratio_95peak

    @property
    def billing_info(self):
        """Gets the billing_info of this ListInternetBandwidths.

        订单信息

        :return: The billing_info of this ListInternetBandwidths.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this ListInternetBandwidths.

        订单信息

        :param billing_info: The billing_info of this ListInternetBandwidths.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def freezen_info(self):
        """Gets the freezen_info of this ListInternetBandwidths.

        冻结原因

        :return: The freezen_info of this ListInternetBandwidths.
        :rtype: str
        """
        return self._freezen_info

    @freezen_info.setter
    def freezen_info(self, freezen_info):
        """Sets the freezen_info of this ListInternetBandwidths.

        冻结原因

        :param freezen_info: The freezen_info of this ListInternetBandwidths.
        :type freezen_info: str
        """
        self._freezen_info = freezen_info

    @property
    def domain_id(self):
        """Gets the domain_id of this ListInternetBandwidths.

        租户ID

        :return: The domain_id of this ListInternetBandwidths.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListInternetBandwidths.

        租户ID

        :param domain_id: The domain_id of this ListInternetBandwidths.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def status(self):
        """Gets the status of this ListInternetBandwidths.

        状态

        :return: The status of this ListInternetBandwidths.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInternetBandwidths.

        状态

        :param status: The status of this ListInternetBandwidths.
        :type status: str
        """
        self._status = status

    @property
    def geip_count(self):
        """Gets the geip_count of this ListInternetBandwidths.

        全域弹性公网IP个数

        :return: The geip_count of this ListInternetBandwidths.
        :rtype: int
        """
        return self._geip_count

    @geip_count.setter
    def geip_count(self, geip_count):
        """Sets the geip_count of this ListInternetBandwidths.

        全域弹性公网IP个数

        :param geip_count: The geip_count of this ListInternetBandwidths.
        :type geip_count: int
        """
        self._geip_count = geip_count

    @property
    def geip_segment_count(self):
        """Gets the geip_segment_count of this ListInternetBandwidths.

        全域弹性公网IP段个数

        :return: The geip_segment_count of this ListInternetBandwidths.
        :rtype: int
        """
        return self._geip_segment_count

    @geip_segment_count.setter
    def geip_segment_count(self, geip_segment_count):
        """Sets the geip_segment_count of this ListInternetBandwidths.

        全域弹性公网IP段个数

        :param geip_segment_count: The geip_segment_count of this ListInternetBandwidths.
        :type geip_segment_count: int
        """
        self._geip_segment_count = geip_segment_count

    @property
    def created_at(self):
        """Gets the created_at of this ListInternetBandwidths.

        创建时间

        :return: The created_at of this ListInternetBandwidths.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListInternetBandwidths.

        创建时间

        :param created_at: The created_at of this ListInternetBandwidths.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListInternetBandwidths.

        更新时间

        :return: The updated_at of this ListInternetBandwidths.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListInternetBandwidths.

        更新时间

        :param updated_at: The updated_at of this ListInternetBandwidths.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def is_pre_paid(self):
        """Gets the is_pre_paid of this ListInternetBandwidths.

        是否包周期

        :return: The is_pre_paid of this ListInternetBandwidths.
        :rtype: bool
        """
        return self._is_pre_paid

    @is_pre_paid.setter
    def is_pre_paid(self, is_pre_paid):
        """Sets the is_pre_paid of this ListInternetBandwidths.

        是否包周期

        :param is_pre_paid: The is_pre_paid of this ListInternetBandwidths.
        :type is_pre_paid: bool
        """
        self._is_pre_paid = is_pre_paid

    @property
    def tags(self):
        """Gets the tags of this ListInternetBandwidths.

        全域公网带宽标签

        :return: The tags of this ListInternetBandwidths.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListInternetBandwidths.

        全域公网带宽标签

        :param tags: The tags of this ListInternetBandwidths.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ListInternetBandwidths.

        系统标签

        :return: The sys_tags of this ListInternetBandwidths.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ListInternetBandwidths.

        系统标签

        :param sys_tags: The sys_tags of this ListInternetBandwidths.
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        self._sys_tags = sys_tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListInternetBandwidths.

        资源的企业项目id

        :return: The enterprise_project_id of this ListInternetBandwidths.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListInternetBandwidths.

        资源的企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListInternetBandwidths.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this ListInternetBandwidths.

        全域公网带宽类型

        :return: The type of this ListInternetBandwidths.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInternetBandwidths.

        全域公网带宽类型

        :param type: The type of this ListInternetBandwidths.
        :type type: str
        """
        self._type = type

    @property
    def lock_infos(self):
        """Gets the lock_infos of this ListInternetBandwidths.

        全域公网带宽资源的锁状态

        :return: The lock_infos of this ListInternetBandwidths.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.LockInfo`]
        """
        return self._lock_infos

    @lock_infos.setter
    def lock_infos(self, lock_infos):
        """Sets the lock_infos of this ListInternetBandwidths.

        全域公网带宽资源的锁状态

        :param lock_infos: The lock_infos of this ListInternetBandwidths.
        :type lock_infos: list[:class:`huaweicloudsdkgeip.v3.LockInfo`]
        """
        self._lock_infos = lock_infos

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
        if not isinstance(other, ListInternetBandwidths):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other