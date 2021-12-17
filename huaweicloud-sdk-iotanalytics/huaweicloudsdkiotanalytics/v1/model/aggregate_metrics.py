# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregateMetrics:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'time_span': 'TimeSpan',
        'interval': 'str',
        'offset': 'str',
        'tags': 'dict(str, str)',
        'metrics': 'list[AggregateMetric]',
        'limit': 'int'
    }

    attribute_map = {
        'time_span': 'time_span',
        'interval': 'interval',
        'offset': 'offset',
        'tags': 'tags',
        'metrics': 'metrics',
        'limit': 'limit'
    }

    def __init__(self, time_span=None, interval=None, offset=None, tags=None, metrics=None, limit=None):
        """AggregateMetrics - a model defined in huaweicloud sdk"""
        
        

        self._time_span = None
        self._interval = None
        self._offset = None
        self._tags = None
        self._metrics = None
        self._limit = None
        self.discriminator = None

        self.time_span = time_span
        if interval is not None:
            self.interval = interval
        if offset is not None:
            self.offset = offset
        self.tags = tags
        self.metrics = metrics
        if limit is not None:
            self.limit = limit

    @property
    def time_span(self):
        """Gets the time_span of this AggregateMetrics.


        :return: The time_span of this AggregateMetrics.
        :rtype: TimeSpan
        """
        return self._time_span

    @time_span.setter
    def time_span(self, time_span):
        """Sets the time_span of this AggregateMetrics.


        :param time_span: The time_span of this AggregateMetrics.
        :type: TimeSpan
        """
        self._time_span = time_span

    @property
    def interval(self):
        """Gets the interval of this AggregateMetrics.

        聚合时间间隔, 示例：\"1d|1h|10m|10s\"

        :return: The interval of this AggregateMetrics.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this AggregateMetrics.

        聚合时间间隔, 示例：\"1d|1h|10m|10s\"

        :param interval: The interval of this AggregateMetrics.
        :type: str
        """
        self._interval = interval

    @property
    def offset(self):
        """Gets the offset of this AggregateMetrics.

        聚合时间偏移量, 需要小于interval, 示例： \"1h|10m|10s\"

        :return: The offset of this AggregateMetrics.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this AggregateMetrics.

        聚合时间偏移量, 需要小于interval, 示例： \"1h|10m|10s\"

        :param offset: The offset of this AggregateMetrics.
        :type: str
        """
        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this AggregateMetrics.

        对property按指定tags标签进行过滤查询，填入设备标签与标签值，不可为空，例如 {\"deviceId\": \"id0001\"}

        :return: The tags of this AggregateMetrics.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AggregateMetrics.

        对property按指定tags标签进行过滤查询，填入设备标签与标签值，不可为空，例如 {\"deviceId\": \"id0001\"}

        :param tags: The tags of this AggregateMetrics.
        :type: dict(str, str)
        """
        self._tags = tags

    @property
    def metrics(self):
        """Gets the metrics of this AggregateMetrics.

        查询的测量指标列表

        :return: The metrics of this AggregateMetrics.
        :rtype: list[AggregateMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this AggregateMetrics.

        查询的测量指标列表

        :param metrics: The metrics of this AggregateMetrics.
        :type: list[AggregateMetric]
        """
        self._metrics = metrics

    @property
    def limit(self):
        """Gets the limit of this AggregateMetrics.

        返回值个数限制

        :return: The limit of this AggregateMetrics.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this AggregateMetrics.

        返回值个数限制

        :param limit: The limit of this AggregateMetrics.
        :type: int
        """
        self._limit = limit

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AggregateMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
