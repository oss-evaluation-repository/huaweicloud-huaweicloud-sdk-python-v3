# coding: utf-8

import re
import six





class UpdateLogGroupParams:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ttl_in_days': 'int'
    }

    attribute_map = {
        'ttl_in_days': 'ttl_in_days'
    }

    def __init__(self, ttl_in_days=None):
        """UpdateLogGroupParams - a model defined in huaweicloud sdk"""
        
        

        self._ttl_in_days = None
        self.discriminator = None

        self.ttl_in_days = ttl_in_days

    @property
    def ttl_in_days(self):
        """Gets the ttl_in_days of this UpdateLogGroupParams.

        日志存储时间 天。 取值范围为 [1, 30]

        :return: The ttl_in_days of this UpdateLogGroupParams.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        """Sets the ttl_in_days of this UpdateLogGroupParams.

        日志存储时间 天。 取值范围为 [1, 30]

        :param ttl_in_days: The ttl_in_days of this UpdateLogGroupParams.
        :type: int
        """
        self._ttl_in_days = ttl_in_days

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
        if not isinstance(other, UpdateLogGroupParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
