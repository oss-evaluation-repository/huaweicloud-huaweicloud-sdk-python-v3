# coding: utf-8

import pprint
import re

import six


class ScalingActivityLogV2(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'status': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'id': 'str',
        'instance_removed_list': 'list[ScalingInstance]',
        'instance_deleted_list': 'list[ScalingInstance]',
        'instance_added_list': 'list[ScalingInstance]',
        'instance_failed_list': 'list[ScalingInstance]',
        'instance_standby_list': 'list[ScalingInstance]',
        'scaling_value': 'str',
        'description': 'str',
        'instance_value': 'int',
        'desire_value': 'int',
        'lb_bind_success_list': 'list[ModifyLb]',
        'lb_bind_failed_list': 'list[ModifyLb]',
        'lb_unbind_success_list': 'list[ModifyLb]',
        'lb_unbind_failed_list': 'list[ModifyLb]'
    }

    attribute_map = {
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'id': 'id',
        'instance_removed_list': 'instance_removed_list',
        'instance_deleted_list': 'instance_deleted_list',
        'instance_added_list': 'instance_added_list',
        'instance_failed_list': 'instance_failed_list',
        'instance_standby_list': 'instance_standby_list',
        'scaling_value': 'scaling_value',
        'description': 'description',
        'instance_value': 'instance_value',
        'desire_value': 'desire_value',
        'lb_bind_success_list': 'lb_bind_success_list',
        'lb_bind_failed_list': 'lb_bind_failed_list',
        'lb_unbind_success_list': 'lb_unbind_success_list',
        'lb_unbind_failed_list': 'lb_unbind_failed_list'
    }

    def __init__(self, status=None, start_time=None, end_time=None, id=None, instance_removed_list=None, instance_deleted_list=None, instance_added_list=None, instance_failed_list=None, instance_standby_list=None, scaling_value=None, description=None, instance_value=None, desire_value=None, lb_bind_success_list=None, lb_bind_failed_list=None, lb_unbind_success_list=None, lb_unbind_failed_list=None):  # noqa: E501
        """ScalingActivityLogV2 - a model defined in huaweicloud sdk"""

        self._status = None
        self._start_time = None
        self._end_time = None
        self._id = None
        self._instance_removed_list = None
        self._instance_deleted_list = None
        self._instance_added_list = None
        self._instance_failed_list = None
        self._instance_standby_list = None
        self._scaling_value = None
        self._description = None
        self._instance_value = None
        self._desire_value = None
        self._lb_bind_success_list = None
        self._lb_bind_failed_list = None
        self._lb_unbind_success_list = None
        self._lb_unbind_failed_list = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if id is not None:
            self.id = id
        if instance_removed_list is not None:
            self.instance_removed_list = instance_removed_list
        if instance_deleted_list is not None:
            self.instance_deleted_list = instance_deleted_list
        if instance_added_list is not None:
            self.instance_added_list = instance_added_list
        if instance_failed_list is not None:
            self.instance_failed_list = instance_failed_list
        if instance_standby_list is not None:
            self.instance_standby_list = instance_standby_list
        if scaling_value is not None:
            self.scaling_value = scaling_value
        if description is not None:
            self.description = description
        if instance_value is not None:
            self.instance_value = instance_value
        if desire_value is not None:
            self.desire_value = desire_value
        if lb_bind_success_list is not None:
            self.lb_bind_success_list = lb_bind_success_list
        if lb_bind_failed_list is not None:
            self.lb_bind_failed_list = lb_bind_failed_list
        if lb_unbind_success_list is not None:
            self.lb_unbind_success_list = lb_unbind_success_list
        if lb_unbind_failed_list is not None:
            self.lb_unbind_failed_list = lb_unbind_failed_list

    @property
    def status(self):
        """Gets the status of this ScalingActivityLogV2.

        伸缩活动状态：SUCCESS：成功。FAIL：失败。DOING：伸缩过程中。

        :return: The status of this ScalingActivityLogV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScalingActivityLogV2.

        伸缩活动状态：SUCCESS：成功。FAIL：失败。DOING：伸缩过程中。

        :param status: The status of this ScalingActivityLogV2.
        :type: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ScalingActivityLogV2.

        伸缩活动触发时间，遵循UTC时间。

        :return: The start_time of this ScalingActivityLogV2.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScalingActivityLogV2.

        伸缩活动触发时间，遵循UTC时间。

        :param start_time: The start_time of this ScalingActivityLogV2.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScalingActivityLogV2.

        伸缩活动结束时间，遵循UTC时间。

        :return: The end_time of this ScalingActivityLogV2.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScalingActivityLogV2.

        伸缩活动结束时间，遵循UTC时间。

        :param end_time: The end_time of this ScalingActivityLogV2.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def id(self):
        """Gets the id of this ScalingActivityLogV2.

        伸缩活动日志ID。

        :return: The id of this ScalingActivityLogV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScalingActivityLogV2.

        伸缩活动日志ID。

        :param id: The id of this ScalingActivityLogV2.
        :type: str
        """
        self._id = id

    @property
    def instance_removed_list(self):
        """Gets the instance_removed_list of this ScalingActivityLogV2.

        完成伸缩活动且只被移出弹性伸缩组的云服务器名称列表，云服务信息之间以逗号分隔。

        :return: The instance_removed_list of this ScalingActivityLogV2.
        :rtype: list[ScalingInstance]
        """
        return self._instance_removed_list

    @instance_removed_list.setter
    def instance_removed_list(self, instance_removed_list):
        """Sets the instance_removed_list of this ScalingActivityLogV2.

        完成伸缩活动且只被移出弹性伸缩组的云服务器名称列表，云服务信息之间以逗号分隔。

        :param instance_removed_list: The instance_removed_list of this ScalingActivityLogV2.
        :type: list[ScalingInstance]
        """
        self._instance_removed_list = instance_removed_list

    @property
    def instance_deleted_list(self):
        """Gets the instance_deleted_list of this ScalingActivityLogV2.

        完成伸缩活动且被移出弹性伸缩组并删除的云服务器名称列表，云服务器信息之间以逗号分隔。

        :return: The instance_deleted_list of this ScalingActivityLogV2.
        :rtype: list[ScalingInstance]
        """
        return self._instance_deleted_list

    @instance_deleted_list.setter
    def instance_deleted_list(self, instance_deleted_list):
        """Sets the instance_deleted_list of this ScalingActivityLogV2.

        完成伸缩活动且被移出弹性伸缩组并删除的云服务器名称列表，云服务器信息之间以逗号分隔。

        :param instance_deleted_list: The instance_deleted_list of this ScalingActivityLogV2.
        :type: list[ScalingInstance]
        """
        self._instance_deleted_list = instance_deleted_list

    @property
    def instance_added_list(self):
        """Gets the instance_added_list of this ScalingActivityLogV2.

        完成伸缩活动且被加入弹性伸缩组的云服务器名称列表，云服务器信息之间以逗号分割。

        :return: The instance_added_list of this ScalingActivityLogV2.
        :rtype: list[ScalingInstance]
        """
        return self._instance_added_list

    @instance_added_list.setter
    def instance_added_list(self, instance_added_list):
        """Sets the instance_added_list of this ScalingActivityLogV2.

        完成伸缩活动且被加入弹性伸缩组的云服务器名称列表，云服务器信息之间以逗号分割。

        :param instance_added_list: The instance_added_list of this ScalingActivityLogV2.
        :type: list[ScalingInstance]
        """
        self._instance_added_list = instance_added_list

    @property
    def instance_failed_list(self):
        """Gets the instance_failed_list of this ScalingActivityLogV2.

        弹性伸缩组中伸缩活动失败的云服务器列表。

        :return: The instance_failed_list of this ScalingActivityLogV2.
        :rtype: list[ScalingInstance]
        """
        return self._instance_failed_list

    @instance_failed_list.setter
    def instance_failed_list(self, instance_failed_list):
        """Sets the instance_failed_list of this ScalingActivityLogV2.

        弹性伸缩组中伸缩活动失败的云服务器列表。

        :param instance_failed_list: The instance_failed_list of this ScalingActivityLogV2.
        :type: list[ScalingInstance]
        """
        self._instance_failed_list = instance_failed_list

    @property
    def instance_standby_list(self):
        """Gets the instance_standby_list of this ScalingActivityLogV2.

        完成伸缩活动且被转入/移出备用状态的云服务器列表

        :return: The instance_standby_list of this ScalingActivityLogV2.
        :rtype: list[ScalingInstance]
        """
        return self._instance_standby_list

    @instance_standby_list.setter
    def instance_standby_list(self, instance_standby_list):
        """Sets the instance_standby_list of this ScalingActivityLogV2.

        完成伸缩活动且被转入/移出备用状态的云服务器列表

        :param instance_standby_list: The instance_standby_list of this ScalingActivityLogV2.
        :type: list[ScalingInstance]
        """
        self._instance_standby_list = instance_standby_list

    @property
    def scaling_value(self):
        """Gets the scaling_value of this ScalingActivityLogV2.

        伸缩活动中变化（增加或减少）的云服务器数量。

        :return: The scaling_value of this ScalingActivityLogV2.
        :rtype: str
        """
        return self._scaling_value

    @scaling_value.setter
    def scaling_value(self, scaling_value):
        """Sets the scaling_value of this ScalingActivityLogV2.

        伸缩活动中变化（增加或减少）的云服务器数量。

        :param scaling_value: The scaling_value of this ScalingActivityLogV2.
        :type: str
        """
        self._scaling_value = scaling_value

    @property
    def description(self):
        """Gets the description of this ScalingActivityLogV2.

        伸缩活动的描述信息。

        :return: The description of this ScalingActivityLogV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScalingActivityLogV2.

        伸缩活动的描述信息。

        :param description: The description of this ScalingActivityLogV2.
        :type: str
        """
        self._description = description

    @property
    def instance_value(self):
        """Gets the instance_value of this ScalingActivityLogV2.

        伸缩组当前instance值。

        :return: The instance_value of this ScalingActivityLogV2.
        :rtype: int
        """
        return self._instance_value

    @instance_value.setter
    def instance_value(self, instance_value):
        """Sets the instance_value of this ScalingActivityLogV2.

        伸缩组当前instance值。

        :param instance_value: The instance_value of this ScalingActivityLogV2.
        :type: int
        """
        self._instance_value = instance_value

    @property
    def desire_value(self):
        """Gets the desire_value of this ScalingActivityLogV2.

        伸缩活动最终desire值。

        :return: The desire_value of this ScalingActivityLogV2.
        :rtype: int
        """
        return self._desire_value

    @desire_value.setter
    def desire_value(self, desire_value):
        """Sets the desire_value of this ScalingActivityLogV2.

        伸缩活动最终desire值。

        :param desire_value: The desire_value of this ScalingActivityLogV2.
        :type: int
        """
        self._desire_value = desire_value

    @property
    def lb_bind_success_list(self):
        """Gets the lb_bind_success_list of this ScalingActivityLogV2.

        绑定成功的负载均衡器列表。

        :return: The lb_bind_success_list of this ScalingActivityLogV2.
        :rtype: list[ModifyLb]
        """
        return self._lb_bind_success_list

    @lb_bind_success_list.setter
    def lb_bind_success_list(self, lb_bind_success_list):
        """Sets the lb_bind_success_list of this ScalingActivityLogV2.

        绑定成功的负载均衡器列表。

        :param lb_bind_success_list: The lb_bind_success_list of this ScalingActivityLogV2.
        :type: list[ModifyLb]
        """
        self._lb_bind_success_list = lb_bind_success_list

    @property
    def lb_bind_failed_list(self):
        """Gets the lb_bind_failed_list of this ScalingActivityLogV2.

        绑定失败的负载均衡器列表。

        :return: The lb_bind_failed_list of this ScalingActivityLogV2.
        :rtype: list[ModifyLb]
        """
        return self._lb_bind_failed_list

    @lb_bind_failed_list.setter
    def lb_bind_failed_list(self, lb_bind_failed_list):
        """Sets the lb_bind_failed_list of this ScalingActivityLogV2.

        绑定失败的负载均衡器列表。

        :param lb_bind_failed_list: The lb_bind_failed_list of this ScalingActivityLogV2.
        :type: list[ModifyLb]
        """
        self._lb_bind_failed_list = lb_bind_failed_list

    @property
    def lb_unbind_success_list(self):
        """Gets the lb_unbind_success_list of this ScalingActivityLogV2.

        解绑成功的负载均衡器列表。

        :return: The lb_unbind_success_list of this ScalingActivityLogV2.
        :rtype: list[ModifyLb]
        """
        return self._lb_unbind_success_list

    @lb_unbind_success_list.setter
    def lb_unbind_success_list(self, lb_unbind_success_list):
        """Sets the lb_unbind_success_list of this ScalingActivityLogV2.

        解绑成功的负载均衡器列表。

        :param lb_unbind_success_list: The lb_unbind_success_list of this ScalingActivityLogV2.
        :type: list[ModifyLb]
        """
        self._lb_unbind_success_list = lb_unbind_success_list

    @property
    def lb_unbind_failed_list(self):
        """Gets the lb_unbind_failed_list of this ScalingActivityLogV2.

        解绑失败的负载均衡器列表。

        :return: The lb_unbind_failed_list of this ScalingActivityLogV2.
        :rtype: list[ModifyLb]
        """
        return self._lb_unbind_failed_list

    @lb_unbind_failed_list.setter
    def lb_unbind_failed_list(self, lb_unbind_failed_list):
        """Sets the lb_unbind_failed_list of this ScalingActivityLogV2.

        解绑失败的负载均衡器列表。

        :param lb_unbind_failed_list: The lb_unbind_failed_list of this ScalingActivityLogV2.
        :type: list[ModifyLb]
        """
        self._lb_unbind_failed_list = lb_unbind_failed_list

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
        if not isinstance(other, ScalingActivityLogV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
