# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'secret_name': 'str',
        'body': 'UpdateSecretRequestBody'
    }

    attribute_map = {
        'secret_name': 'secret_name',
        'body': 'body'
    }

    def __init__(self, secret_name=None, body=None):
        """UpdateSecretRequest - a model defined in huaweicloud sdk"""
        
        

        self._secret_name = None
        self._body = None
        self.discriminator = None

        self.secret_name = secret_name
        if body is not None:
            self.body = body

    @property
    def secret_name(self):
        """Gets the secret_name of this UpdateSecretRequest.

        凭据名称。

        :return: The secret_name of this UpdateSecretRequest.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this UpdateSecretRequest.

        凭据名称。

        :param secret_name: The secret_name of this UpdateSecretRequest.
        :type: str
        """
        self._secret_name = secret_name

    @property
    def body(self):
        """Gets the body of this UpdateSecretRequest.


        :return: The body of this UpdateSecretRequest.
        :rtype: UpdateSecretRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSecretRequest.


        :param body: The body of this UpdateSecretRequest.
        :type: UpdateSecretRequestBody
        """
        self._body = body

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateSecretRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
