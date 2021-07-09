# coding: utf-8

import re
import six





class DeleteSecretForScheduleRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'recovery_window_in_days': 'int'
    }

    attribute_map = {
        'recovery_window_in_days': 'recovery_window_in_days'
    }

    def __init__(self, recovery_window_in_days=None):
        """DeleteSecretForScheduleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._recovery_window_in_days = None
        self.discriminator = None

        self.recovery_window_in_days = recovery_window_in_days

    @property
    def recovery_window_in_days(self):
        """Gets the recovery_window_in_days of this DeleteSecretForScheduleRequestBody.

        创建定时删除凭据的任务，且指定可恢复的天数。  约束：7~30。  默认值：30。 

        :return: The recovery_window_in_days of this DeleteSecretForScheduleRequestBody.
        :rtype: int
        """
        return self._recovery_window_in_days

    @recovery_window_in_days.setter
    def recovery_window_in_days(self, recovery_window_in_days):
        """Sets the recovery_window_in_days of this DeleteSecretForScheduleRequestBody.

        创建定时删除凭据的任务，且指定可恢复的天数。  约束：7~30。  默认值：30。 

        :param recovery_window_in_days: The recovery_window_in_days of this DeleteSecretForScheduleRequestBody.
        :type: int
        """
        self._recovery_window_in_days = recovery_window_in_days

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
        if not isinstance(other, DeleteSecretForScheduleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
