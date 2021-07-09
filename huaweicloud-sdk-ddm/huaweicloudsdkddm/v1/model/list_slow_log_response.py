# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSlowLogResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_record': 'int',
        'slow_log_list': 'list[SlowLogList]'
    }

    attribute_map = {
        'total_record': 'totalRecord',
        'slow_log_list': 'slowLogList'
    }

    def __init__(self, total_record=None, slow_log_list=None):
        """ListSlowLogResponse - a model defined in huaweicloud sdk"""
        
        super(ListSlowLogResponse, self).__init__()

        self._total_record = None
        self._slow_log_list = None
        self.discriminator = None

        if total_record is not None:
            self.total_record = total_record
        if slow_log_list is not None:
            self.slow_log_list = slow_log_list

    @property
    def total_record(self):
        """Gets the total_record of this ListSlowLogResponse.

        DDM慢sql日志条数。

        :return: The total_record of this ListSlowLogResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListSlowLogResponse.

        DDM慢sql日志条数。

        :param total_record: The total_record of this ListSlowLogResponse.
        :type: int
        """
        self._total_record = total_record

    @property
    def slow_log_list(self):
        """Gets the slow_log_list of this ListSlowLogResponse.

        DDM慢sql日志信息列表的集合。

        :return: The slow_log_list of this ListSlowLogResponse.
        :rtype: list[SlowLogList]
        """
        return self._slow_log_list

    @slow_log_list.setter
    def slow_log_list(self, slow_log_list):
        """Sets the slow_log_list of this ListSlowLogResponse.

        DDM慢sql日志信息列表的集合。

        :param slow_log_list: The slow_log_list of this ListSlowLogResponse.
        :type: list[SlowLogList]
        """
        self._slow_log_list = slow_log_list

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSlowLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
