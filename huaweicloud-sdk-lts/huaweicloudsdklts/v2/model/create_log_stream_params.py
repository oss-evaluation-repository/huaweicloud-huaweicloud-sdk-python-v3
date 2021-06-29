# coding: utf-8

import pprint
import re

import six





class CreateLogStreamParams:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'log_stream_name': 'str',
        'tag': 'object'
    }

    attribute_map = {
        'log_stream_name': 'log_stream_name',
        'tag': 'tag'
    }

    def __init__(self, log_stream_name=None, tag=None):
        """CreateLogStreamParams - a model defined in huaweicloud sdk"""
        
        

        self._log_stream_name = None
        self._tag = None
        self.discriminator = None

        self.log_stream_name = log_stream_name
        if tag is not None:
            self.tag = tag

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this CreateLogStreamParams.

        需要创建的日志流名称。

        :return: The log_stream_name of this CreateLogStreamParams.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this CreateLogStreamParams.

        需要创建的日志流名称。

        :param log_stream_name: The log_stream_name of this CreateLogStreamParams.
        :type: str
        """
        self._log_stream_name = log_stream_name

    @property
    def tag(self):
        """Gets the tag of this CreateLogStreamParams.

        日志流Tag集合，不同日志流属性不同。

        :return: The tag of this CreateLogStreamParams.
        :rtype: object
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CreateLogStreamParams.

        日志流Tag集合，不同日志流属性不同。

        :param tag: The tag of this CreateLogStreamParams.
        :type: object
        """
        self._tag = tag

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
        if not isinstance(other, CreateLogStreamParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other