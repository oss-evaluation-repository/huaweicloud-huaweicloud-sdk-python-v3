# coding: utf-8

import re
import six





class CreateCcRuleRequestBodyAction:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'category': 'str'
    }

    attribute_map = {
        'category': 'category'
    }

    def __init__(self, category=None):
        """CreateCcRuleRequestBodyAction - a model defined in huaweicloud sdk"""
        
        

        self._category = None
        self.discriminator = None

        if category is not None:
            self.category = category

    @property
    def category(self):
        """Gets the category of this CreateCcRuleRequestBodyAction.

        防护动作

        :return: The category of this CreateCcRuleRequestBodyAction.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CreateCcRuleRequestBodyAction.

        防护动作

        :param category: The category of this CreateCcRuleRequestBodyAction.
        :type: str
        """
        self._category = category

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
        if not isinstance(other, CreateCcRuleRequestBodyAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
