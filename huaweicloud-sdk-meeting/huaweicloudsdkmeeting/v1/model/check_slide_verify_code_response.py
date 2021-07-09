# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CheckSlideVerifyCodeResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'token': 'str',
        'expire': 'int'
    }

    attribute_map = {
        'token': 'token',
        'expire': 'expire'
    }

    def __init__(self, token=None, expire=None):
        """CheckSlideVerifyCodeResponse - a model defined in huaweicloud sdk"""
        
        super(CheckSlideVerifyCodeResponse, self).__init__()

        self._token = None
        self._expire = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if expire is not None:
            self.expire = expire

    @property
    def token(self):
        """Gets the token of this CheckSlideVerifyCodeResponse.

        访问token字符串

        :return: The token of this CheckSlideVerifyCodeResponse.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CheckSlideVerifyCodeResponse.

        访问token字符串

        :param token: The token of this CheckSlideVerifyCodeResponse.
        :type: str
        """
        self._token = token

    @property
    def expire(self):
        """Gets the expire of this CheckSlideVerifyCodeResponse.

        过期时间，单位：秒

        :return: The expire of this CheckSlideVerifyCodeResponse.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """Sets the expire of this CheckSlideVerifyCodeResponse.

        过期时间，单位：秒

        :param expire: The expire of this CheckSlideVerifyCodeResponse.
        :type: int
        """
        self._expire = expire

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
        if not isinstance(other, CheckSlideVerifyCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
