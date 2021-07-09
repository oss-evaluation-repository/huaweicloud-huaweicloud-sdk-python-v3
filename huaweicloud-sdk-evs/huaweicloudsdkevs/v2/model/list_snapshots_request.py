# coding: utf-8

import re
import six





class ListSnapshotsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'status': 'str',
        'volume_id': 'str',
        'availability_zone': 'str',
        'id': 'str',
        'dedicated_storage_name': 'str',
        'dedicated_storage_id': 'str',
        'service_type': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'status': 'status',
        'volume_id': 'volume_id',
        'availability_zone': 'availability_zone',
        'id': 'id',
        'dedicated_storage_name': 'dedicated_storage_name',
        'dedicated_storage_id': 'dedicated_storage_id',
        'service_type': 'service_type',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, offset=None, limit=None, name=None, status=None, volume_id=None, availability_zone=None, id=None, dedicated_storage_name=None, dedicated_storage_id=None, service_type=None, enterprise_project_id=None):
        """ListSnapshotsRequest - a model defined in huaweicloud sdk"""
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._status = None
        self._volume_id = None
        self._availability_zone = None
        self._id = None
        self._dedicated_storage_name = None
        self._dedicated_storage_id = None
        self._service_type = None
        self._enterprise_project_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if volume_id is not None:
            self.volume_id = volume_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if id is not None:
            self.id = id
        if dedicated_storage_name is not None:
            self.dedicated_storage_name = dedicated_storage_name
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if service_type is not None:
            self.service_type = service_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListSnapshotsRequest.

        偏移量。 说明:分页查询快照时使用，与limit配合使用。假如共有30个快照，设置offset为11，limit为10，即为从第12个快照开始查询，一次最多可读取10个快照。

        :return: The offset of this ListSnapshotsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSnapshotsRequest.

        偏移量。 说明:分页查询快照时使用，与limit配合使用。假如共有30个快照，设置offset为11，limit为10，即为从第12个快照开始查询，一次最多可读取10个快照。

        :param offset: The offset of this ListSnapshotsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSnapshotsRequest.

        返回结果个数限制，值为大于0的整数。默认值为1000。

        :return: The limit of this ListSnapshotsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSnapshotsRequest.

        返回结果个数限制，值为大于0的整数。默认值为1000。

        :param limit: The limit of this ListSnapshotsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListSnapshotsRequest.

        云硬盘快照名称。最大支持255个字节。

        :return: The name of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListSnapshotsRequest.

        云硬盘快照名称。最大支持255个字节。

        :param name: The name of this ListSnapshotsRequest.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListSnapshotsRequest.

        云硬盘快照状态，具体请参见A.3 云硬盘快照状态。

        :return: The status of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSnapshotsRequest.

        云硬盘快照状态，具体请参见A.3 云硬盘快照状态。

        :param status: The status of this ListSnapshotsRequest.
        :type: str
        """
        self._status = status

    @property
    def volume_id(self):
        """Gets the volume_id of this ListSnapshotsRequest.

        快照所属云硬盘的ID。

        :return: The volume_id of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this ListSnapshotsRequest.

        快照所属云硬盘的ID。

        :param volume_id: The volume_id of this ListSnapshotsRequest.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListSnapshotsRequest.

        快照所属云硬盘的可用区。

        :return: The availability_zone of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListSnapshotsRequest.

        快照所属云硬盘的可用区。

        :param availability_zone: The availability_zone of this ListSnapshotsRequest.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def id(self):
        """Gets the id of this ListSnapshotsRequest.

        指定快照id进行过滤。

        :return: The id of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSnapshotsRequest.

        指定快照id进行过滤。

        :param id: The id of this ListSnapshotsRequest.
        :type: str
        """
        self._id = id

    @property
    def dedicated_storage_name(self):
        """Gets the dedicated_storage_name of this ListSnapshotsRequest.

        专属存储的名称。

        :return: The dedicated_storage_name of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._dedicated_storage_name

    @dedicated_storage_name.setter
    def dedicated_storage_name(self, dedicated_storage_name):
        """Sets the dedicated_storage_name of this ListSnapshotsRequest.

        专属存储的名称。

        :param dedicated_storage_name: The dedicated_storage_name of this ListSnapshotsRequest.
        :type: str
        """
        self._dedicated_storage_name = dedicated_storage_name

    @property
    def dedicated_storage_id(self):
        """Gets the dedicated_storage_id of this ListSnapshotsRequest.

        专属存储ID。

        :return: The dedicated_storage_id of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        """Sets the dedicated_storage_id of this ListSnapshotsRequest.

        专属存储ID。

        :param dedicated_storage_id: The dedicated_storage_id of this ListSnapshotsRequest.
        :type: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def service_type(self):
        """Gets the service_type of this ListSnapshotsRequest.

        服务类型。仅支持EVS、DSS、DESS。

        :return: The service_type of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ListSnapshotsRequest.

        服务类型。仅支持EVS、DSS、DESS。

        :param service_type: The service_type of this ListSnapshotsRequest.
        :type: str
        """
        self._service_type = service_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListSnapshotsRequest.

        指定企业项目id进行过滤。 传入“all_granted_eps”，代表查询权限范围内的所有企业项目下的云硬盘。 > 说明： >  > 关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\"。

        :return: The enterprise_project_id of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListSnapshotsRequest.

        指定企业项目id进行过滤。 传入“all_granted_eps”，代表查询权限范围内的所有企业项目下的云硬盘。 > 说明： >  > 关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\"。

        :param enterprise_project_id: The enterprise_project_id of this ListSnapshotsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListSnapshotsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
