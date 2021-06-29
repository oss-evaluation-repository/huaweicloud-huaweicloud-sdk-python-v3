# coding: utf-8

import pprint
import re

import six





class QueryLTSStructLogParamsNew:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'query': 'str',
        'format': 'str',
        'time_range': 'object'
    }

    attribute_map = {
        'query': 'query',
        'format': 'format',
        'time_range': 'time_range'
    }

    def __init__(self, query=None, format=None, time_range=None):
        """QueryLTSStructLogParamsNew - a model defined in huaweicloud sdk"""
        
        

        self._query = None
        self._format = None
        self._time_range = None
        self.discriminator = None

        self.query = query
        self.format = format
        self.time_range = time_range

    @property
    def query(self):
        """Gets the query of this QueryLTSStructLogParamsNew.

        sql语句字符串。

        :return: The query of this QueryLTSStructLogParamsNew.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryLTSStructLogParamsNew.

        sql语句字符串。

        :param query: The query of this QueryLTSStructLogParamsNew.
        :type: str
        """
        self._query = query

    @property
    def format(self):
        """Gets the format of this QueryLTSStructLogParamsNew.

        查询结果格式。当前仅支持：\"k-v\"。

        :return: The format of this QueryLTSStructLogParamsNew.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this QueryLTSStructLogParamsNew.

        查询结果格式。当前仅支持：\"k-v\"。

        :param format: The format of this QueryLTSStructLogParamsNew.
        :type: str
        """
        self._format = format

    @property
    def time_range(self):
        """Gets the time_range of this QueryLTSStructLogParamsNew.

        时间范围信息。

        :return: The time_range of this QueryLTSStructLogParamsNew.
        :rtype: object
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this QueryLTSStructLogParamsNew.

        时间范围信息。

        :param time_range: The time_range of this QueryLTSStructLogParamsNew.
        :type: object
        """
        self._time_range = time_range

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
        if not isinstance(other, QueryLTSStructLogParamsNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other