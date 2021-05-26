# coding: utf-8

import pprint
import re

import six





class NeutronListFirewallRulesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'action': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'action': 'action',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, marker=None, limit=None, id=None, name=None, description=None, action=None, tenant_id=None):
        """NeutronListFirewallRulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._marker = None
        self._limit = None
        self._id = None
        self._name = None
        self._description = None
        self._action = None
        self._tenant_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if action is not None:
            self.action = action
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def marker(self):
        """Gets the marker of this NeutronListFirewallRulesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this NeutronListFirewallRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListFirewallRulesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this NeutronListFirewallRulesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this NeutronListFirewallRulesRequest.

        每页返回的个数

        :return: The limit of this NeutronListFirewallRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListFirewallRulesRequest.

        每页返回的个数

        :param limit: The limit of this NeutronListFirewallRulesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def id(self):
        """Gets the id of this NeutronListFirewallRulesRequest.

        使用网络ACL规则ID过滤网络ACL规则

        :return: The id of this NeutronListFirewallRulesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListFirewallRulesRequest.

        使用网络ACL规则ID过滤网络ACL规则

        :param id: The id of this NeutronListFirewallRulesRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronListFirewallRulesRequest.

        使用网络ACL规则name过滤网络ACL规则

        :return: The name of this NeutronListFirewallRulesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronListFirewallRulesRequest.

        使用网络ACL规则name过滤网络ACL规则

        :param name: The name of this NeutronListFirewallRulesRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronListFirewallRulesRequest.

        使用网络ACL规则的description过滤网络ACL规则

        :return: The description of this NeutronListFirewallRulesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronListFirewallRulesRequest.

        使用网络ACL规则的description过滤网络ACL规则

        :param description: The description of this NeutronListFirewallRulesRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def action(self):
        """Gets the action of this NeutronListFirewallRulesRequest.

        使用action过滤查询网络ACL规则

        :return: The action of this NeutronListFirewallRulesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NeutronListFirewallRulesRequest.

        使用action过滤查询网络ACL规则

        :param action: The action of this NeutronListFirewallRulesRequest.
        :type: str
        """
        self._action = action

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListFirewallRulesRequest.

        使用tenant_id过滤查询网络ACL规则

        :return: The tenant_id of this NeutronListFirewallRulesRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListFirewallRulesRequest.

        使用tenant_id过滤查询网络ACL规则

        :param tenant_id: The tenant_id of this NeutronListFirewallRulesRequest.
        :type: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, NeutronListFirewallRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
