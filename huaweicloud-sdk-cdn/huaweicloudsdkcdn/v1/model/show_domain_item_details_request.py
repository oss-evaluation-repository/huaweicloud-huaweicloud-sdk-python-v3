# coding: utf-8

import pprint
import re

import six





class ShowDomainItemDetailsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'domain_name': 'str',
        'stat_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type'
    }

    def __init__(self, enterprise_project_id=None, start_time=None, end_time=None, domain_name=None, stat_type=None):
        """ShowDomainItemDetailsRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._stat_type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        self.stat_type = stat_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowDomainItemDetailsRequest.

        当用户开启企业项目功能时，该参数生效，表示资源所属企业项目，不传表示默认项目。

        :return: The enterprise_project_id of this ShowDomainItemDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowDomainItemDetailsRequest.

        当用户开启企业项目功能时，该参数生效，表示资源所属企业项目，不传表示默认项目。

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainItemDetailsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowDomainItemDetailsRequest.

        查询起始时间戳，必须设为5分钟整时刻点

        :return: The start_time of this ShowDomainItemDetailsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowDomainItemDetailsRequest.

        查询起始时间戳，必须设为5分钟整时刻点

        :param start_time: The start_time of this ShowDomainItemDetailsRequest.
        :type: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowDomainItemDetailsRequest.

        查询结束时间戳，必须设为5分钟整时刻点，与开始时间戳时间差不可以超过一天

        :return: The end_time of this ShowDomainItemDetailsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowDomainItemDetailsRequest.

        查询结束时间戳，必须设为5分钟整时刻点，与开始时间戳时间差不可以超过一天

        :param end_time: The end_time of this ShowDomainItemDetailsRequest.
        :type: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowDomainItemDetailsRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名

        :return: The domain_name of this ShowDomainItemDetailsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowDomainItemDetailsRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名

        :param domain_name: The domain_name of this ShowDomainItemDetailsRequest.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        """Gets the stat_type of this ShowDomainItemDetailsRequest.

        网络资源消耗： - bw（带宽） - flux（流量） - bs_bw(回源带宽) - bs_flux（回源流量）  访问情况： - req_num（请求总数） - hit_num（请求命中次数） - bs_num(回源总数) - bs_fail_num(回源失败数) - hit_flux（命中流量）

        :return: The stat_type of this ShowDomainItemDetailsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ShowDomainItemDetailsRequest.

        网络资源消耗： - bw（带宽） - flux（流量） - bs_bw(回源带宽) - bs_flux（回源流量）  访问情况： - req_num（请求总数） - hit_num（请求命中次数） - bs_num(回源总数) - bs_fail_num(回源失败数) - hit_flux（命中流量）

        :param stat_type: The stat_type of this ShowDomainItemDetailsRequest.
        :type: str
        """
        self._stat_type = stat_type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDomainItemDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other