# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class KeystoneValidateTokenResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'token': 'TokenResult',
        'x_subject_token': 'str'
    }

    attribute_map = {
        'token': 'token',
        'x_subject_token': 'X-Subject-Token'
    }

    def __init__(self, token=None, x_subject_token=None):
        """KeystoneValidateTokenResponse - a model defined in huaweicloud sdk"""
        
        super(KeystoneValidateTokenResponse, self).__init__()

        self._token = None
        self._x_subject_token = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if x_subject_token is not None:
            self.x_subject_token = x_subject_token

    @property
    def token(self):
        """Gets the token of this KeystoneValidateTokenResponse.


        :return: The token of this KeystoneValidateTokenResponse.
        :rtype: TokenResult
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this KeystoneValidateTokenResponse.


        :param token: The token of this KeystoneValidateTokenResponse.
        :type: TokenResult
        """
        self._token = token

    @property
    def x_subject_token(self):
        """Gets the x_subject_token of this KeystoneValidateTokenResponse.


        :return: The x_subject_token of this KeystoneValidateTokenResponse.
        :rtype: str
        """
        return self._x_subject_token

    @x_subject_token.setter
    def x_subject_token(self, x_subject_token):
        """Sets the x_subject_token of this KeystoneValidateTokenResponse.


        :param x_subject_token: The x_subject_token of this KeystoneValidateTokenResponse.
        :type: str
        """
        self._x_subject_token = x_subject_token

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
        if not isinstance(other, KeystoneValidateTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
