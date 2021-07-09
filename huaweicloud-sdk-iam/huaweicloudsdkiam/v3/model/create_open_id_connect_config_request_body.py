# coding: utf-8

import re
import six





class CreateOpenIdConnectConfigRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'openid_connect_config': 'CreateOpenIdConnectConfig'
    }

    attribute_map = {
        'openid_connect_config': 'openid_connect_config'
    }

    def __init__(self, openid_connect_config=None):
        """CreateOpenIdConnectConfigRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._openid_connect_config = None
        self.discriminator = None

        self.openid_connect_config = openid_connect_config

    @property
    def openid_connect_config(self):
        """Gets the openid_connect_config of this CreateOpenIdConnectConfigRequestBody.


        :return: The openid_connect_config of this CreateOpenIdConnectConfigRequestBody.
        :rtype: CreateOpenIdConnectConfig
        """
        return self._openid_connect_config

    @openid_connect_config.setter
    def openid_connect_config(self, openid_connect_config):
        """Sets the openid_connect_config of this CreateOpenIdConnectConfigRequestBody.


        :param openid_connect_config: The openid_connect_config of this CreateOpenIdConnectConfigRequestBody.
        :type: CreateOpenIdConnectConfig
        """
        self._openid_connect_config = openid_connect_config

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
        if not isinstance(other, CreateOpenIdConnectConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
