# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListAvailableZonesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'available_zones': 'list[AvailableZones]'
    }

    attribute_map = {
        'region_id': 'region_id',
        'available_zones': 'available_zones'
    }

    def __init__(self, region_id=None, available_zones=None):
        """ListAvailableZonesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._region_id = None
        self._available_zones = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if available_zones is not None:
            self.available_zones = available_zones

    @property
    def region_id(self):
        """Gets the region_id of this ListAvailableZonesResponse.

        区域ID。

        :return: The region_id of this ListAvailableZonesResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListAvailableZonesResponse.

        区域ID。

        :param region_id: The region_id of this ListAvailableZonesResponse.
        :type: str
        """
        self._region_id = region_id

    @property
    def available_zones(self):
        """Gets the available_zones of this ListAvailableZonesResponse.

        可用分区数组。

        :return: The available_zones of this ListAvailableZonesResponse.
        :rtype: list[AvailableZones]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ListAvailableZonesResponse.

        可用分区数组。

        :param available_zones: The available_zones of this ListAvailableZonesResponse.
        :type: list[AvailableZones]
        """
        self._available_zones = available_zones

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
        if not isinstance(other, ListAvailableZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
