# coding: utf-8

import pprint
import re

import six





class LogStream:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'creation_time': 'int',
        'log_stream_name': 'str',
        'log_stream_id': 'str',
        'filter_count': 'int'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'log_stream_name': 'log_stream_name',
        'log_stream_id': 'log_stream_id',
        'filter_count': 'filter_count'
    }

    def __init__(self, creation_time=None, log_stream_name=None, log_stream_id=None, filter_count=None):
        """LogStream - a model defined in huaweicloud sdk"""
        
        

        self._creation_time = None
        self._log_stream_name = None
        self._log_stream_id = None
        self._filter_count = None
        self.discriminator = None

        self.creation_time = creation_time
        self.log_stream_name = log_stream_name
        self.log_stream_id = log_stream_id
        self.filter_count = filter_count

    @property
    def creation_time(self):
        """Gets the creation_time of this LogStream.

        创建时间 

        :return: The creation_time of this LogStream.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this LogStream.

        创建时间 

        :param creation_time: The creation_time of this LogStream.
        :type: int
        """
        self._creation_time = creation_time

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this LogStream.

        日志流名称 

        :return: The log_stream_name of this LogStream.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this LogStream.

        日志流名称 

        :param log_stream_name: The log_stream_name of this LogStream.
        :type: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this LogStream.

        日志流ID 

        :return: The log_stream_id of this LogStream.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this LogStream.

        日志流ID 

        :param log_stream_id: The log_stream_id of this LogStream.
        :type: str
        """
        self._log_stream_id = log_stream_id

    @property
    def filter_count(self):
        """Gets the filter_count of this LogStream.

        过滤器个数 

        :return: The filter_count of this LogStream.
        :rtype: int
        """
        return self._filter_count

    @filter_count.setter
    def filter_count(self, filter_count):
        """Sets the filter_count of this LogStream.

        过滤器个数 

        :param filter_count: The filter_count of this LogStream.
        :type: int
        """
        self._filter_count = filter_count

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
        if not isinstance(other, LogStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other