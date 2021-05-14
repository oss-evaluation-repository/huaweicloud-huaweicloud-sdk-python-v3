# coding: utf-8

import pprint
import re

import six





class CreateSecretVersionRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'secret_binary': 'str',
        'secret_string': 'str',
        'version_stages': 'list[str]'
    }

    attribute_map = {
        'secret_binary': 'secret_binary',
        'secret_string': 'secret_string',
        'version_stages': 'version_stages'
    }

    def __init__(self, secret_binary=None, secret_string=None, version_stages=None):
        """CreateSecretVersionRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._secret_binary = None
        self._secret_string = None
        self._version_stages = None
        self.discriminator = None

        if secret_binary is not None:
            self.secret_binary = secret_binary
        if secret_string is not None:
            self.secret_string = secret_string
        if version_stages is not None:
            self.version_stages = version_stages

    @property
    def secret_binary(self):
        """Gets the secret_binary of this CreateSecretVersionRequestBody.

        新创建凭据的凭据值，将其加密后，存入初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 

        :return: The secret_binary of this CreateSecretVersionRequestBody.
        :rtype: str
        """
        return self._secret_binary

    @secret_binary.setter
    def secret_binary(self, secret_binary):
        """Sets the secret_binary of this CreateSecretVersionRequestBody.

        新创建凭据的凭据值，将其加密后，存入初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 

        :param secret_binary: The secret_binary of this CreateSecretVersionRequestBody.
        :type: str
        """
        self._secret_binary = secret_binary

    @property
    def secret_string(self):
        """Gets the secret_string of this CreateSecretVersionRequestBody.

        新创建凭据的凭据值，将其加密后，存入初始版本中。  约束：secret_binary和 secret_string必须且只能设置一个，最大32K。 

        :return: The secret_string of this CreateSecretVersionRequestBody.
        :rtype: str
        """
        return self._secret_string

    @secret_string.setter
    def secret_string(self, secret_string):
        """Sets the secret_string of this CreateSecretVersionRequestBody.

        新创建凭据的凭据值，将其加密后，存入初始版本中。  约束：secret_binary和 secret_string必须且只能设置一个，最大32K。 

        :param secret_string: The secret_string of this CreateSecretVersionRequestBody.
        :type: str
        """
        self._secret_string = secret_string

    @property
    def version_stages(self):
        """Gets the version_stages of this CreateSecretVersionRequestBody.

        凭据版本在存入时需要被同时标记的版本状态。如果您不指定此参数，凭据管家默认为新版本标记SYSCURRENT  约束：数组大小：最小1，最大12。stage长度：最小1字节，最大64字节。 

        :return: The version_stages of this CreateSecretVersionRequestBody.
        :rtype: list[str]
        """
        return self._version_stages

    @version_stages.setter
    def version_stages(self, version_stages):
        """Sets the version_stages of this CreateSecretVersionRequestBody.

        凭据版本在存入时需要被同时标记的版本状态。如果您不指定此参数，凭据管家默认为新版本标记SYSCURRENT  约束：数组大小：最小1，最大12。stage长度：最小1字节，最大64字节。 

        :param version_stages: The version_stages of this CreateSecretVersionRequestBody.
        :type: list[str]
        """
        self._version_stages = version_stages

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
        if not isinstance(other, CreateSecretVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other