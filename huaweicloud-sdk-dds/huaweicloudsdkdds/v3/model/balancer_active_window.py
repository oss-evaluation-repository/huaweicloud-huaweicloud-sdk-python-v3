# coding: utf-8

import re
import six





class BalancerActiveWindow:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'stop_time': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'stop_time': 'stop_time'
    }

    def __init__(self, start_time=None, stop_time=None):
        """BalancerActiveWindow - a model defined in huaweicloud sdk"""
        
        

        self._start_time = None
        self._stop_time = None
        self.discriminator = None

        self.start_time = start_time
        self.stop_time = stop_time

    @property
    def start_time(self):
        """Gets the start_time of this BalancerActiveWindow.

        活动时间窗开始时间。

        :return: The start_time of this BalancerActiveWindow.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BalancerActiveWindow.

        活动时间窗开始时间。

        :param start_time: The start_time of this BalancerActiveWindow.
        :type: str
        """
        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this BalancerActiveWindow.

        活动时间窗结束时间。

        :return: The stop_time of this BalancerActiveWindow.
        :rtype: str
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this BalancerActiveWindow.

        活动时间窗结束时间。

        :param stop_time: The stop_time of this BalancerActiveWindow.
        :type: str
        """
        self._stop_time = stop_time

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
        if not isinstance(other, BalancerActiveWindow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
