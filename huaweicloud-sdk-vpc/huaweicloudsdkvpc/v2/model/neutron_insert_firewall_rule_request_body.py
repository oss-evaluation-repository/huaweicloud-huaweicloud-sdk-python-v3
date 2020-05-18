# coding: utf-8

import pprint
import re

import six


class NeutronInsertFirewallRuleRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'firewall_rule_id': 'str',
        'insert_after': 'str',
        'insert_before': 'str'
    }

    attribute_map = {
        'firewall_rule_id': 'firewall_rule_id',
        'insert_after': 'insert_after',
        'insert_before': 'insert_before'
    }

    def __init__(self, firewall_rule_id=None, insert_after=None, insert_before=None):  # noqa: E501
        """NeutronInsertFirewallRuleRequestBody - a model defined in huaweicloud sdk"""

        self._firewall_rule_id = None
        self._insert_after = None
        self._insert_before = None
        self.discriminator = None

        self.firewall_rule_id = firewall_rule_id
        if insert_after is not None:
            self.insert_after = insert_after
        if insert_before is not None:
            self.insert_before = insert_before

    @property
    def firewall_rule_id(self):
        """Gets the firewall_rule_id of this NeutronInsertFirewallRuleRequestBody.

        网络ACL防火墙规则ID

        :return: The firewall_rule_id of this NeutronInsertFirewallRuleRequestBody.
        :rtype: str
        """
        return self._firewall_rule_id

    @firewall_rule_id.setter
    def firewall_rule_id(self, firewall_rule_id):
        """Sets the firewall_rule_id of this NeutronInsertFirewallRuleRequestBody.

        网络ACL防火墙规则ID

        :param firewall_rule_id: The firewall_rule_id of this NeutronInsertFirewallRuleRequestBody.
        :type: str
        """
        self._firewall_rule_id = firewall_rule_id

    @property
    def insert_after(self):
        """Gets the insert_after of this NeutronInsertFirewallRuleRequestBody.

        insert_after参数表示已经和某个policy关联的rule，新的rule将会直接被插入到insert_after参数指定的rule后面。如果insert_after和insert_before都被指定了，insert_after参数值将被忽略。

        :return: The insert_after of this NeutronInsertFirewallRuleRequestBody.
        :rtype: str
        """
        return self._insert_after

    @insert_after.setter
    def insert_after(self, insert_after):
        """Sets the insert_after of this NeutronInsertFirewallRuleRequestBody.

        insert_after参数表示已经和某个policy关联的rule，新的rule将会直接被插入到insert_after参数指定的rule后面。如果insert_after和insert_before都被指定了，insert_after参数值将被忽略。

        :param insert_after: The insert_after of this NeutronInsertFirewallRuleRequestBody.
        :type: str
        """
        self._insert_after = insert_after

    @property
    def insert_before(self):
        """Gets the insert_before of this NeutronInsertFirewallRuleRequestBody.

        insert_before参数表示已经和某个policy关联的rule，新的firewall rule将会直接被插入到insert_ before参数指定的firewall rule前面。如果insert_after和insert_before都被指定了，insert_after参数值将被忽略。

        :return: The insert_before of this NeutronInsertFirewallRuleRequestBody.
        :rtype: str
        """
        return self._insert_before

    @insert_before.setter
    def insert_before(self, insert_before):
        """Sets the insert_before of this NeutronInsertFirewallRuleRequestBody.

        insert_before参数表示已经和某个policy关联的rule，新的firewall rule将会直接被插入到insert_ before参数指定的firewall rule前面。如果insert_after和insert_before都被指定了，insert_after参数值将被忽略。

        :param insert_before: The insert_before of this NeutronInsertFirewallRuleRequestBody.
        :type: str
        """
        self._insert_before = insert_before

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
        if not isinstance(other, NeutronInsertFirewallRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
