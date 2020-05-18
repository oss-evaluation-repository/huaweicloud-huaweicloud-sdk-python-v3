# coding: utf-8

import pprint
import re

import six


class RollbackSnapshotResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'rollback': 'RollbackInfo'
    }

    attribute_map = {
        'rollback': 'rollback'
    }

    def __init__(self, rollback=None):  # noqa: E501
        """RollbackSnapshotResponse - a model defined in huaweicloud sdk"""

        self._rollback = None
        self.discriminator = None

        if rollback is not None:
            self.rollback = rollback

    @property
    def rollback(self):
        """Gets the rollback of this RollbackSnapshotResponse.


        :return: The rollback of this RollbackSnapshotResponse.
        :rtype: RollbackInfo
        """
        return self._rollback

    @rollback.setter
    def rollback(self, rollback):
        """Sets the rollback of this RollbackSnapshotResponse.


        :param rollback: The rollback of this RollbackSnapshotResponse.
        :type: RollbackInfo
        """
        self._rollback = rollback

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
        if not isinstance(other, RollbackSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
