# coding: utf-8

import pprint
import re

import six


class EnableOrDisableScalingGroupRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'scaling_group_id': 'str',
        'body': 'EnableOrDisableScalingGroupRequestBody'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'body': 'body'
    }

    def __init__(self, scaling_group_id=None, body=None):  # noqa: E501
        """EnableOrDisableScalingGroupRequest - a model defined in huaweicloud sdk"""

        self._scaling_group_id = None
        self._body = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        if body is not None:
            self.body = body

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this EnableOrDisableScalingGroupRequest.


        :return: The scaling_group_id of this EnableOrDisableScalingGroupRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this EnableOrDisableScalingGroupRequest.


        :param scaling_group_id: The scaling_group_id of this EnableOrDisableScalingGroupRequest.
        :type: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def body(self):
        """Gets the body of this EnableOrDisableScalingGroupRequest.


        :return: The body of this EnableOrDisableScalingGroupRequest.
        :rtype: EnableOrDisableScalingGroupRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EnableOrDisableScalingGroupRequest.


        :param body: The body of this EnableOrDisableScalingGroupRequest.
        :type: EnableOrDisableScalingGroupRequestBody
        """
        self._body = body

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
        if not isinstance(other, EnableOrDisableScalingGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
