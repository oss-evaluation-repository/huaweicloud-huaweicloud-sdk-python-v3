# coding: utf-8

import pprint
import re

import six





class DomainRegion:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'region_isp_details': 'list[DomainRegionIspDetail]'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'region_isp_details': 'region_isp_details'
    }

    def __init__(self, domain_name=None, region_isp_details=None):
        """DomainRegion - a model defined in huaweicloud sdk"""
        
        

        self._domain_name = None
        self._region_isp_details = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if region_isp_details is not None:
            self.region_isp_details = region_isp_details

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainRegion.

        域名

        :return: The domain_name of this DomainRegion.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainRegion.

        域名

        :param domain_name: The domain_name of this DomainRegion.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def region_isp_details(self):
        """Gets the region_isp_details of this DomainRegion.

        指标统计数据列表  如果该时间段内无值，则为空数组[]

        :return: The region_isp_details of this DomainRegion.
        :rtype: list[DomainRegionIspDetail]
        """
        return self._region_isp_details

    @region_isp_details.setter
    def region_isp_details(self, region_isp_details):
        """Sets the region_isp_details of this DomainRegion.

        指标统计数据列表  如果该时间段内无值，则为空数组[]

        :param region_isp_details: The region_isp_details of this DomainRegion.
        :type: list[DomainRegionIspDetail]
        """
        self._region_isp_details = region_isp_details

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
        if not isinstance(other, DomainRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other