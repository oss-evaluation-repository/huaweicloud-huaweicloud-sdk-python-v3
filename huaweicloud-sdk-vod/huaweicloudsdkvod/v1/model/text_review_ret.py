# coding: utf-8

import re
import six





class TextReviewRet:


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
        'politics': 'str',
        'porn': 'str',
        'abuse': 'str'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'politics': 'politics',
        'porn': 'porn',
        'abuse': 'abuse'
    }

    def __init__(self, suggestion=None, politics=None, porn=None, abuse=None):
        """TextReviewRet - a model defined in huaweicloud sdk"""
        
        

        self._suggestion = None
        self._politics = None
        self._porn = None
        self._abuse = None
        self.discriminator = None

        self.suggestion = suggestion
        if politics is not None:
            self.politics = politics
        if porn is not None:
            self.porn = porn
        if abuse is not None:
            self.abuse = abuse

    @property
    def suggestion(self):
        """Gets the suggestion of this TextReviewRet.

        检测结果是否通过。  取值如下： - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过。 - review：需要人工复检。

        :return: The suggestion of this TextReviewRet.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this TextReviewRet.

        检测结果是否通过。  取值如下： - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过。 - review：需要人工复检。

        :param suggestion: The suggestion of this TextReviewRet.
        :type: str
        """
        self._suggestion = suggestion

    @property
    def politics(self):
        """Gets the politics of this TextReviewRet.

        涉政敏感词列表

        :return: The politics of this TextReviewRet.
        :rtype: str
        """
        return self._politics

    @politics.setter
    def politics(self, politics):
        """Sets the politics of this TextReviewRet.

        涉政敏感词列表

        :param politics: The politics of this TextReviewRet.
        :type: str
        """
        self._politics = politics

    @property
    def porn(self):
        """Gets the porn of this TextReviewRet.

        涉黄敏感词列表

        :return: The porn of this TextReviewRet.
        :rtype: str
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        """Sets the porn of this TextReviewRet.

        涉黄敏感词列表

        :param porn: The porn of this TextReviewRet.
        :type: str
        """
        self._porn = porn

    @property
    def abuse(self):
        """Gets the abuse of this TextReviewRet.

        辱骂敏感词列表

        :return: The abuse of this TextReviewRet.
        :rtype: str
        """
        return self._abuse

    @abuse.setter
    def abuse(self, abuse):
        """Sets the abuse of this TextReviewRet.

        辱骂敏感词列表

        :param abuse: The abuse of this TextReviewRet.
        :type: str
        """
        self._abuse = abuse

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
        if not isinstance(other, TextReviewRet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
