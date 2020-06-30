# coding: utf-8

import pprint
import re

import six


class KeystoneCreateProjectResult(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_domain': 'bool',
        'description': 'str',
        'extra': 'object',
        'links': 'Links',
        'enabled': 'bool',
        'id': 'str',
        'parent_id': 'str',
        'domain_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'is_domain': 'is_domain',
        'description': 'description',
        'extra': 'extra',
        'links': 'links',
        'enabled': 'enabled',
        'id': 'id',
        'parent_id': 'parent_id',
        'domain_id': 'domain_id',
        'name': 'name'
    }

    def __init__(self, is_domain=None, description=None, extra=None, links=None, enabled=None, id=None, parent_id=None, domain_id=None, name=None):  # noqa: E501
        """KeystoneCreateProjectResult - a model defined in huaweicloud sdk"""

        self._is_domain = None
        self._description = None
        self._extra = None
        self._links = None
        self._enabled = None
        self._id = None
        self._parent_id = None
        self._domain_id = None
        self._name = None
        self.discriminator = None

        self.is_domain = is_domain
        self.description = description
        if extra is not None:
            self.extra = extra
        self.links = links
        self.enabled = enabled
        self.id = id
        self.parent_id = parent_id
        self.domain_id = domain_id
        self.name = name

    @property
    def is_domain(self):
        """Gets the is_domain of this KeystoneCreateProjectResult.

        false.

        :return: The is_domain of this KeystoneCreateProjectResult.
        :rtype: bool
        """
        return self._is_domain

    @is_domain.setter
    def is_domain(self, is_domain):
        """Sets the is_domain of this KeystoneCreateProjectResult.

        false.

        :param is_domain: The is_domain of this KeystoneCreateProjectResult.
        :type: bool
        """
        self._is_domain = is_domain

    @property
    def description(self):
        """Gets the description of this KeystoneCreateProjectResult.

        项目描述信息。

        :return: The description of this KeystoneCreateProjectResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeystoneCreateProjectResult.

        项目描述信息。

        :param description: The description of this KeystoneCreateProjectResult.
        :type: str
        """
        self._description = description

    @property
    def extra(self):
        """Gets the extra of this KeystoneCreateProjectResult.

        项目的其他信息。

        :return: The extra of this KeystoneCreateProjectResult.
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this KeystoneCreateProjectResult.

        项目的其他信息。

        :param extra: The extra of this KeystoneCreateProjectResult.
        :type: object
        """
        self._extra = extra

    @property
    def links(self):
        """Gets the links of this KeystoneCreateProjectResult.


        :return: The links of this KeystoneCreateProjectResult.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneCreateProjectResult.


        :param links: The links of this KeystoneCreateProjectResult.
        :type: Links
        """
        self._links = links

    @property
    def enabled(self):
        """Gets the enabled of this KeystoneCreateProjectResult.

        项目是否可用。

        :return: The enabled of this KeystoneCreateProjectResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this KeystoneCreateProjectResult.

        项目是否可用。

        :param enabled: The enabled of this KeystoneCreateProjectResult.
        :type: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this KeystoneCreateProjectResult.

        项目ID。

        :return: The id of this KeystoneCreateProjectResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KeystoneCreateProjectResult.

        项目ID。

        :param id: The id of this KeystoneCreateProjectResult.
        :type: str
        """
        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this KeystoneCreateProjectResult.

        区域对应的项目ID，例如区域“华北-北京一”区域对应的项目ID为：04dd42abe48026ad2fa3c01ad7fa.....。

        :return: The parent_id of this KeystoneCreateProjectResult.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this KeystoneCreateProjectResult.

        区域对应的项目ID，例如区域“华北-北京一”区域对应的项目ID为：04dd42abe48026ad2fa3c01ad7fa.....。

        :param parent_id: The parent_id of this KeystoneCreateProjectResult.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneCreateProjectResult.

        项目所属账号ID。

        :return: The domain_id of this KeystoneCreateProjectResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneCreateProjectResult.

        项目所属账号ID。

        :param domain_id: The domain_id of this KeystoneCreateProjectResult.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this KeystoneCreateProjectResult.

        项目名称。

        :return: The name of this KeystoneCreateProjectResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneCreateProjectResult.

        项目名称。

        :param name: The name of this KeystoneCreateProjectResult.
        :type: str
        """
        self._name = name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KeystoneCreateProjectResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other