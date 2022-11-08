# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePerformanceResourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_quota': 'int'
    }

    attribute_map = {
        'job_quota': 'job_quota'
    }

    def __init__(self, job_quota=None):
        """UpdatePerformanceResourceReq

        The model defined in huaweicloud sdk

        :param job_quota: 运行的最大作业数量
        :type job_quota: int
        """
        
        

        self._job_quota = None
        self.discriminator = None

        self.job_quota = job_quota

    @property
    def job_quota(self):
        """Gets the job_quota of this UpdatePerformanceResourceReq.

        运行的最大作业数量

        :return: The job_quota of this UpdatePerformanceResourceReq.
        :rtype: int
        """
        return self._job_quota

    @job_quota.setter
    def job_quota(self, job_quota):
        """Sets the job_quota of this UpdatePerformanceResourceReq.

        运行的最大作业数量

        :param job_quota: The job_quota of this UpdatePerformanceResourceReq.
        :type job_quota: int
        """
        self._job_quota = job_quota

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
        if not isinstance(other, UpdatePerformanceResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other