# coding: utf-8

import re
import six





class DisableKeyRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'version_id': 'str',
        'body': 'OperateKeyRequestBody'
    }

    attribute_map = {
        'version_id': 'version_id',
        'body': 'body'
    }

    def __init__(self, version_id=None, body=None):
        """DisableKeyRequest - a model defined in huaweicloud sdk"""
        
        

        self._version_id = None
        self._body = None
        self.discriminator = None

        self.version_id = version_id
        if body is not None:
            self.body = body

    @property
    def version_id(self):
        """Gets the version_id of this DisableKeyRequest.

        API版本号

        :return: The version_id of this DisableKeyRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this DisableKeyRequest.

        API版本号

        :param version_id: The version_id of this DisableKeyRequest.
        :type: str
        """
        self._version_id = version_id

    @property
    def body(self):
        """Gets the body of this DisableKeyRequest.


        :return: The body of this DisableKeyRequest.
        :rtype: OperateKeyRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DisableKeyRequest.


        :param body: The body of this DisableKeyRequest.
        :type: OperateKeyRequestBody
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
        if not isinstance(other, DisableKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
