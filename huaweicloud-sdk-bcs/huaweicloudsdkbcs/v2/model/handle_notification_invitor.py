# coding: utf-8

import re
import six





class HandleNotificationInvitor:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'invitor_bcs_id': 'str',
        'invitor_bcs_name': 'str',
        'invitor_project_id': 'str',
        'invitor_user_id': 'str'
    }

    attribute_map = {
        'invitor_bcs_id': 'invitor_bcs_id',
        'invitor_bcs_name': 'invitor_bcs_name',
        'invitor_project_id': 'invitor_project_id',
        'invitor_user_id': 'invitor_user_id'
    }

    def __init__(self, invitor_bcs_id=None, invitor_bcs_name=None, invitor_project_id=None, invitor_user_id=None):
        """HandleNotificationInvitor - a model defined in huaweicloud sdk"""
        
        

        self._invitor_bcs_id = None
        self._invitor_bcs_name = None
        self._invitor_project_id = None
        self._invitor_user_id = None
        self.discriminator = None

        self.invitor_bcs_id = invitor_bcs_id
        self.invitor_bcs_name = invitor_bcs_name
        self.invitor_project_id = invitor_project_id
        self.invitor_user_id = invitor_user_id

    @property
    def invitor_bcs_id(self):
        """Gets the invitor_bcs_id of this HandleNotificationInvitor.

        邀请方实例id

        :return: The invitor_bcs_id of this HandleNotificationInvitor.
        :rtype: str
        """
        return self._invitor_bcs_id

    @invitor_bcs_id.setter
    def invitor_bcs_id(self, invitor_bcs_id):
        """Sets the invitor_bcs_id of this HandleNotificationInvitor.

        邀请方实例id

        :param invitor_bcs_id: The invitor_bcs_id of this HandleNotificationInvitor.
        :type: str
        """
        self._invitor_bcs_id = invitor_bcs_id

    @property
    def invitor_bcs_name(self):
        """Gets the invitor_bcs_name of this HandleNotificationInvitor.

        邀请方实例名称，同意联盟邀请时比填

        :return: The invitor_bcs_name of this HandleNotificationInvitor.
        :rtype: str
        """
        return self._invitor_bcs_name

    @invitor_bcs_name.setter
    def invitor_bcs_name(self, invitor_bcs_name):
        """Sets the invitor_bcs_name of this HandleNotificationInvitor.

        邀请方实例名称，同意联盟邀请时比填

        :param invitor_bcs_name: The invitor_bcs_name of this HandleNotificationInvitor.
        :type: str
        """
        self._invitor_bcs_name = invitor_bcs_name

    @property
    def invitor_project_id(self):
        """Gets the invitor_project_id of this HandleNotificationInvitor.

        邀请方project id

        :return: The invitor_project_id of this HandleNotificationInvitor.
        :rtype: str
        """
        return self._invitor_project_id

    @invitor_project_id.setter
    def invitor_project_id(self, invitor_project_id):
        """Sets the invitor_project_id of this HandleNotificationInvitor.

        邀请方project id

        :param invitor_project_id: The invitor_project_id of this HandleNotificationInvitor.
        :type: str
        """
        self._invitor_project_id = invitor_project_id

    @property
    def invitor_user_id(self):
        """Gets the invitor_user_id of this HandleNotificationInvitor.

        邀请方租户,hcs模式下是邀请方租户id

        :return: The invitor_user_id of this HandleNotificationInvitor.
        :rtype: str
        """
        return self._invitor_user_id

    @invitor_user_id.setter
    def invitor_user_id(self, invitor_user_id):
        """Sets the invitor_user_id of this HandleNotificationInvitor.

        邀请方租户,hcs模式下是邀请方租户id

        :param invitor_user_id: The invitor_user_id of this HandleNotificationInvitor.
        :type: str
        """
        self._invitor_user_id = invitor_user_id

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
        if not isinstance(other, HandleNotificationInvitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
