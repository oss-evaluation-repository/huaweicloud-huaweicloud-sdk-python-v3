# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoDailyCodeline:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'additions': 'int',
        'date': 'str',
        'deletions': 'int'
    }

    attribute_map = {
        'additions': 'additions',
        'date': 'date',
        'deletions': 'deletions'
    }

    def __init__(self, additions=None, date=None, deletions=None):
        """RepoDailyCodeline - a model defined in huaweicloud sdk"""
        
        

        self._additions = None
        self._date = None
        self._deletions = None
        self.discriminator = None

        if additions is not None:
            self.additions = additions
        if date is not None:
            self.date = date
        if deletions is not None:
            self.deletions = deletions

    @property
    def additions(self):
        """Gets the additions of this RepoDailyCodeline.

        每日增加代码行

        :return: The additions of this RepoDailyCodeline.
        :rtype: int
        """
        return self._additions

    @additions.setter
    def additions(self, additions):
        """Sets the additions of this RepoDailyCodeline.

        每日增加代码行

        :param additions: The additions of this RepoDailyCodeline.
        :type: int
        """
        self._additions = additions

    @property
    def date(self):
        """Gets the date of this RepoDailyCodeline.

        日期

        :return: The date of this RepoDailyCodeline.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this RepoDailyCodeline.

        日期

        :param date: The date of this RepoDailyCodeline.
        :type: str
        """
        self._date = date

    @property
    def deletions(self):
        """Gets the deletions of this RepoDailyCodeline.

        每日删除代码行

        :return: The deletions of this RepoDailyCodeline.
        :rtype: int
        """
        return self._deletions

    @deletions.setter
    def deletions(self, deletions):
        """Sets the deletions of this RepoDailyCodeline.

        每日删除代码行

        :param deletions: The deletions of this RepoDailyCodeline.
        :type: int
        """
        self._deletions = deletions

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
        if not isinstance(other, RepoDailyCodeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other