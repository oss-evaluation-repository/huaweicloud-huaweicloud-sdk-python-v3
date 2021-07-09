# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class DeletePublicZoneResponse(SdkResponse):


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
        'description': 'str',
        'email': 'str',
        'zone_type': 'str',
        'ttl': 'int',
        'serial': 'int',
        'status': 'str',
        'record_num': 'int',
        'pool_id': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'masters': 'str',
        'links': 'list[PageLink]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'email': 'email',
        'zone_type': 'zone_type',
        'ttl': 'ttl',
        'serial': 'serial',
        'status': 'status',
        'record_num': 'record_num',
        'pool_id': 'pool_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'masters': 'masters',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, description=None, email=None, zone_type=None, ttl=None, serial=None, status=None, record_num=None, pool_id=None, project_id=None, created_at=None, updated_at=None, masters=None, links=None):
        """DeletePublicZoneResponse - a model defined in huaweicloud sdk"""
        
        super(DeletePublicZoneResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._email = None
        self._zone_type = None
        self._ttl = None
        self._serial = None
        self._status = None
        self._record_num = None
        self._pool_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._masters = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if email is not None:
            self.email = email
        if zone_type is not None:
            self.zone_type = zone_type
        if ttl is not None:
            self.ttl = ttl
        if serial is not None:
            self.serial = serial
        if status is not None:
            self.status = status
        if record_num is not None:
            self.record_num = record_num
        if pool_id is not None:
            self.pool_id = pool_id
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if masters is not None:
            self.masters = masters
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this DeletePublicZoneResponse.

        Zone的ID

        :return: The id of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeletePublicZoneResponse.

        Zone的ID

        :param id: The id of this DeletePublicZoneResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DeletePublicZoneResponse.

        zone名称

        :return: The name of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeletePublicZoneResponse.

        zone名称

        :param name: The name of this DeletePublicZoneResponse.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this DeletePublicZoneResponse.

        对zone的描述信息

        :return: The description of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeletePublicZoneResponse.

        对zone的描述信息

        :param description: The description of this DeletePublicZoneResponse.
        :type: str
        """
        self._description = description

    @property
    def email(self):
        """Gets the email of this DeletePublicZoneResponse.

        管理该zone的管理员邮箱

        :return: The email of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DeletePublicZoneResponse.

        管理该zone的管理员邮箱

        :param email: The email of this DeletePublicZoneResponse.
        :type: str
        """
        self._email = email

    @property
    def zone_type(self):
        """Gets the zone_type of this DeletePublicZoneResponse.

        zone类型，公网（public）或者内网（private）

        :return: The zone_type of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """Sets the zone_type of this DeletePublicZoneResponse.

        zone类型，公网（public）或者内网（private）

        :param zone_type: The zone_type of this DeletePublicZoneResponse.
        :type: str
        """
        self._zone_type = zone_type

    @property
    def ttl(self):
        """Gets the ttl of this DeletePublicZoneResponse.

        该zone下SOA记录中的ttl值

        :return: The ttl of this DeletePublicZoneResponse.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this DeletePublicZoneResponse.

        该zone下SOA记录中的ttl值

        :param ttl: The ttl of this DeletePublicZoneResponse.
        :type: int
        """
        self._ttl = ttl

    @property
    def serial(self):
        """Gets the serial of this DeletePublicZoneResponse.

        该zone下SOA记录中用于标识zone文件变更的序列值，用于主从节点同步

        :return: The serial of this DeletePublicZoneResponse.
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DeletePublicZoneResponse.

        该zone下SOA记录中用于标识zone文件变更的序列值，用于主从节点同步

        :param serial: The serial of this DeletePublicZoneResponse.
        :type: int
        """
        self._serial = serial

    @property
    def status(self):
        """Gets the status of this DeletePublicZoneResponse.

        该zone下的recordset个数

        :return: The status of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeletePublicZoneResponse.

        该zone下的recordset个数

        :param status: The status of this DeletePublicZoneResponse.
        :type: str
        """
        self._status = status

    @property
    def record_num(self):
        """Gets the record_num of this DeletePublicZoneResponse.

        该zone下的recordset个数

        :return: The record_num of this DeletePublicZoneResponse.
        :rtype: int
        """
        return self._record_num

    @record_num.setter
    def record_num(self, record_num):
        """Sets the record_num of this DeletePublicZoneResponse.

        该zone下的recordset个数

        :param record_num: The record_num of this DeletePublicZoneResponse.
        :type: int
        """
        self._record_num = record_num

    @property
    def pool_id(self):
        """Gets the pool_id of this DeletePublicZoneResponse.

        托管该zone的pool，由系统分配

        :return: The pool_id of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this DeletePublicZoneResponse.

        托管该zone的pool，由系统分配

        :param pool_id: The pool_id of this DeletePublicZoneResponse.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def project_id(self):
        """Gets the project_id of this DeletePublicZoneResponse.

        zone所属的项目ID

        :return: The project_id of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DeletePublicZoneResponse.

        zone所属的项目ID

        :param project_id: The project_id of this DeletePublicZoneResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this DeletePublicZoneResponse.

        创建时间

        :return: The created_at of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DeletePublicZoneResponse.

        创建时间

        :param created_at: The created_at of this DeletePublicZoneResponse.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DeletePublicZoneResponse.

        更新时间

        :return: The updated_at of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DeletePublicZoneResponse.

        更新时间

        :param updated_at: The updated_at of this DeletePublicZoneResponse.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def masters(self):
        """Gets the masters of this DeletePublicZoneResponse.

        主从模式中，从DNS服务器用以获取DNS信息

        :return: The masters of this DeletePublicZoneResponse.
        :rtype: str
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        """Sets the masters of this DeletePublicZoneResponse.

        主从模式中，从DNS服务器用以获取DNS信息

        :param masters: The masters of this DeletePublicZoneResponse.
        :type: str
        """
        self._masters = masters

    @property
    def links(self):
        """Gets the links of this DeletePublicZoneResponse.

        指向当前资源或者其他资源的链接。当查询需要分页时，需要包含一个next链接指向下一页

        :return: The links of this DeletePublicZoneResponse.
        :rtype: list[PageLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DeletePublicZoneResponse.

        指向当前资源或者其他资源的链接。当查询需要分页时，需要包含一个next链接指向下一页

        :param links: The links of this DeletePublicZoneResponse.
        :type: list[PageLink]
        """
        self._links = links

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
        if not isinstance(other, DeletePublicZoneResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
