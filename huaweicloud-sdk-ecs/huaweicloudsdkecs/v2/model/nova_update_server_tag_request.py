# coding: utf-8

import pprint
import re

import six


class NovaUpdateServerTagRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'server_id': 'str',
        'tag': 'str',
        'open_stack_api_version': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'tag': 'tag',
        'open_stack_api_version': 'OpenStack-API-Version'
    }

    def __init__(self, server_id=None, tag=None, open_stack_api_version='compute 2.26'):  # noqa: E501
        """NovaUpdateServerTagRequest - a model defined in huaweicloud sdk"""

        self._server_id = None
        self._tag = None
        self._open_stack_api_version = None
        self.discriminator = None

        self.server_id = server_id
        self.tag = tag
        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version

    @property
    def server_id(self):
        """Gets the server_id of this NovaUpdateServerTagRequest.


        :return: The server_id of this NovaUpdateServerTagRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this NovaUpdateServerTagRequest.


        :param server_id: The server_id of this NovaUpdateServerTagRequest.
        :type: str
        """
        self._server_id = server_id

    @property
    def tag(self):
        """Gets the tag of this NovaUpdateServerTagRequest.


        :return: The tag of this NovaUpdateServerTagRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this NovaUpdateServerTagRequest.


        :param tag: The tag of this NovaUpdateServerTagRequest.
        :type: str
        """
        self._tag = tag

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaUpdateServerTagRequest.


        :return: The open_stack_api_version of this NovaUpdateServerTagRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaUpdateServerTagRequest.


        :param open_stack_api_version: The open_stack_api_version of this NovaUpdateServerTagRequest.
        :type: str
        """
        self._open_stack_api_version = open_stack_api_version

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
        if not isinstance(other, NovaUpdateServerTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
