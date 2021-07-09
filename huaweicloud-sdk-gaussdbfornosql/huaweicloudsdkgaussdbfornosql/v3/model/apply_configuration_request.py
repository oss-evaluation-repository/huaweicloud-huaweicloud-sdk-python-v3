# coding: utf-8

import re
import six





class ApplyConfigurationRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'config_id': 'str',
        'body': 'ApplyConfigurationRequestBody'
    }

    attribute_map = {
        'config_id': 'config_id',
        'body': 'body'
    }

    def __init__(self, config_id=None, body=None):
        """ApplyConfigurationRequest - a model defined in huaweicloud sdk"""
        
        

        self._config_id = None
        self._body = None
        self.discriminator = None

        self.config_id = config_id
        if body is not None:
            self.body = body

    @property
    def config_id(self):
        """Gets the config_id of this ApplyConfigurationRequest.

        参数模板ID。

        :return: The config_id of this ApplyConfigurationRequest.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this ApplyConfigurationRequest.

        参数模板ID。

        :param config_id: The config_id of this ApplyConfigurationRequest.
        :type: str
        """
        self._config_id = config_id

    @property
    def body(self):
        """Gets the body of this ApplyConfigurationRequest.


        :return: The body of this ApplyConfigurationRequest.
        :rtype: ApplyConfigurationRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ApplyConfigurationRequest.


        :param body: The body of this ApplyConfigurationRequest.
        :type: ApplyConfigurationRequestBody
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
        if not isinstance(other, ApplyConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
