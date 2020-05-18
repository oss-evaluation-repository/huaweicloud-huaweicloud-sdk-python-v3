# coding: utf-8

import pprint
import re

import six


class UpdateRouteTableRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'routetable_id': 'str',
        'body': 'UpdateRoutetableReqBody'
    }

    attribute_map = {
        'routetable_id': 'routetable_id',
        'body': 'body'
    }

    def __init__(self, routetable_id=None, body=None):  # noqa: E501
        """UpdateRouteTableRequest - a model defined in huaweicloud sdk"""

        self._routetable_id = None
        self._body = None
        self.discriminator = None

        self.routetable_id = routetable_id
        if body is not None:
            self.body = body

    @property
    def routetable_id(self):
        """Gets the routetable_id of this UpdateRouteTableRequest.


        :return: The routetable_id of this UpdateRouteTableRequest.
        :rtype: str
        """
        return self._routetable_id

    @routetable_id.setter
    def routetable_id(self, routetable_id):
        """Sets the routetable_id of this UpdateRouteTableRequest.


        :param routetable_id: The routetable_id of this UpdateRouteTableRequest.
        :type: str
        """
        self._routetable_id = routetable_id

    @property
    def body(self):
        """Gets the body of this UpdateRouteTableRequest.


        :return: The body of this UpdateRouteTableRequest.
        :rtype: UpdateRoutetableReqBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateRouteTableRequest.


        :param body: The body of this UpdateRouteTableRequest.
        :type: UpdateRoutetableReqBody
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
        if not isinstance(other, UpdateRouteTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
