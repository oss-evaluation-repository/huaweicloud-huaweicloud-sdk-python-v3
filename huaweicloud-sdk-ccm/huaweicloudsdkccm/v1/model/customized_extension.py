# coding: utf-8

import re
import six





class CustomizedExtension:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'object_identifier': 'str',
        'value': 'str'
    }

    attribute_map = {
        'object_identifier': 'object_identifier',
        'value': 'value'
    }

    def __init__(self, object_identifier=None, value=None):
        """CustomizedExtension - a model defined in huaweicloud sdk"""
        
        

        self._object_identifier = None
        self._value = None
        self.discriminator = None

        if object_identifier is not None:
            self.object_identifier = object_identifier
        if value is not None:
            self.value = value

    @property
    def object_identifier(self):
        """Gets the object_identifier of this CustomizedExtension.

        对象标识符

        :return: The object_identifier of this CustomizedExtension.
        :rtype: str
        """
        return self._object_identifier

    @object_identifier.setter
    def object_identifier(self, object_identifier):
        """Sets the object_identifier of this CustomizedExtension.

        对象标识符

        :param object_identifier: The object_identifier of this CustomizedExtension.
        :type: str
        """
        self._object_identifier = object_identifier

    @property
    def value(self):
        """Gets the value of this CustomizedExtension.

        自定义属性内容

        :return: The value of this CustomizedExtension.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomizedExtension.

        自定义属性内容

        :param value: The value of this CustomizedExtension.
        :type: str
        """
        self._value = value

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
        if not isinstance(other, CustomizedExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other