# coding: utf-8

import pprint
import re

import six


class CreateIpAddressGroupResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'address_group': 'AddressGroupResp'
    }

    attribute_map = {
        'address_group': 'address_group'
    }

    def __init__(self, address_group=None):  # noqa: E501
        """CreateIpAddressGroupResponse - a model defined in huaweicloud sdk"""

        self._address_group = None
        self.discriminator = None

        if address_group is not None:
            self.address_group = address_group

    @property
    def address_group(self):
        """Gets the address_group of this CreateIpAddressGroupResponse.


        :return: The address_group of this CreateIpAddressGroupResponse.
        :rtype: AddressGroupResp
        """
        return self._address_group

    @address_group.setter
    def address_group(self, address_group):
        """Sets the address_group of this CreateIpAddressGroupResponse.


        :param address_group: The address_group of this CreateIpAddressGroupResponse.
        :type: AddressGroupResp
        """
        self._address_group = address_group

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
        if not isinstance(other, CreateIpAddressGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
