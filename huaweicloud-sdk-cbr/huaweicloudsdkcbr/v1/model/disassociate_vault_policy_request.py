# coding: utf-8

import re
import six





class DisassociateVaultPolicyRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vault_id': 'str',
        'body': 'VaultDissociate'
    }

    attribute_map = {
        'vault_id': 'vault_id',
        'body': 'body'
    }

    def __init__(self, vault_id=None, body=None):
        """DisassociateVaultPolicyRequest - a model defined in huaweicloud sdk"""
        
        

        self._vault_id = None
        self._body = None
        self.discriminator = None

        self.vault_id = vault_id
        if body is not None:
            self.body = body

    @property
    def vault_id(self):
        """Gets the vault_id of this DisassociateVaultPolicyRequest.

        存储库ID

        :return: The vault_id of this DisassociateVaultPolicyRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this DisassociateVaultPolicyRequest.

        存储库ID

        :param vault_id: The vault_id of this DisassociateVaultPolicyRequest.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def body(self):
        """Gets the body of this DisassociateVaultPolicyRequest.


        :return: The body of this DisassociateVaultPolicyRequest.
        :rtype: VaultDissociate
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DisassociateVaultPolicyRequest.


        :param body: The body of this DisassociateVaultPolicyRequest.
        :type: VaultDissociate
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DisassociateVaultPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
