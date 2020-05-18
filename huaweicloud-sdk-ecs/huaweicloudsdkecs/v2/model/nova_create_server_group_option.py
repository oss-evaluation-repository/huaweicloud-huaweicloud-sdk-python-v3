# coding: utf-8

import pprint
import re

import six


class NovaCreateServerGroupOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'name': 'str',
        'policies': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'policies': 'policies'
    }

    def __init__(self, name=None, policies=None):  # noqa: E501
        """NovaCreateServerGroupOption - a model defined in huaweicloud sdk"""

        self._name = None
        self._policies = None
        self.discriminator = None

        self.name = name
        self.policies = policies

    @property
    def name(self):
        """Gets the name of this NovaCreateServerGroupOption.

        弹性云服务器组名称，长度大于0小于256字节。

        :return: The name of this NovaCreateServerGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaCreateServerGroupOption.

        弹性云服务器组名称，长度大于0小于256字节。

        :param name: The name of this NovaCreateServerGroupOption.
        :type: str
        """
        self._name = name

    @property
    def policies(self):
        """Gets the policies of this NovaCreateServerGroupOption.

        与云服务器组关联的策略名称列表。包括：  - anti-affinity：此组中的弹性云服务器必须安排到不同的主机。  - affinity：此组中的弹性云服务器必须安排在同一主机上。  - soft-anti-affinity：如果可能，应将此组中的云服务器尽量安排到不同的主机上，但如果无法实现，则仍应安排它们，而不是导致生成失败。  - soft-affinity：如果可能，应将此组中的弹性云服务器尽量安排在同一主机上， 但如果无法实现，则仍应安排它们，而不是导致生成失败。   > 说明：  - 当前仅支持反亲和性anti-affinity策略。

        :return: The policies of this NovaCreateServerGroupOption.
        :rtype: list[str]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this NovaCreateServerGroupOption.

        与云服务器组关联的策略名称列表。包括：  - anti-affinity：此组中的弹性云服务器必须安排到不同的主机。  - affinity：此组中的弹性云服务器必须安排在同一主机上。  - soft-anti-affinity：如果可能，应将此组中的云服务器尽量安排到不同的主机上，但如果无法实现，则仍应安排它们，而不是导致生成失败。  - soft-affinity：如果可能，应将此组中的弹性云服务器尽量安排在同一主机上， 但如果无法实现，则仍应安排它们，而不是导致生成失败。   > 说明：  - 当前仅支持反亲和性anti-affinity策略。

        :param policies: The policies of this NovaCreateServerGroupOption.
        :type: list[str]
        """
        self._policies = policies

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
        if not isinstance(other, NovaCreateServerGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
