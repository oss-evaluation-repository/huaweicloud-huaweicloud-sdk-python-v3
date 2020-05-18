# coding: utf-8

import pprint
import re

import six


class NeutronRemoveFirewallRuleRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'firewall_rule_id': 'str'
    }

    attribute_map = {
        'firewall_rule_id': 'firewall_rule_id'
    }

    def __init__(self, firewall_rule_id=None):  # noqa: E501
        """NeutronRemoveFirewallRuleRequestBody - a model defined in huaweicloud sdk"""

        self._firewall_rule_id = None
        self.discriminator = None

        self.firewall_rule_id = firewall_rule_id

    @property
    def firewall_rule_id(self):
        """Gets the firewall_rule_id of this NeutronRemoveFirewallRuleRequestBody.

        待移除的ACL规则ID

        :return: The firewall_rule_id of this NeutronRemoveFirewallRuleRequestBody.
        :rtype: str
        """
        return self._firewall_rule_id

    @firewall_rule_id.setter
    def firewall_rule_id(self, firewall_rule_id):
        """Sets the firewall_rule_id of this NeutronRemoveFirewallRuleRequestBody.

        待移除的ACL规则ID

        :param firewall_rule_id: The firewall_rule_id of this NeutronRemoveFirewallRuleRequestBody.
        :type: str
        """
        self._firewall_rule_id = firewall_rule_id

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
        if not isinstance(other, NeutronRemoveFirewallRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
