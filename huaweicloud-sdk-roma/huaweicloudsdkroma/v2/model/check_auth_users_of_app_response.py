# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckAuthUsersOfAppResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'id': 'str',
        'users': 'list[AppUsersUsers]'
    }

    attribute_map = {
        'total': 'total',
        'id': 'id',
        'users': 'users'
    }

    def __init__(self, total=None, id=None, users=None):
        """CheckAuthUsersOfAppResponse - a model defined in huaweicloud sdk"""
        
        super(CheckAuthUsersOfAppResponse, self).__init__()

        self._total = None
        self._id = None
        self._users = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if id is not None:
            self.id = id
        if users is not None:
            self.users = users

    @property
    def total(self):
        """Gets the total of this CheckAuthUsersOfAppResponse.

        应用的总成员数量

        :return: The total of this CheckAuthUsersOfAppResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CheckAuthUsersOfAppResponse.

        应用的总成员数量

        :param total: The total of this CheckAuthUsersOfAppResponse.
        :type: int
        """
        self._total = total

    @property
    def id(self):
        """Gets the id of this CheckAuthUsersOfAppResponse.

        应用ID

        :return: The id of this CheckAuthUsersOfAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckAuthUsersOfAppResponse.

        应用ID

        :param id: The id of this CheckAuthUsersOfAppResponse.
        :type: str
        """
        self._id = id

    @property
    def users(self):
        """Gets the users of this CheckAuthUsersOfAppResponse.

        用户成员列表

        :return: The users of this CheckAuthUsersOfAppResponse.
        :rtype: list[AppUsersUsers]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this CheckAuthUsersOfAppResponse.

        用户成员列表

        :param users: The users of this CheckAuthUsersOfAppResponse.
        :type: list[AppUsersUsers]
        """
        self._users = users

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
        if not isinstance(other, CheckAuthUsersOfAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other