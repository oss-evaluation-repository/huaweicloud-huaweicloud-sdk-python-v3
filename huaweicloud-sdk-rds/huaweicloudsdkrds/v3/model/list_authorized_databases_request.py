# coding: utf-8

import re
import six





class ListAuthorizedDatabasesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'user_name': 'str',
        'page': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'user_name': 'user-name',
        'page': 'page',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, user_name=None, page=None, limit=None):
        """ListAuthorizedDatabasesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._instance_id = None
        self._user_name = None
        self._page = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.user_name = user_name
        self.page = page
        self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListAuthorizedDatabasesRequest.

        语言

        :return: The x_language of this ListAuthorizedDatabasesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListAuthorizedDatabasesRequest.

        语言

        :param x_language: The x_language of this ListAuthorizedDatabasesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAuthorizedDatabasesRequest.

        实例ID。

        :return: The instance_id of this ListAuthorizedDatabasesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAuthorizedDatabasesRequest.

        实例ID。

        :param instance_id: The instance_id of this ListAuthorizedDatabasesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def user_name(self):
        """Gets the user_name of this ListAuthorizedDatabasesRequest.

        数据库用户名。

        :return: The user_name of this ListAuthorizedDatabasesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListAuthorizedDatabasesRequest.

        数据库用户名。

        :param user_name: The user_name of this ListAuthorizedDatabasesRequest.
        :type: str
        """
        self._user_name = user_name

    @property
    def page(self):
        """Gets the page of this ListAuthorizedDatabasesRequest.

        分页页码，从1开始。

        :return: The page of this ListAuthorizedDatabasesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListAuthorizedDatabasesRequest.

        分页页码，从1开始。

        :param page: The page of this ListAuthorizedDatabasesRequest.
        :type: int
        """
        self._page = page

    @property
    def limit(self):
        """Gets the limit of this ListAuthorizedDatabasesRequest.

        每页数据条数。取值范围[1, 100]。

        :return: The limit of this ListAuthorizedDatabasesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAuthorizedDatabasesRequest.

        每页数据条数。取值范围[1, 100]。

        :param limit: The limit of this ListAuthorizedDatabasesRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAuthorizedDatabasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
