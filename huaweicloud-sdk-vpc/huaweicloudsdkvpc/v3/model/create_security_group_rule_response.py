# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityGroupRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'security_group_rule': 'SecurityGroupRule'
    }

    attribute_map = {
        'request_id': 'request_id',
        'security_group_rule': 'security_group_rule'
    }

    def __init__(self, request_id=None, security_group_rule=None):
        """CreateSecurityGroupRuleResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param security_group_rule: 
        :type security_group_rule: :class:`huaweicloudsdkvpc.v3.SecurityGroupRule`
        """
        
        super(CreateSecurityGroupRuleResponse, self).__init__()

        self._request_id = None
        self._security_group_rule = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if security_group_rule is not None:
            self.security_group_rule = security_group_rule

    @property
    def request_id(self):
        """Gets the request_id of this CreateSecurityGroupRuleResponse.

        请求ID

        :return: The request_id of this CreateSecurityGroupRuleResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateSecurityGroupRuleResponse.

        请求ID

        :param request_id: The request_id of this CreateSecurityGroupRuleResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def security_group_rule(self):
        """Gets the security_group_rule of this CreateSecurityGroupRuleResponse.


        :return: The security_group_rule of this CreateSecurityGroupRuleResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.SecurityGroupRule`
        """
        return self._security_group_rule

    @security_group_rule.setter
    def security_group_rule(self, security_group_rule):
        """Sets the security_group_rule of this CreateSecurityGroupRuleResponse.


        :param security_group_rule: The security_group_rule of this CreateSecurityGroupRuleResponse.
        :type security_group_rule: :class:`huaweicloudsdkvpc.v3.SecurityGroupRule`
        """
        self._security_group_rule = security_group_rule

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
        if not isinstance(other, CreateSecurityGroupRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
