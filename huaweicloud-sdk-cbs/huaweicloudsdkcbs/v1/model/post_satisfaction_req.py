# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostSatisfactionReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'degree': 'int'
    }

    attribute_map = {
        'degree': 'degree'
    }

    def __init__(self, degree=None):
        """PostSatisfactionReq - a model defined in huaweicloud sdk"""
        
        

        self._degree = None
        self.discriminator = None

        self.degree = degree

    @property
    def degree(self):
        """Gets the degree of this PostSatisfactionReq.

        满意度评分，当前仅支持二级评分，1表示满意，-1表示不满意。

        :return: The degree of this PostSatisfactionReq.
        :rtype: int
        """
        return self._degree

    @degree.setter
    def degree(self, degree):
        """Sets the degree of this PostSatisfactionReq.

        满意度评分，当前仅支持二级评分，1表示满意，-1表示不满意。

        :param degree: The degree of this PostSatisfactionReq.
        :type: int
        """
        self._degree = degree

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
        if not isinstance(other, PostSatisfactionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other