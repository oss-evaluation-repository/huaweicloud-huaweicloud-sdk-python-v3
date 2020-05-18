# coding: utf-8

import pprint
import re

import six


class ExternalGatewayInfo(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'enable_snat': 'bool',
        'network_id': 'str'
    }

    attribute_map = {
        'enable_snat': 'enable_snat',
        'network_id': 'network_id'
    }

    def __init__(self, enable_snat=None, network_id=None):  # noqa: E501
        """ExternalGatewayInfo - a model defined in huaweicloud sdk"""

        self._enable_snat = None
        self._network_id = None
        self.discriminator = None

        if enable_snat is not None:
            self.enable_snat = enable_snat
        if network_id is not None:
            self.network_id = network_id

    @property
    def enable_snat(self):
        """Gets the enable_snat of this ExternalGatewayInfo.

        功能说明：是否启用SNAT 取值范围：true、false；默认为false。

        :return: The enable_snat of this ExternalGatewayInfo.
        :rtype: bool
        """
        return self._enable_snat

    @enable_snat.setter
    def enable_snat(self, enable_snat):
        """Sets the enable_snat of this ExternalGatewayInfo.

        功能说明：是否启用SNAT 取值范围：true、false；默认为false。

        :param enable_snat: The enable_snat of this ExternalGatewayInfo.
        :type: bool
        """
        self._enable_snat = enable_snat

    @property
    def network_id(self):
        """Gets the network_id of this ExternalGatewayInfo.

        外部网络的ID。

        :return: The network_id of this ExternalGatewayInfo.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this ExternalGatewayInfo.

        外部网络的ID。

        :param network_id: The network_id of this ExternalGatewayInfo.
        :type: str
        """
        self._network_id = network_id

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
        if not isinstance(other, ExternalGatewayInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
