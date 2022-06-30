# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'secrets': 'dict(str, str)'
    }

    attribute_map = {
        'description': 'description',
        'secrets': 'secrets'
    }

    def __init__(self, description=None, secrets=None):
        """UpdateSecretDetail

        The model defined in huaweicloud sdk

        :param description: 密钥描述,最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param secrets: secrets是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value必须为base64字符。 注：secrets字典的长度即字典转为标准的字符串后的长度，例如字典{\&quot;a\&quot;: \&quot;b\&quot;}转为标准字符串后为&#39;{\&quot;a\&quot;: \&quot;b\&quot;}&#39;，长度为10
        :type secrets: dict(str, str)
        """
        
        

        self._description = None
        self._secrets = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if secrets is not None:
            self.secrets = secrets

    @property
    def description(self):
        """Gets the description of this UpdateSecretDetail.

        密钥描述,最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this UpdateSecretDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSecretDetail.

        密钥描述,最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this UpdateSecretDetail.
        :type description: str
        """
        self._description = description

    @property
    def secrets(self):
        """Gets the secrets of this UpdateSecretDetail.

        secrets是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value必须为base64字符。 注：secrets字典的长度即字典转为标准的字符串后的长度，例如字典{\"a\": \"b\"}转为标准字符串后为'{\"a\": \"b\"}'，长度为10

        :return: The secrets of this UpdateSecretDetail.
        :rtype: dict(str, str)
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this UpdateSecretDetail.

        secrets是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value必须为base64字符。 注：secrets字典的长度即字典转为标准的字符串后的长度，例如字典{\"a\": \"b\"}转为标准字符串后为'{\"a\": \"b\"}'，长度为10

        :param secrets: The secrets of this UpdateSecretDetail.
        :type secrets: dict(str, str)
        """
        self._secrets = secrets

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
        if not isinstance(other, UpdateSecretDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
