# coding: utf-8

import re
import six





class MountUser:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_id': 'int',
        'user_group_id': 'int'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_group_id': 'user_group_id'
    }

    def __init__(self, user_id=None, user_group_id=None):
        """MountUser - a model defined in huaweicloud sdk"""
        
        

        self._user_id = None
        self._user_group_id = None
        self.discriminator = None

        self.user_id = user_id
        self.user_group_id = user_group_id

    @property
    def user_id(self):
        """Gets the user_id of this MountUser.

        用户ID(-1~65534的非0整数)

        :return: The user_id of this MountUser.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MountUser.

        用户ID(-1~65534的非0整数)

        :param user_id: The user_id of this MountUser.
        :type: int
        """
        self._user_id = user_id

    @property
    def user_group_id(self):
        """Gets the user_group_id of this MountUser.

        用户组ID(-1~65534的非0整数)

        :return: The user_group_id of this MountUser.
        :rtype: int
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this MountUser.

        用户组ID(-1~65534的非0整数)

        :param user_group_id: The user_group_id of this MountUser.
        :type: int
        """
        self._user_group_id = user_group_id

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
        if not isinstance(other, MountUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
