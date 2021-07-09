# coding: utf-8

import re
import six





class NeutronShowFirewallRuleRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_rule_id': 'str'
    }

    attribute_map = {
        'firewall_rule_id': 'firewall_rule_id'
    }

    def __init__(self, firewall_rule_id=None):
        """NeutronShowFirewallRuleRequest - a model defined in huaweicloud sdk"""
        
        

        self._firewall_rule_id = None
        self.discriminator = None

        self.firewall_rule_id = firewall_rule_id

    @property
    def firewall_rule_id(self):
        """Gets the firewall_rule_id of this NeutronShowFirewallRuleRequest.

        网络ACL规则ID

        :return: The firewall_rule_id of this NeutronShowFirewallRuleRequest.
        :rtype: str
        """
        return self._firewall_rule_id

    @firewall_rule_id.setter
    def firewall_rule_id(self, firewall_rule_id):
        """Sets the firewall_rule_id of this NeutronShowFirewallRuleRequest.

        网络ACL规则ID

        :param firewall_rule_id: The firewall_rule_id of this NeutronShowFirewallRuleRequest.
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
        if not isinstance(other, NeutronShowFirewallRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
