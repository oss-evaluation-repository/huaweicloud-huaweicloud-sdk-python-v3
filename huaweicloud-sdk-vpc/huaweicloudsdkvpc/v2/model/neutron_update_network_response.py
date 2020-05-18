# coding: utf-8

import pprint
import re

import six


class NeutronUpdateNetworkResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'network': 'NeutronNetwork'
    }

    attribute_map = {
        'network': 'network'
    }

    def __init__(self, network=None):  # noqa: E501
        """NeutronUpdateNetworkResponse - a model defined in huaweicloud sdk"""

        self._network = None
        self.discriminator = None

        if network is not None:
            self.network = network

    @property
    def network(self):
        """Gets the network of this NeutronUpdateNetworkResponse.


        :return: The network of this NeutronUpdateNetworkResponse.
        :rtype: NeutronNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this NeutronUpdateNetworkResponse.


        :param network: The network of this NeutronUpdateNetworkResponse.
        :type: NeutronNetwork
        """
        self._network = network

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
        if not isinstance(other, NeutronUpdateNetworkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
