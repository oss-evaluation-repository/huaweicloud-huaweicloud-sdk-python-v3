# coding: utf-8

import pprint
import re

import six





class ListGeoipRulesRequest:


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
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, policy_id=None, offset=None, limit=None):
        """ListGeoipRulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._policy_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.policy_id = policy_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def policy_id(self):
        """Gets the policy_id of this ListGeoipRulesRequest.

        policyid

        :return: The policy_id of this ListGeoipRulesRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ListGeoipRulesRequest.

        policyid

        :param policy_id: The policy_id of this ListGeoipRulesRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def offset(self):
        """Gets the offset of this ListGeoipRulesRequest.

        offset

        :return: The offset of this ListGeoipRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListGeoipRulesRequest.

        offset

        :param offset: The offset of this ListGeoipRulesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListGeoipRulesRequest.

        limit

        :return: The limit of this ListGeoipRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGeoipRulesRequest.

        limit

        :param limit: The limit of this ListGeoipRulesRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListGeoipRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other