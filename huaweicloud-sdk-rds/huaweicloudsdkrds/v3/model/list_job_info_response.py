# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListJobInfoResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job': 'GetJobInfoResponseBodyJob'
    }

    attribute_map = {
        'job': 'job'
    }

    def __init__(self, job=None):
        """ListJobInfoResponse - a model defined in huaweicloud sdk"""
        
        super(ListJobInfoResponse, self).__init__()

        self._job = None
        self.discriminator = None

        if job is not None:
            self.job = job

    @property
    def job(self):
        """Gets the job of this ListJobInfoResponse.


        :return: The job of this ListJobInfoResponse.
        :rtype: GetJobInfoResponseBodyJob
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this ListJobInfoResponse.


        :param job: The job of this ListJobInfoResponse.
        :type: GetJobInfoResponseBodyJob
        """
        self._job = job

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
        if not isinstance(other, ListJobInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
