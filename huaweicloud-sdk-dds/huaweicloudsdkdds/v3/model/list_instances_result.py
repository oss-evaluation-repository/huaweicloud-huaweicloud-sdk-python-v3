# coding: utf-8

import pprint
import re

import six


class ListInstancesResult(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'port': 'int',
        'mode': 'str',
        'region': 'str',
        'datastore': 'ListInstancesDatastoreResult',
        'engine': 'str',
        'created': 'str',
        'updated': 'str',
        'db_user_name': 'str',
        'ssl': 'int',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'backup_strategy': 'ListInstancesBackupStrategyResult',
        'pay_mode': 'str',
        'maintenance_window': 'str',
        'groups': 'list[ListInstancesGroupResult]',
        'storage': 'ListInstancesStorageResult',
        'disk_encryption_id': 'str',
        'enterprise_project_id': 'str',
        'time_zone': 'str',
        'actions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'port': 'port',
        'mode': 'mode',
        'region': 'region',
        'datastore': 'datastore',
        'engine': 'engine',
        'created': 'created',
        'updated': 'updated',
        'db_user_name': 'db_user_name',
        'ssl': 'ssl',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'backup_strategy': 'backup_strategy',
        'pay_mode': 'pay_mode',
        'maintenance_window': 'maintenance_window',
        'groups': 'groups',
        'storage': 'storage',
        'disk_encryption_id': 'disk_encryption_id',
        'enterprise_project_id': 'enterprise_project_id',
        'time_zone': 'time_zone',
        'actions': 'actions'
    }

    def __init__(self, id=None, name=None, status=None, port=None, mode=None, region=None, datastore=None, engine=None, created=None, updated=None, db_user_name=None, ssl=None, vpc_id=None, subnet_id=None, security_group_id=None, backup_strategy=None, pay_mode=None, maintenance_window=None, groups=None, storage=None, disk_encryption_id=None, enterprise_project_id=None, time_zone=None, actions=None):  # noqa: E501
        """ListInstancesResult - a model defined in huaweicloud sdk"""

        self._id = None
        self._name = None
        self._status = None
        self._port = None
        self._mode = None
        self._region = None
        self._datastore = None
        self._engine = None
        self._created = None
        self._updated = None
        self._db_user_name = None
        self._ssl = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._backup_strategy = None
        self._pay_mode = None
        self._maintenance_window = None
        self._groups = None
        self._storage = None
        self._disk_encryption_id = None
        self._enterprise_project_id = None
        self._time_zone = None
        self._actions = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.port = port
        self.mode = mode
        self.region = region
        self.datastore = datastore
        self.engine = engine
        self.created = created
        self.updated = updated
        self.db_user_name = db_user_name
        self.ssl = ssl
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.backup_strategy = backup_strategy
        if pay_mode is not None:
            self.pay_mode = pay_mode
        self.maintenance_window = maintenance_window
        self.groups = groups
        self.storage = storage
        self.disk_encryption_id = disk_encryption_id
        self.enterprise_project_id = enterprise_project_id
        self.time_zone = time_zone
        self.actions = actions

    @property
    def id(self):
        """Gets the id of this ListInstancesResult.

        实例ID。

        :return: The id of this ListInstancesResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInstancesResult.

        实例ID。

        :param id: The id of this ListInstancesResult.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListInstancesResult.

        实例名称。

        :return: The name of this ListInstancesResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesResult.

        实例名称。

        :param name: The name of this ListInstancesResult.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListInstancesResult.

        实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。

        :return: The status of this ListInstancesResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesResult.

        实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。

        :param status: The status of this ListInstancesResult.
        :type: str
        """
        self._status = status

    @property
    def port(self):
        """Gets the port of this ListInstancesResult.

        数据库端口号。文档数据库实例支持的端口号范围为2100～9500。

        :return: The port of this ListInstancesResult.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListInstancesResult.

        数据库端口号。文档数据库实例支持的端口号范围为2100～9500。

        :param port: The port of this ListInstancesResult.
        :type: int
        """
        self._port = port

    @property
    def mode(self):
        """Gets the mode of this ListInstancesResult.

        实例类型。与请求参数相同。

        :return: The mode of this ListInstancesResult.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ListInstancesResult.

        实例类型。与请求参数相同。

        :param mode: The mode of this ListInstancesResult.
        :type: str
        """
        self._mode = mode

    @property
    def region(self):
        """Gets the region of this ListInstancesResult.

        实例所在区域。

        :return: The region of this ListInstancesResult.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListInstancesResult.

        实例所在区域。

        :param region: The region of this ListInstancesResult.
        :type: str
        """
        self._region = region

    @property
    def datastore(self):
        """Gets the datastore of this ListInstancesResult.


        :return: The datastore of this ListInstancesResult.
        :rtype: ListInstancesDatastoreResult
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ListInstancesResult.


        :param datastore: The datastore of this ListInstancesResult.
        :type: ListInstancesDatastoreResult
        """
        self._datastore = datastore

    @property
    def engine(self):
        """Gets the engine of this ListInstancesResult.

        存储引擎。 - 对于社区版实例，取值为“wiredTiger”。 - 对于增强版实例，取值为“rocksDB”。

        :return: The engine of this ListInstancesResult.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListInstancesResult.

        存储引擎。 - 对于社区版实例，取值为“wiredTiger”。 - 对于增强版实例，取值为“rocksDB”。

        :param engine: The engine of this ListInstancesResult.
        :type: str
        """
        self._engine = engine

    @property
    def created(self):
        """Gets the created of this ListInstancesResult.

        实例创建时间。

        :return: The created of this ListInstancesResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ListInstancesResult.

        实例创建时间。

        :param created: The created of this ListInstancesResult.
        :type: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ListInstancesResult.

        实例操作最新变更的时间。

        :return: The updated of this ListInstancesResult.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ListInstancesResult.

        实例操作最新变更的时间。

        :param updated: The updated of this ListInstancesResult.
        :type: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        """Gets the db_user_name of this ListInstancesResult.

        默认用户名。取值为“rwuser”。

        :return: The db_user_name of this ListInstancesResult.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """Sets the db_user_name of this ListInstancesResult.

        默认用户名。取值为“rwuser”。

        :param db_user_name: The db_user_name of this ListInstancesResult.
        :type: str
        """
        self._db_user_name = db_user_name

    @property
    def ssl(self):
        """Gets the ssl of this ListInstancesResult.

        是否开启SSL安全连接。 - 取值为“1”，表示开启。 - 取值为“0”，表示不开启。

        :return: The ssl of this ListInstancesResult.
        :rtype: int
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this ListInstancesResult.

        是否开启SSL安全连接。 - 取值为“1”，表示开启。 - 取值为“0”，表示不开启。

        :param ssl: The ssl of this ListInstancesResult.
        :type: int
        """
        self._ssl = ssl

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListInstancesResult.

        虚拟私有云ID。

        :return: The vpc_id of this ListInstancesResult.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListInstancesResult.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListInstancesResult.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListInstancesResult.

        子网ID。

        :return: The subnet_id of this ListInstancesResult.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListInstancesResult.

        子网ID。

        :param subnet_id: The subnet_id of this ListInstancesResult.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ListInstancesResult.

        安全组ID。

        :return: The security_group_id of this ListInstancesResult.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ListInstancesResult.

        安全组ID。

        :param security_group_id: The security_group_id of this ListInstancesResult.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this ListInstancesResult.


        :return: The backup_strategy of this ListInstancesResult.
        :rtype: ListInstancesBackupStrategyResult
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this ListInstancesResult.


        :param backup_strategy: The backup_strategy of this ListInstancesResult.
        :type: ListInstancesBackupStrategyResult
        """
        self._backup_strategy = backup_strategy

    @property
    def pay_mode(self):
        """Gets the pay_mode of this ListInstancesResult.

        计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :return: The pay_mode of this ListInstancesResult.
        :rtype: str
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        """Sets the pay_mode of this ListInstancesResult.

        计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :param pay_mode: The pay_mode of this ListInstancesResult.
        :type: str
        """
        self._pay_mode = pay_mode

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this ListInstancesResult.

        系统可维护时间窗。

        :return: The maintenance_window of this ListInstancesResult.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this ListInstancesResult.

        系统可维护时间窗。

        :param maintenance_window: The maintenance_window of this ListInstancesResult.
        :type: str
        """
        self._maintenance_window = maintenance_window

    @property
    def groups(self):
        """Gets the groups of this ListInstancesResult.

        组信息。

        :return: The groups of this ListInstancesResult.
        :rtype: list[ListInstancesGroupResult]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ListInstancesResult.

        组信息。

        :param groups: The groups of this ListInstancesResult.
        :type: list[ListInstancesGroupResult]
        """
        self._groups = groups

    @property
    def storage(self):
        """Gets the storage of this ListInstancesResult.


        :return: The storage of this ListInstancesResult.
        :rtype: ListInstancesStorageResult
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this ListInstancesResult.


        :param storage: The storage of this ListInstancesResult.
        :type: ListInstancesStorageResult
        """
        self._storage = storage

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this ListInstancesResult.

        磁盘加密的密钥ID。

        :return: The disk_encryption_id of this ListInstancesResult.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this ListInstancesResult.

        磁盘加密的密钥ID。

        :param disk_encryption_id: The disk_encryption_id of this ListInstancesResult.
        :type: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListInstancesResult.

        企业项目ID。取值为“0”，表示为default企业项目。

        :return: The enterprise_project_id of this ListInstancesResult.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListInstancesResult.

        企业项目ID。取值为“0”，表示为default企业项目。

        :param enterprise_project_id: The enterprise_project_id of this ListInstancesResult.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def time_zone(self):
        """Gets the time_zone of this ListInstancesResult.

        时区。

        :return: The time_zone of this ListInstancesResult.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ListInstancesResult.

        时区。

        :param time_zone: The time_zone of this ListInstancesResult.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def actions(self):
        """Gets the actions of this ListInstancesResult.

        实例正在执行的动作。

        :return: The actions of this ListInstancesResult.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ListInstancesResult.

        实例正在执行的动作。

        :param actions: The actions of this ListInstancesResult.
        :type: list[str]
        """
        self._actions = actions

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
        if not isinstance(other, ListInstancesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
