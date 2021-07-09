# coding: utf-8

import re
import six





class UpdateNatGatewayRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'nat_gateway': 'UpdateNatGatewayOption'
    }

    attribute_map = {
        'nat_gateway': 'nat_gateway'
    }

    def __init__(self, nat_gateway=None):
        """UpdateNatGatewayRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._nat_gateway = None
        self.discriminator = None

        self.nat_gateway = nat_gateway

    @property
    def nat_gateway(self):
        """Gets the nat_gateway of this UpdateNatGatewayRequestBody.


        :return: The nat_gateway of this UpdateNatGatewayRequestBody.
        :rtype: UpdateNatGatewayOption
        """
        return self._nat_gateway

    @nat_gateway.setter
    def nat_gateway(self, nat_gateway):
        """Sets the nat_gateway of this UpdateNatGatewayRequestBody.


        :param nat_gateway: The nat_gateway of this UpdateNatGatewayRequestBody.
        :type: UpdateNatGatewayOption
        """
        self._nat_gateway = nat_gateway

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
        if not isinstance(other, UpdateNatGatewayRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
