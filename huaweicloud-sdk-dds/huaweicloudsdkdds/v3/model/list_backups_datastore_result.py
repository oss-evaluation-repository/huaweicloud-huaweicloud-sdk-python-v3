# coding: utf-8

import pprint
import re

import six


class ListBackupsDatastoreResult(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, type=None, version=None):  # noqa: E501
        """ListBackupsDatastoreResult - a model defined in huaweicloud sdk"""

        self._type = None
        self._version = None
        self.discriminator = None

        self.type = type
        self.version = version

    @property
    def type(self):
        """Gets the type of this ListBackupsDatastoreResult.

        数据库引擎。 取值：DDS-Community，或DDS-Enhanced。

        :return: The type of this ListBackupsDatastoreResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListBackupsDatastoreResult.

        数据库引擎。 取值：DDS-Community，或DDS-Enhanced。

        :param type: The type of this ListBackupsDatastoreResult.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListBackupsDatastoreResult.

        数据库版本。取值： - 社区版引擎取“3.2”、“3.4”或“4.0”。 - 增强版引擎取“3.4”。 支持3.2、3.4和4.0数据库版本。取值为“3.2”、“3.4”或“4.0”。

        :return: The version of this ListBackupsDatastoreResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListBackupsDatastoreResult.

        数据库版本。取值： - 社区版引擎取“3.2”、“3.4”或“4.0”。 - 增强版引擎取“3.4”。 支持3.2、3.4和4.0数据库版本。取值为“3.2”、“3.4”或“4.0”。

        :param version: The version of this ListBackupsDatastoreResult.
        :type: str
        """
        self._version = version

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
        if not isinstance(other, ListBackupsDatastoreResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
