# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WordFluency:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'rhythm': 'float'
    }

    attribute_map = {
        'score': 'score',
        'rhythm': 'rhythm'
    }

    def __init__(self, score=None, rhythm=None):
        """WordFluency - a model defined in huaweicloud sdk"""
        
        

        self._score = None
        self._rhythm = None
        self.discriminator = None

        self.score = score
        self.rhythm = rhythm

    @property
    def score(self):
        """Gets the score of this WordFluency.

        

        :return: The score of this WordFluency.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this WordFluency.

        

        :param score: The score of this WordFluency.
        :type: float
        """
        self._score = score

    @property
    def rhythm(self):
        """Gets the rhythm of this WordFluency.

        

        :return: The rhythm of this WordFluency.
        :rtype: float
        """
        return self._rhythm

    @rhythm.setter
    def rhythm(self, rhythm):
        """Sets the rhythm of this WordFluency.

        

        :param rhythm: The rhythm of this WordFluency.
        :type: float
        """
        self._rhythm = rhythm

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WordFluency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other