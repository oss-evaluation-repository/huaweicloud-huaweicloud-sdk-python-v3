# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlLimitObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'query_id': 'str',
        'query_string': 'str',
        'max_concurrency': 'int',
        'is_effective': 'bool',
        'max_waiting': 'int',
        'search_path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'query_id': 'query_id',
        'query_string': 'query_string',
        'max_concurrency': 'max_concurrency',
        'is_effective': 'is_effective',
        'max_waiting': 'max_waiting',
        'search_path': 'search_path'
    }

    def __init__(self, id=None, query_id=None, query_string=None, max_concurrency=None, is_effective=None, max_waiting=None, search_path=None):
        """SqlLimitObject

        The model defined in huaweicloud sdk

        :param id: SQL限流ID。
        :type id: str
        :param query_id: 由SQL的语法解析树计算出的内部哈希码，默认为0，取值范围（-9223372036854775808~ 9223372036854775807）。
        :type query_id: str
        :param query_string: SQL语句的文本形式。
        :type query_string: str
        :param max_concurrency: 同时执行的SQL数量，小于等于0表示不限制，默认为0，取值范围（-1~50000）。
        :type max_concurrency: int
        :param is_effective: 是否生效
        :type is_effective: bool
        :param max_waiting: 最大等待时间，单位为秒。
        :type max_waiting: int
        :param search_path: 为不是模式限定的名称设置模式搜索顺序，默认为public。
        :type search_path: str
        """
        
        

        self._id = None
        self._query_id = None
        self._query_string = None
        self._max_concurrency = None
        self._is_effective = None
        self._max_waiting = None
        self._search_path = None
        self.discriminator = None

        self.id = id
        self.query_id = query_id
        self.query_string = query_string
        self.max_concurrency = max_concurrency
        self.is_effective = is_effective
        self.max_waiting = max_waiting
        self.search_path = search_path

    @property
    def id(self):
        """Gets the id of this SqlLimitObject.

        SQL限流ID。

        :return: The id of this SqlLimitObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SqlLimitObject.

        SQL限流ID。

        :param id: The id of this SqlLimitObject.
        :type id: str
        """
        self._id = id

    @property
    def query_id(self):
        """Gets the query_id of this SqlLimitObject.

        由SQL的语法解析树计算出的内部哈希码，默认为0，取值范围（-9223372036854775808~ 9223372036854775807）。

        :return: The query_id of this SqlLimitObject.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this SqlLimitObject.

        由SQL的语法解析树计算出的内部哈希码，默认为0，取值范围（-9223372036854775808~ 9223372036854775807）。

        :param query_id: The query_id of this SqlLimitObject.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def query_string(self):
        """Gets the query_string of this SqlLimitObject.

        SQL语句的文本形式。

        :return: The query_string of this SqlLimitObject.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this SqlLimitObject.

        SQL语句的文本形式。

        :param query_string: The query_string of this SqlLimitObject.
        :type query_string: str
        """
        self._query_string = query_string

    @property
    def max_concurrency(self):
        """Gets the max_concurrency of this SqlLimitObject.

        同时执行的SQL数量，小于等于0表示不限制，默认为0，取值范围（-1~50000）。

        :return: The max_concurrency of this SqlLimitObject.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        """Sets the max_concurrency of this SqlLimitObject.

        同时执行的SQL数量，小于等于0表示不限制，默认为0，取值范围（-1~50000）。

        :param max_concurrency: The max_concurrency of this SqlLimitObject.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def is_effective(self):
        """Gets the is_effective of this SqlLimitObject.

        是否生效

        :return: The is_effective of this SqlLimitObject.
        :rtype: bool
        """
        return self._is_effective

    @is_effective.setter
    def is_effective(self, is_effective):
        """Sets the is_effective of this SqlLimitObject.

        是否生效

        :param is_effective: The is_effective of this SqlLimitObject.
        :type is_effective: bool
        """
        self._is_effective = is_effective

    @property
    def max_waiting(self):
        """Gets the max_waiting of this SqlLimitObject.

        最大等待时间，单位为秒。

        :return: The max_waiting of this SqlLimitObject.
        :rtype: int
        """
        return self._max_waiting

    @max_waiting.setter
    def max_waiting(self, max_waiting):
        """Sets the max_waiting of this SqlLimitObject.

        最大等待时间，单位为秒。

        :param max_waiting: The max_waiting of this SqlLimitObject.
        :type max_waiting: int
        """
        self._max_waiting = max_waiting

    @property
    def search_path(self):
        """Gets the search_path of this SqlLimitObject.

        为不是模式限定的名称设置模式搜索顺序，默认为public。

        :return: The search_path of this SqlLimitObject.
        :rtype: str
        """
        return self._search_path

    @search_path.setter
    def search_path(self, search_path):
        """Sets the search_path of this SqlLimitObject.

        为不是模式限定的名称设置模式搜索顺序，默认为public。

        :param search_path: The search_path of this SqlLimitObject.
        :type search_path: str
        """
        self._search_path = search_path

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
        if not isinstance(other, SqlLimitObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
