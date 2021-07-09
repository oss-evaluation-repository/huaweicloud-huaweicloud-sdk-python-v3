# coding: utf-8

import re
import six





class ApplicationConfigModifyConfiguration:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'env': 'list[ApplicationConfigModifyConfigurationEnv]'
    }

    attribute_map = {
        'env': 'env'
    }

    def __init__(self, env=None):
        """ApplicationConfigModifyConfiguration - a model defined in huaweicloud sdk"""
        
        

        self._env = None
        self.discriminator = None

        self.env = env

    @property
    def env(self):
        """Gets the env of this ApplicationConfigModifyConfiguration.

        应用环境变量。

        :return: The env of this ApplicationConfigModifyConfiguration.
        :rtype: list[ApplicationConfigModifyConfigurationEnv]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this ApplicationConfigModifyConfiguration.

        应用环境变量。

        :param env: The env of this ApplicationConfigModifyConfiguration.
        :type: list[ApplicationConfigModifyConfigurationEnv]
        """
        self._env = env

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
        if not isinstance(other, ApplicationConfigModifyConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
