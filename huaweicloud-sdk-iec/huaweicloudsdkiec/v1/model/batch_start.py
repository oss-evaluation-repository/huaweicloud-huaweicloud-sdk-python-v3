# coding: utf-8

import re
import six





class BatchStart:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'servers': 'list[BaseId]'
    }

    attribute_map = {
        'servers': 'servers'
    }

    def __init__(self, servers=None):
        """BatchStart - a model defined in huaweicloud sdk"""
        
        

        self._servers = None
        self.discriminator = None

        if servers is not None:
            self.servers = servers

    @property
    def servers(self):
        """Gets the servers of this BatchStart.

        待启动的边缘实例列表。

        :return: The servers of this BatchStart.
        :rtype: list[BaseId]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this BatchStart.

        待启动的边缘实例列表。

        :param servers: The servers of this BatchStart.
        :type: list[BaseId]
        """
        self._servers = servers

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
        if not isinstance(other, BatchStart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
