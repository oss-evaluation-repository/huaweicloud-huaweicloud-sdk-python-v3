# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistObjectIdDecryptDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'decrypt': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'decrypt': 'decrypt',
        'id': 'id'
    }

    def __init__(self, decrypt=None, id=None):
        """PersistObjectIdDecryptDTO

        The model defined in huaweicloud sdk

        :param decrypt: 是否加密。 - true：加密。 - false：不加密。
        :type decrypt: bool
        :param id: 唯一标识。
        :type id: str
        """
        
        

        self._decrypt = None
        self._id = None
        self.discriminator = None

        if decrypt is not None:
            self.decrypt = decrypt
        self.id = id

    @property
    def decrypt(self):
        """Gets the decrypt of this PersistObjectIdDecryptDTO.

        是否加密。 - true：加密。 - false：不加密。

        :return: The decrypt of this PersistObjectIdDecryptDTO.
        :rtype: bool
        """
        return self._decrypt

    @decrypt.setter
    def decrypt(self, decrypt):
        """Sets the decrypt of this PersistObjectIdDecryptDTO.

        是否加密。 - true：加密。 - false：不加密。

        :param decrypt: The decrypt of this PersistObjectIdDecryptDTO.
        :type decrypt: bool
        """
        self._decrypt = decrypt

    @property
    def id(self):
        """Gets the id of this PersistObjectIdDecryptDTO.

        唯一标识。

        :return: The id of this PersistObjectIdDecryptDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PersistObjectIdDecryptDTO.

        唯一标识。

        :param id: The id of this PersistObjectIdDecryptDTO.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, PersistObjectIdDecryptDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
