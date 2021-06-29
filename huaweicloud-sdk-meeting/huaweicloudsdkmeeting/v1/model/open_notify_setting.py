# coding: utf-8

import pprint
import re

import six





class OpenNotifySetting:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enable_calendar': 'str',
        'enable_sms': 'str',
        'enable_email': 'str'
    }

    attribute_map = {
        'enable_calendar': 'enableCalendar',
        'enable_sms': 'enableSms',
        'enable_email': 'enableEmail'
    }

    def __init__(self, enable_calendar=None, enable_sms=None, enable_email=None):
        """OpenNotifySetting - a model defined in huaweicloud sdk"""
        
        

        self._enable_calendar = None
        self._enable_sms = None
        self._enable_email = None
        self.discriminator = None

        self.enable_calendar = enable_calendar
        self.enable_sms = enable_sms
        self.enable_email = enable_email

    @property
    def enable_calendar(self):
        """Gets the enable_calendar of this OpenNotifySetting.

        发送邮件日历是否开启，\"Y\" 开启，\"N\" 不开启。

        :return: The enable_calendar of this OpenNotifySetting.
        :rtype: str
        """
        return self._enable_calendar

    @enable_calendar.setter
    def enable_calendar(self, enable_calendar):
        """Sets the enable_calendar of this OpenNotifySetting.

        发送邮件日历是否开启，\"Y\" 开启，\"N\" 不开启。

        :param enable_calendar: The enable_calendar of this OpenNotifySetting.
        :type: str
        """
        self._enable_calendar = enable_calendar

    @property
    def enable_sms(self):
        """Gets the enable_sms of this OpenNotifySetting.

        短信通知是否开启，\"Y\" 开启，\"N\" 不开启。

        :return: The enable_sms of this OpenNotifySetting.
        :rtype: str
        """
        return self._enable_sms

    @enable_sms.setter
    def enable_sms(self, enable_sms):
        """Sets the enable_sms of this OpenNotifySetting.

        短信通知是否开启，\"Y\" 开启，\"N\" 不开启。

        :param enable_sms: The enable_sms of this OpenNotifySetting.
        :type: str
        """
        self._enable_sms = enable_sms

    @property
    def enable_email(self):
        """Gets the enable_email of this OpenNotifySetting.

        短信通知是否开启，\"Y\" 开启，\"N\" 不开启。

        :return: The enable_email of this OpenNotifySetting.
        :rtype: str
        """
        return self._enable_email

    @enable_email.setter
    def enable_email(self, enable_email):
        """Sets the enable_email of this OpenNotifySetting.

        短信通知是否开启，\"Y\" 开启，\"N\" 不开启。

        :param enable_email: The enable_email of this OpenNotifySetting.
        :type: str
        """
        self._enable_email = enable_email

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OpenNotifySetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other