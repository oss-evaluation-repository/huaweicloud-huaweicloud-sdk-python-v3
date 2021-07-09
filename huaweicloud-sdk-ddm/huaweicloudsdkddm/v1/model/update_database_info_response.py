# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateDatabaseInfoResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instanceId',
        'job_id': 'jobId'
    }

    def __init__(self, instance_id=None, job_id=None):
        """UpdateDatabaseInfoResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateDatabaseInfoResponse, self).__init__()

        self._instance_id = None
        self._job_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateDatabaseInfoResponse.

        DDM实例id。

        :return: The instance_id of this UpdateDatabaseInfoResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateDatabaseInfoResponse.

        DDM实例id。

        :param instance_id: The instance_id of this UpdateDatabaseInfoResponse.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def job_id(self):
        """Gets the job_id of this UpdateDatabaseInfoResponse.

        任务ID。

        :return: The job_id of this UpdateDatabaseInfoResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateDatabaseInfoResponse.

        任务ID。

        :param job_id: The job_id of this UpdateDatabaseInfoResponse.
        :type: str
        """
        self._job_id = job_id

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
        if not isinstance(other, UpdateDatabaseInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
