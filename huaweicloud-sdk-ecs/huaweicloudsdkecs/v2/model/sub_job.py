# coding: utf-8

import pprint
import re

import six


class SubJob(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'status': 'str',
        'entities': 'SubJobEntities',
        'job_id': 'str',
        'job_type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'error_code': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'status': 'status',
        'entities': 'entities',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, status=None, entities=None, job_id=None, job_type=None, begin_time=None, end_time=None, error_code=None, fail_reason=None):  # noqa: E501
        """SubJob - a model defined in huaweicloud sdk"""

        self._status = None
        self._entities = None
        self._job_id = None
        self._job_type = None
        self._begin_time = None
        self._end_time = None
        self._error_code = None
        self._fail_reason = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if entities is not None:
            self.entities = entities
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def status(self):
        """Gets the status of this SubJob.

        Job的状态。  - SUCCESS：成功。  - RUNNING：运行中。  - FAIL：失败。  - INIT：正在初始化。

        :return: The status of this SubJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubJob.

        Job的状态。  - SUCCESS：成功。  - RUNNING：运行中。  - FAIL：失败。  - INIT：正在初始化。

        :param status: The status of this SubJob.
        :type: str
        """
        self._status = status

    @property
    def entities(self):
        """Gets the entities of this SubJob.


        :return: The entities of this SubJob.
        :rtype: SubJobEntities
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this SubJob.


        :param entities: The entities of this SubJob.
        :type: SubJobEntities
        """
        self._entities = entities

    @property
    def job_id(self):
        """Gets the job_id of this SubJob.

        子任务的ID。

        :return: The job_id of this SubJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this SubJob.

        子任务的ID。

        :param job_id: The job_id of this SubJob.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this SubJob.

        子任务的类型。

        :return: The job_type of this SubJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this SubJob.

        子任务的类型。

        :param job_type: The job_type of this SubJob.
        :type: str
        """
        self._job_type = job_type

    @property
    def begin_time(self):
        """Gets the begin_time of this SubJob.

        开始时间。

        :return: The begin_time of this SubJob.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this SubJob.

        开始时间。

        :param begin_time: The begin_time of this SubJob.
        :type: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this SubJob.

        结束时间。

        :return: The end_time of this SubJob.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SubJob.

        结束时间。

        :param end_time: The end_time of this SubJob.
        :type: str
        """
        self._end_time = end_time

    @property
    def error_code(self):
        """Gets the error_code of this SubJob.

        Job执行失败时的错误码。  Job执行成功后，该值为null。

        :return: The error_code of this SubJob.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this SubJob.

        Job执行失败时的错误码。  Job执行成功后，该值为null。

        :param error_code: The error_code of this SubJob.
        :type: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this SubJob.

        Job执行失败时的错误原因。  Job执行成功后，该值为null。

        :return: The fail_reason of this SubJob.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this SubJob.

        Job执行失败时的错误原因。  Job执行成功后，该值为null。

        :param fail_reason: The fail_reason of this SubJob.
        :type: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, SubJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
