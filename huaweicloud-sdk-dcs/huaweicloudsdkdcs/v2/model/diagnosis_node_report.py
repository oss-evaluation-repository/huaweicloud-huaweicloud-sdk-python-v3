# coding: utf-8

import re
import six





class DiagnosisNodeReport:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_ip': 'str',
        'az_code': 'str',
        'group_name': 'str',
        'abnormal_sum': 'int',
        'failed_sum': 'int',
        'role': 'str',
        'diagnosis_dimension_list': 'list[DiagnosisDimension]',
        'command_time_taken_list': 'object'
    }

    attribute_map = {
        'node_ip': 'node_ip',
        'az_code': 'az_code',
        'group_name': 'group_name',
        'abnormal_sum': 'abnormal_sum',
        'failed_sum': 'failed_sum',
        'role': 'role',
        'diagnosis_dimension_list': 'diagnosis_dimension_list',
        'command_time_taken_list': 'command_time_taken_list'
    }

    def __init__(self, node_ip=None, az_code=None, group_name=None, abnormal_sum=None, failed_sum=None, role=None, diagnosis_dimension_list=None, command_time_taken_list=None):
        """DiagnosisNodeReport - a model defined in huaweicloud sdk"""
        
        

        self._node_ip = None
        self._az_code = None
        self._group_name = None
        self._abnormal_sum = None
        self._failed_sum = None
        self._role = None
        self._diagnosis_dimension_list = None
        self._command_time_taken_list = None
        self.discriminator = None

        self.node_ip = node_ip
        self.az_code = az_code
        self.group_name = group_name
        self.abnormal_sum = abnormal_sum
        self.failed_sum = failed_sum
        self.role = role
        self.diagnosis_dimension_list = diagnosis_dimension_list
        self.command_time_taken_list = command_time_taken_list

    @property
    def node_ip(self):
        """Gets the node_ip of this DiagnosisNodeReport.

        节点IP。例如：192.168.0.234:6379

        :return: The node_ip of this DiagnosisNodeReport.
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        """Sets the node_ip of this DiagnosisNodeReport.

        节点IP。例如：192.168.0.234:6379

        :param node_ip: The node_ip of this DiagnosisNodeReport.
        :type: str
        """
        self._node_ip = node_ip

    @property
    def az_code(self):
        """Gets the az_code of this DiagnosisNodeReport.

        节点所在可用区Code

        :return: The az_code of this DiagnosisNodeReport.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this DiagnosisNodeReport.

        节点所在可用区Code

        :param az_code: The az_code of this DiagnosisNodeReport.
        :type: str
        """
        self._az_code = az_code

    @property
    def group_name(self):
        """Gets the group_name of this DiagnosisNodeReport.

        节点所在分片的名称

        :return: The group_name of this DiagnosisNodeReport.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this DiagnosisNodeReport.

        节点所在分片的名称

        :param group_name: The group_name of this DiagnosisNodeReport.
        :type: str
        """
        self._group_name = group_name

    @property
    def abnormal_sum(self):
        """Gets the abnormal_sum of this DiagnosisNodeReport.

        诊断结果为异常的诊断项总数

        :return: The abnormal_sum of this DiagnosisNodeReport.
        :rtype: int
        """
        return self._abnormal_sum

    @abnormal_sum.setter
    def abnormal_sum(self, abnormal_sum):
        """Sets the abnormal_sum of this DiagnosisNodeReport.

        诊断结果为异常的诊断项总数

        :param abnormal_sum: The abnormal_sum of this DiagnosisNodeReport.
        :type: int
        """
        self._abnormal_sum = abnormal_sum

    @property
    def failed_sum(self):
        """Gets the failed_sum of this DiagnosisNodeReport.

        诊断失败的诊断项总数

        :return: The failed_sum of this DiagnosisNodeReport.
        :rtype: int
        """
        return self._failed_sum

    @failed_sum.setter
    def failed_sum(self, failed_sum):
        """Sets the failed_sum of this DiagnosisNodeReport.

        诊断失败的诊断项总数

        :param failed_sum: The failed_sum of this DiagnosisNodeReport.
        :type: int
        """
        self._failed_sum = failed_sum

    @property
    def role(self):
        """Gets the role of this DiagnosisNodeReport.

        节点角色

        :return: The role of this DiagnosisNodeReport.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DiagnosisNodeReport.

        节点角色

        :param role: The role of this DiagnosisNodeReport.
        :type: str
        """
        self._role = role

    @property
    def diagnosis_dimension_list(self):
        """Gets the diagnosis_dimension_list of this DiagnosisNodeReport.

        诊断维度列表

        :return: The diagnosis_dimension_list of this DiagnosisNodeReport.
        :rtype: list[DiagnosisDimension]
        """
        return self._diagnosis_dimension_list

    @diagnosis_dimension_list.setter
    def diagnosis_dimension_list(self, diagnosis_dimension_list):
        """Sets the diagnosis_dimension_list of this DiagnosisNodeReport.

        诊断维度列表

        :param diagnosis_dimension_list: The diagnosis_dimension_list of this DiagnosisNodeReport.
        :type: list[DiagnosisDimension]
        """
        self._diagnosis_dimension_list = diagnosis_dimension_list

    @property
    def command_time_taken_list(self):
        """Gets the command_time_taken_list of this DiagnosisNodeReport.

        命令耗时统计列表

        :return: The command_time_taken_list of this DiagnosisNodeReport.
        :rtype: object
        """
        return self._command_time_taken_list

    @command_time_taken_list.setter
    def command_time_taken_list(self, command_time_taken_list):
        """Sets the command_time_taken_list of this DiagnosisNodeReport.

        命令耗时统计列表

        :param command_time_taken_list: The command_time_taken_list of this DiagnosisNodeReport.
        :type: object
        """
        self._command_time_taken_list = command_time_taken_list

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
        if not isinstance(other, DiagnosisNodeReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other