# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyProtectHostRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'hosts': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'hosts': 'hosts'
    }

    def __init__(self, policy_id=None, hosts=None):
        """UpdatePolicyProtectHostRequest - a model defined in huaweicloud sdk"""
        
        

        self._policy_id = None
        self._hosts = None
        self.discriminator = None

        self.policy_id = policy_id
        self.hosts = hosts

    @property
    def policy_id(self):
        """Gets the policy_id of this UpdatePolicyProtectHostRequest.

        策略id（策略id从查询防护策略列表接口获取）

        :return: The policy_id of this UpdatePolicyProtectHostRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this UpdatePolicyProtectHostRequest.

        策略id（策略id从查询防护策略列表接口获取）

        :param policy_id: The policy_id of this UpdatePolicyProtectHostRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def hosts(self):
        """Gets the hosts of this UpdatePolicyProtectHostRequest.

        域名id9从获取防护网站列表获取域名id）

        :return: The hosts of this UpdatePolicyProtectHostRequest.
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this UpdatePolicyProtectHostRequest.

        域名id9从获取防护网站列表获取域名id）

        :param hosts: The hosts of this UpdatePolicyProtectHostRequest.
        :type: str
        """
        self._hosts = hosts

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
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatePolicyProtectHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other