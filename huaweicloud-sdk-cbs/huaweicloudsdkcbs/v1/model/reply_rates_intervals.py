# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplyRatesIntervals:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start': 'str',
        'question_count': 'int',
        'direct_count': 'int',
        'recommend_count': 'int',
        'notmatch_count': 'int',
        'invalid_count': 'int',
        'chat_count': 'int',
        'direct_rate': 'float',
        'recommend_rate': 'float',
        'notmatch_rate': 'float',
        'chat_rate': 'float',
        'invalid_rate': 'float',
        'dialog_count': 'int',
        'dialog_rate': 'float'
    }

    attribute_map = {
        'start': 'start',
        'question_count': 'question_count',
        'direct_count': 'direct_count',
        'recommend_count': 'recommend_count',
        'notmatch_count': 'notmatch_count',
        'invalid_count': 'invalid_count',
        'chat_count': 'chat_count',
        'direct_rate': 'direct_rate',
        'recommend_rate': 'recommend_rate',
        'notmatch_rate': 'notmatch_rate',
        'chat_rate': 'chat_rate',
        'invalid_rate': 'invalid_rate',
        'dialog_count': 'dialog_count',
        'dialog_rate': 'dialog_rate'
    }

    def __init__(self, start=None, question_count=None, direct_count=None, recommend_count=None, notmatch_count=None, invalid_count=None, chat_count=None, direct_rate=None, recommend_rate=None, notmatch_rate=None, chat_rate=None, invalid_rate=None, dialog_count=None, dialog_rate=None):
        """ReplyRatesIntervals

        The model defined in huaweicloud sdk

        :param start: 间隔周期开始时间。
        :type start: str
        :param question_count: 间隔周期用户提问总数。
        :type question_count: int
        :param direct_count: 间隔周期直接回答个数。
        :type direct_count: int
        :param recommend_count: 间隔周期推荐回答个数。
        :type recommend_count: int
        :param notmatch_count: 间隔周期未匹配个数。
        :type notmatch_count: int
        :param invalid_count: 间隔周期无效问题个数。
        :type invalid_count: int
        :param chat_count: 间隔周期闲聊匹配个数。
        :type chat_count: int
        :param direct_rate: 间隔周期直接回答比率，保留小数点后三位。
        :type direct_rate: float
        :param recommend_rate: 间隔周期推荐回答比率，保留小数点后三位。
        :type recommend_rate: float
        :param notmatch_rate: 间隔周期未匹配比率，保留小数点后三位。
        :type notmatch_rate: float
        :param chat_rate: 间隔周期闲聊匹配比率，保留小数点后三位。
        :type chat_rate: float
        :param invalid_rate: 间隔周期无效问题比率，保留小数点后三位。
        :type invalid_rate: float
        :param dialog_count: 多轮会话次数。
        :type dialog_count: int
        :param dialog_rate: 多轮会话比例。
        :type dialog_rate: float
        """
        
        

        self._start = None
        self._question_count = None
        self._direct_count = None
        self._recommend_count = None
        self._notmatch_count = None
        self._invalid_count = None
        self._chat_count = None
        self._direct_rate = None
        self._recommend_rate = None
        self._notmatch_rate = None
        self._chat_rate = None
        self._invalid_rate = None
        self._dialog_count = None
        self._dialog_rate = None
        self.discriminator = None

        self.start = start
        self.question_count = question_count
        self.direct_count = direct_count
        self.recommend_count = recommend_count
        self.notmatch_count = notmatch_count
        self.invalid_count = invalid_count
        self.chat_count = chat_count
        self.direct_rate = direct_rate
        self.recommend_rate = recommend_rate
        self.notmatch_rate = notmatch_rate
        self.chat_rate = chat_rate
        self.invalid_rate = invalid_rate
        self.dialog_count = dialog_count
        self.dialog_rate = dialog_rate

    @property
    def start(self):
        """Gets the start of this ReplyRatesIntervals.

        间隔周期开始时间。

        :return: The start of this ReplyRatesIntervals.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ReplyRatesIntervals.

        间隔周期开始时间。

        :param start: The start of this ReplyRatesIntervals.
        :type start: str
        """
        self._start = start

    @property
    def question_count(self):
        """Gets the question_count of this ReplyRatesIntervals.

        间隔周期用户提问总数。

        :return: The question_count of this ReplyRatesIntervals.
        :rtype: int
        """
        return self._question_count

    @question_count.setter
    def question_count(self, question_count):
        """Sets the question_count of this ReplyRatesIntervals.

        间隔周期用户提问总数。

        :param question_count: The question_count of this ReplyRatesIntervals.
        :type question_count: int
        """
        self._question_count = question_count

    @property
    def direct_count(self):
        """Gets the direct_count of this ReplyRatesIntervals.

        间隔周期直接回答个数。

        :return: The direct_count of this ReplyRatesIntervals.
        :rtype: int
        """
        return self._direct_count

    @direct_count.setter
    def direct_count(self, direct_count):
        """Sets the direct_count of this ReplyRatesIntervals.

        间隔周期直接回答个数。

        :param direct_count: The direct_count of this ReplyRatesIntervals.
        :type direct_count: int
        """
        self._direct_count = direct_count

    @property
    def recommend_count(self):
        """Gets the recommend_count of this ReplyRatesIntervals.

        间隔周期推荐回答个数。

        :return: The recommend_count of this ReplyRatesIntervals.
        :rtype: int
        """
        return self._recommend_count

    @recommend_count.setter
    def recommend_count(self, recommend_count):
        """Sets the recommend_count of this ReplyRatesIntervals.

        间隔周期推荐回答个数。

        :param recommend_count: The recommend_count of this ReplyRatesIntervals.
        :type recommend_count: int
        """
        self._recommend_count = recommend_count

    @property
    def notmatch_count(self):
        """Gets the notmatch_count of this ReplyRatesIntervals.

        间隔周期未匹配个数。

        :return: The notmatch_count of this ReplyRatesIntervals.
        :rtype: int
        """
        return self._notmatch_count

    @notmatch_count.setter
    def notmatch_count(self, notmatch_count):
        """Sets the notmatch_count of this ReplyRatesIntervals.

        间隔周期未匹配个数。

        :param notmatch_count: The notmatch_count of this ReplyRatesIntervals.
        :type notmatch_count: int
        """
        self._notmatch_count = notmatch_count

    @property
    def invalid_count(self):
        """Gets the invalid_count of this ReplyRatesIntervals.

        间隔周期无效问题个数。

        :return: The invalid_count of this ReplyRatesIntervals.
        :rtype: int
        """
        return self._invalid_count

    @invalid_count.setter
    def invalid_count(self, invalid_count):
        """Sets the invalid_count of this ReplyRatesIntervals.

        间隔周期无效问题个数。

        :param invalid_count: The invalid_count of this ReplyRatesIntervals.
        :type invalid_count: int
        """
        self._invalid_count = invalid_count

    @property
    def chat_count(self):
        """Gets the chat_count of this ReplyRatesIntervals.

        间隔周期闲聊匹配个数。

        :return: The chat_count of this ReplyRatesIntervals.
        :rtype: int
        """
        return self._chat_count

    @chat_count.setter
    def chat_count(self, chat_count):
        """Sets the chat_count of this ReplyRatesIntervals.

        间隔周期闲聊匹配个数。

        :param chat_count: The chat_count of this ReplyRatesIntervals.
        :type chat_count: int
        """
        self._chat_count = chat_count

    @property
    def direct_rate(self):
        """Gets the direct_rate of this ReplyRatesIntervals.

        间隔周期直接回答比率，保留小数点后三位。

        :return: The direct_rate of this ReplyRatesIntervals.
        :rtype: float
        """
        return self._direct_rate

    @direct_rate.setter
    def direct_rate(self, direct_rate):
        """Sets the direct_rate of this ReplyRatesIntervals.

        间隔周期直接回答比率，保留小数点后三位。

        :param direct_rate: The direct_rate of this ReplyRatesIntervals.
        :type direct_rate: float
        """
        self._direct_rate = direct_rate

    @property
    def recommend_rate(self):
        """Gets the recommend_rate of this ReplyRatesIntervals.

        间隔周期推荐回答比率，保留小数点后三位。

        :return: The recommend_rate of this ReplyRatesIntervals.
        :rtype: float
        """
        return self._recommend_rate

    @recommend_rate.setter
    def recommend_rate(self, recommend_rate):
        """Sets the recommend_rate of this ReplyRatesIntervals.

        间隔周期推荐回答比率，保留小数点后三位。

        :param recommend_rate: The recommend_rate of this ReplyRatesIntervals.
        :type recommend_rate: float
        """
        self._recommend_rate = recommend_rate

    @property
    def notmatch_rate(self):
        """Gets the notmatch_rate of this ReplyRatesIntervals.

        间隔周期未匹配比率，保留小数点后三位。

        :return: The notmatch_rate of this ReplyRatesIntervals.
        :rtype: float
        """
        return self._notmatch_rate

    @notmatch_rate.setter
    def notmatch_rate(self, notmatch_rate):
        """Sets the notmatch_rate of this ReplyRatesIntervals.

        间隔周期未匹配比率，保留小数点后三位。

        :param notmatch_rate: The notmatch_rate of this ReplyRatesIntervals.
        :type notmatch_rate: float
        """
        self._notmatch_rate = notmatch_rate

    @property
    def chat_rate(self):
        """Gets the chat_rate of this ReplyRatesIntervals.

        间隔周期闲聊匹配比率，保留小数点后三位。

        :return: The chat_rate of this ReplyRatesIntervals.
        :rtype: float
        """
        return self._chat_rate

    @chat_rate.setter
    def chat_rate(self, chat_rate):
        """Sets the chat_rate of this ReplyRatesIntervals.

        间隔周期闲聊匹配比率，保留小数点后三位。

        :param chat_rate: The chat_rate of this ReplyRatesIntervals.
        :type chat_rate: float
        """
        self._chat_rate = chat_rate

    @property
    def invalid_rate(self):
        """Gets the invalid_rate of this ReplyRatesIntervals.

        间隔周期无效问题比率，保留小数点后三位。

        :return: The invalid_rate of this ReplyRatesIntervals.
        :rtype: float
        """
        return self._invalid_rate

    @invalid_rate.setter
    def invalid_rate(self, invalid_rate):
        """Sets the invalid_rate of this ReplyRatesIntervals.

        间隔周期无效问题比率，保留小数点后三位。

        :param invalid_rate: The invalid_rate of this ReplyRatesIntervals.
        :type invalid_rate: float
        """
        self._invalid_rate = invalid_rate

    @property
    def dialog_count(self):
        """Gets the dialog_count of this ReplyRatesIntervals.

        多轮会话次数。

        :return: The dialog_count of this ReplyRatesIntervals.
        :rtype: int
        """
        return self._dialog_count

    @dialog_count.setter
    def dialog_count(self, dialog_count):
        """Sets the dialog_count of this ReplyRatesIntervals.

        多轮会话次数。

        :param dialog_count: The dialog_count of this ReplyRatesIntervals.
        :type dialog_count: int
        """
        self._dialog_count = dialog_count

    @property
    def dialog_rate(self):
        """Gets the dialog_rate of this ReplyRatesIntervals.

        多轮会话比例。

        :return: The dialog_rate of this ReplyRatesIntervals.
        :rtype: float
        """
        return self._dialog_rate

    @dialog_rate.setter
    def dialog_rate(self, dialog_rate):
        """Sets the dialog_rate of this ReplyRatesIntervals.

        多轮会话比例。

        :param dialog_rate: The dialog_rate of this ReplyRatesIntervals.
        :type dialog_rate: float
        """
        self._dialog_rate = dialog_rate

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
        if not isinstance(other, ReplyRatesIntervals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
