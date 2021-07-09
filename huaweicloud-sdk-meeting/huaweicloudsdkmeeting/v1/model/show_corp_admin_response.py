# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowCorpAdminResponse(SdkResponse):


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
        'account': 'str',
        'name': 'str',
        'admin_type': 'int',
        'email': 'str',
        'phone': 'str',
        'country': 'str',
        'dept': 'DeptBasicDTO'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'name': 'name',
        'admin_type': 'adminType',
        'email': 'email',
        'phone': 'phone',
        'country': 'country',
        'dept': 'dept'
    }

    def __init__(self, id=None, account=None, name=None, admin_type=None, email=None, phone=None, country=None, dept=None):
        """ShowCorpAdminResponse - a model defined in huaweicloud sdk"""
        
        super(ShowCorpAdminResponse, self).__init__()

        self._id = None
        self._account = None
        self._name = None
        self._admin_type = None
        self._email = None
        self._phone = None
        self._country = None
        self._dept = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account is not None:
            self.account = account
        if name is not None:
            self.name = name
        if admin_type is not None:
            self.admin_type = admin_type
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if dept is not None:
            self.dept = dept

    @property
    def id(self):
        """Gets the id of this ShowCorpAdminResponse.

        用户id

        :return: The id of this ShowCorpAdminResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowCorpAdminResponse.

        用户id

        :param id: The id of this ShowCorpAdminResponse.
        :type: str
        """
        self._id = id

    @property
    def account(self):
        """Gets the account of this ShowCorpAdminResponse.

        用户账号

        :return: The account of this ShowCorpAdminResponse.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ShowCorpAdminResponse.

        用户账号

        :param account: The account of this ShowCorpAdminResponse.
        :type: str
        """
        self._account = account

    @property
    def name(self):
        """Gets the name of this ShowCorpAdminResponse.

        名称

        :return: The name of this ShowCorpAdminResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowCorpAdminResponse.

        名称

        :param name: The name of this ShowCorpAdminResponse.
        :type: str
        """
        self._name = name

    @property
    def admin_type(self):
        """Gets the admin_type of this ShowCorpAdminResponse.

        管理员类型。 0：默认管理员 1：普通管理员 

        :return: The admin_type of this ShowCorpAdminResponse.
        :rtype: int
        """
        return self._admin_type

    @admin_type.setter
    def admin_type(self, admin_type):
        """Sets the admin_type of this ShowCorpAdminResponse.

        管理员类型。 0：默认管理员 1：普通管理员 

        :param admin_type: The admin_type of this ShowCorpAdminResponse.
        :type: int
        """
        self._admin_type = admin_type

    @property
    def email(self):
        """Gets the email of this ShowCorpAdminResponse.

        邮箱

        :return: The email of this ShowCorpAdminResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ShowCorpAdminResponse.

        邮箱

        :param email: The email of this ShowCorpAdminResponse.
        :type: str
        """
        self._email = email

    @property
    def phone(self):
        """Gets the phone of this ShowCorpAdminResponse.

        手机号

        :return: The phone of this ShowCorpAdminResponse.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ShowCorpAdminResponse.

        手机号

        :param phone: The phone of this ShowCorpAdminResponse.
        :type: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this ShowCorpAdminResponse.

        手机号所属的国家

        :return: The country of this ShowCorpAdminResponse.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShowCorpAdminResponse.

        手机号所属的国家

        :param country: The country of this ShowCorpAdminResponse.
        :type: str
        """
        self._country = country

    @property
    def dept(self):
        """Gets the dept of this ShowCorpAdminResponse.


        :return: The dept of this ShowCorpAdminResponse.
        :rtype: DeptBasicDTO
        """
        return self._dept

    @dept.setter
    def dept(self, dept):
        """Sets the dept of this ShowCorpAdminResponse.


        :param dept: The dept of this ShowCorpAdminResponse.
        :type: DeptBasicDTO
        """
        self._dept = dept

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
        if not isinstance(other, ShowCorpAdminResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
