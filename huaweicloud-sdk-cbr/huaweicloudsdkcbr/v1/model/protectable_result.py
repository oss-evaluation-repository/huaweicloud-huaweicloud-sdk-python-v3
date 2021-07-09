# coding: utf-8

import re
import six





class ProtectableResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'reason': 'str',
        'result': 'str',
        'vault': 'VaultGet'
    }

    attribute_map = {
        'code': 'code',
        'reason': 'reason',
        'result': 'result',
        'vault': 'vault'
    }

    def __init__(self, code=None, reason=None, result=None, vault=None):
        """ProtectableResult - a model defined in huaweicloud sdk"""
        
        

        self._code = None
        self._reason = None
        self._result = None
        self._vault = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if reason is not None:
            self.reason = reason
        self.result = result
        if vault is not None:
            self.vault = vault

    @property
    def code(self):
        """Gets the code of this ProtectableResult.

        不支持备份的错误码

        :return: The code of this ProtectableResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ProtectableResult.

        不支持备份的错误码

        :param code: The code of this ProtectableResult.
        :type: str
        """
        self._code = code

    @property
    def reason(self):
        """Gets the reason of this ProtectableResult.

        不支持备份的原因

        :return: The reason of this ProtectableResult.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ProtectableResult.

        不支持备份的原因

        :param reason: The reason of this ProtectableResult.
        :type: str
        """
        self._reason = reason

    @property
    def result(self):
        """Gets the result of this ProtectableResult.

        是否可备份

        :return: The result of this ProtectableResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ProtectableResult.

        是否可备份

        :param result: The result of this ProtectableResult.
        :type: str
        """
        self._result = result

    @property
    def vault(self):
        """Gets the vault of this ProtectableResult.


        :return: The vault of this ProtectableResult.
        :rtype: VaultGet
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        """Sets the vault of this ProtectableResult.


        :param vault: The vault of this ProtectableResult.
        :type: VaultGet
        """
        self._vault = vault

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
        if not isinstance(other, ProtectableResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
