# coding: utf-8

import re
import six





class VaultUpdateReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vault': 'VaultUpdate'
    }

    attribute_map = {
        'vault': 'vault'
    }

    def __init__(self, vault=None):
        """VaultUpdateReq - a model defined in huaweicloud sdk"""
        
        

        self._vault = None
        self.discriminator = None

        self.vault = vault

    @property
    def vault(self):
        """Gets the vault of this VaultUpdateReq.


        :return: The vault of this VaultUpdateReq.
        :rtype: VaultUpdate
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        """Sets the vault of this VaultUpdateReq.


        :param vault: The vault of this VaultUpdateReq.
        :type: VaultUpdate
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
        if not isinstance(other, VaultUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
