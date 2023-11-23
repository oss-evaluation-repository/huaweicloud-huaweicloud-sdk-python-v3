# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCassandraSlowLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slow_logs': 'list[CassandraSlowLogDetail]'
    }

    attribute_map = {
        'slow_logs': 'slow_logs'
    }

    def __init__(self, slow_logs=None):
        """ListCassandraSlowLogsResponse

        The model defined in huaweicloud sdk

        :param slow_logs: 慢日志具体信息。
        :type slow_logs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CassandraSlowLogDetail`]
        """
        
        super(ListCassandraSlowLogsResponse, self).__init__()

        self._slow_logs = None
        self.discriminator = None

        if slow_logs is not None:
            self.slow_logs = slow_logs

    @property
    def slow_logs(self):
        """Gets the slow_logs of this ListCassandraSlowLogsResponse.

        慢日志具体信息。

        :return: The slow_logs of this ListCassandraSlowLogsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CassandraSlowLogDetail`]
        """
        return self._slow_logs

    @slow_logs.setter
    def slow_logs(self, slow_logs):
        """Sets the slow_logs of this ListCassandraSlowLogsResponse.

        慢日志具体信息。

        :param slow_logs: The slow_logs of this ListCassandraSlowLogsResponse.
        :type slow_logs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CassandraSlowLogDetail`]
        """
        self._slow_logs = slow_logs

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
        if not isinstance(other, ListCassandraSlowLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other