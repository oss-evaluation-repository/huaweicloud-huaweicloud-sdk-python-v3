# coding: utf-8

import pprint
import re

import six





class ImageModerationResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'suggestion': 'str',
        'category_suggestions': 'CategorySuggestions'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'category_suggestions': 'category_suggestions'
    }

    def __init__(self, suggestion=None, category_suggestions=None):
        """ImageModerationResult - a model defined in huaweicloud sdk"""
        
        

        self._suggestion = None
        self._category_suggestions = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if category_suggestions is not None:
            self.category_suggestions = category_suggestions

    @property
    def suggestion(self):
        """Gets the suggestion of this ImageModerationResult.

        审核情况

        :return: The suggestion of this ImageModerationResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ImageModerationResult.

        审核情况

        :param suggestion: The suggestion of this ImageModerationResult.
        :type: str
        """
        self._suggestion = suggestion

    @property
    def category_suggestions(self):
        """Gets the category_suggestions of this ImageModerationResult.


        :return: The category_suggestions of this ImageModerationResult.
        :rtype: CategorySuggestions
        """
        return self._category_suggestions

    @category_suggestions.setter
    def category_suggestions(self, category_suggestions):
        """Sets the category_suggestions of this ImageModerationResult.


        :param category_suggestions: The category_suggestions of this ImageModerationResult.
        :type: CategorySuggestions
        """
        self._category_suggestions = category_suggestions

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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageModerationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other