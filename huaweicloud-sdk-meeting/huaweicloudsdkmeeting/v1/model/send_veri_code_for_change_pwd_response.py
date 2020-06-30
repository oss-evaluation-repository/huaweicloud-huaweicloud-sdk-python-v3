# coding: utf-8

import pprint
import re

import six


class SendVeriCodeForChangePwdResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'expire': 'int',
        'bind_phone': 'str',
        'bind_email': 'str'
    }

    attribute_map = {
        'expire': 'expire',
        'bind_phone': 'bindPhone',
        'bind_email': 'bindEmail'
    }

    def __init__(self, expire=None, bind_phone=None, bind_email=None):  # noqa: E501
        """SendVeriCodeForChangePwdResponse - a model defined in huaweicloud sdk"""

        self._expire = None
        self._bind_phone = None
        self._bind_email = None
        self.discriminator = None

        if expire is not None:
            self.expire = expire
        if bind_phone is not None:
            self.bind_phone = bind_phone
        if bind_email is not None:
            self.bind_email = bind_email

    @property
    def expire(self):
        """Gets the expire of this SendVeriCodeForChangePwdResponse.

        过期时间，单位：秒。

        :return: The expire of this SendVeriCodeForChangePwdResponse.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """Sets the expire of this SendVeriCodeForChangePwdResponse.

        过期时间，单位：秒。

        :param expire: The expire of this SendVeriCodeForChangePwdResponse.
        :type: int
        """
        self._expire = expire

    @property
    def bind_phone(self):
        """Gets the bind_phone of this SendVeriCodeForChangePwdResponse.

        如果通过手机发送验证码，则该字段携带该用户绑定的手机号（手机号经过处理，屏蔽中间几位，如+8618****12345）

        :return: The bind_phone of this SendVeriCodeForChangePwdResponse.
        :rtype: str
        """
        return self._bind_phone

    @bind_phone.setter
    def bind_phone(self, bind_phone):
        """Sets the bind_phone of this SendVeriCodeForChangePwdResponse.

        如果通过手机发送验证码，则该字段携带该用户绑定的手机号（手机号经过处理，屏蔽中间几位，如+8618****12345）

        :param bind_phone: The bind_phone of this SendVeriCodeForChangePwdResponse.
        :type: str
        """
        self._bind_phone = bind_phone

    @property
    def bind_email(self):
        """Gets the bind_email of this SendVeriCodeForChangePwdResponse.

        如果通过邮箱发送验证码，则该字段携带用户绑定的邮箱账号（邮箱账号经过处理，屏蔽中间几位，如tes****ount@huawei.com）

        :return: The bind_email of this SendVeriCodeForChangePwdResponse.
        :rtype: str
        """
        return self._bind_email

    @bind_email.setter
    def bind_email(self, bind_email):
        """Sets the bind_email of this SendVeriCodeForChangePwdResponse.

        如果通过邮箱发送验证码，则该字段携带用户绑定的邮箱账号（邮箱账号经过处理，屏蔽中间几位，如tes****ount@huawei.com）

        :param bind_email: The bind_email of this SendVeriCodeForChangePwdResponse.
        :type: str
        """
        self._bind_email = bind_email

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
        if not isinstance(other, SendVeriCodeForChangePwdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other