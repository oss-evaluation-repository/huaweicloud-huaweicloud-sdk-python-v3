# coding: utf-8

import re
import six





class BatchJobActionReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'job_id': 'str',
        '_property': 'str'
    }

    attribute_map = {
        'action': 'action',
        'job_id': 'job_id',
        '_property': 'property'
    }

    def __init__(self, action=None, job_id=None, _property=None):
        """BatchJobActionReq - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._job_id = None
        self.__property = None
        self.discriminator = None

        self.action = action
        self.job_id = job_id
        self._property = _property

    @property
    def action(self):
        """Gets the action of this BatchJobActionReq.

        执行操作

        :return: The action of this BatchJobActionReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchJobActionReq.

        执行操作

        :param action: The action of this BatchJobActionReq.
        :type: str
        """
        self._action = action

    @property
    def job_id(self):
        """Gets the job_id of this BatchJobActionReq.

        任务ID（集群模式 取父任务的任务id）

        :return: The job_id of this BatchJobActionReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BatchJobActionReq.

        任务ID（集群模式 取父任务的任务id）

        :param job_id: The job_id of this BatchJobActionReq.
        :type: str
        """
        self._job_id = job_id

    @property
    def _property(self):
        """Gets the _property of this BatchJobActionReq.

        操作对应的参数（API参考文档-批量测试连接-集群模式-property字段数据结构说明）[字段说明参考](https://support.huaweicloud.com/api-drs/zh-cn_topic_0295171516.html)

        :return: The _property of this BatchJobActionReq.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this BatchJobActionReq.

        操作对应的参数（API参考文档-批量测试连接-集群模式-property字段数据结构说明）[字段说明参考](https://support.huaweicloud.com/api-drs/zh-cn_topic_0295171516.html)

        :param _property: The _property of this BatchJobActionReq.
        :type: str
        """
        self.__property = _property

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
        if not isinstance(other, BatchJobActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
