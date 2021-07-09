# coding: utf-8

import re
import six





class CreateListenerRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'listener': 'CreateListenerReq'
    }

    attribute_map = {
        'listener': 'listener'
    }

    def __init__(self, listener=None):
        """CreateListenerRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._listener = None
        self.discriminator = None

        self.listener = listener

    @property
    def listener(self):
        """Gets the listener of this CreateListenerRequestBody.


        :return: The listener of this CreateListenerRequestBody.
        :rtype: CreateListenerReq
        """
        return self._listener

    @listener.setter
    def listener(self, listener):
        """Sets the listener of this CreateListenerRequestBody.


        :param listener: The listener of this CreateListenerRequestBody.
        :type: CreateListenerReq
        """
        self._listener = listener

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
        if not isinstance(other, CreateListenerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
