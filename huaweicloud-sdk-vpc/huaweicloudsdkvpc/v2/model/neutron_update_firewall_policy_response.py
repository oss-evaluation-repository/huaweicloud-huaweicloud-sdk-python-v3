# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronUpdateFirewallPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_policy': 'NeutronFirewallPolicy'
    }

    attribute_map = {
        'firewall_policy': 'firewall_policy'
    }

    def __init__(self, firewall_policy=None):
        """NeutronUpdateFirewallPolicyResponse

        The model defined in huaweicloud sdk

        :param firewall_policy: 
        :type firewall_policy: :class:`huaweicloudsdkvpc.v2.NeutronFirewallPolicy`
        """
        
        super(NeutronUpdateFirewallPolicyResponse, self).__init__()

        self._firewall_policy = None
        self.discriminator = None

        if firewall_policy is not None:
            self.firewall_policy = firewall_policy

    @property
    def firewall_policy(self):
        """Gets the firewall_policy of this NeutronUpdateFirewallPolicyResponse.


        :return: The firewall_policy of this NeutronUpdateFirewallPolicyResponse.
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronFirewallPolicy`
        """
        return self._firewall_policy

    @firewall_policy.setter
    def firewall_policy(self, firewall_policy):
        """Sets the firewall_policy of this NeutronUpdateFirewallPolicyResponse.


        :param firewall_policy: The firewall_policy of this NeutronUpdateFirewallPolicyResponse.
        :type firewall_policy: :class:`huaweicloudsdkvpc.v2.NeutronFirewallPolicy`
        """
        self._firewall_policy = firewall_policy

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NeutronUpdateFirewallPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
