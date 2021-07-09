# coding: utf-8

import re
import six





class NeutronSecurityGroup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'security_group_rules': 'list[NeutronSecurityGroupRule]',
        'tenant_id': 'str',
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'security_group_rules': 'security_group_rules',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, description=None, id=None, name=None, security_group_rules=None, tenant_id=None, project_id=None, created_at=None, updated_at=None):
        """NeutronSecurityGroup - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._id = None
        self._name = None
        self._security_group_rules = None
        self._tenant_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.description = description
        self.id = id
        self.name = name
        self.security_group_rules = security_group_rules
        self.tenant_id = tenant_id
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def description(self):
        """Gets the description of this NeutronSecurityGroup.

        功能说明：安全组描述 取值范围：0-255个字符

        :return: The description of this NeutronSecurityGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronSecurityGroup.

        功能说明：安全组描述 取值范围：0-255个字符

        :param description: The description of this NeutronSecurityGroup.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this NeutronSecurityGroup.

        安全组ID

        :return: The id of this NeutronSecurityGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronSecurityGroup.

        安全组ID

        :param id: The id of this NeutronSecurityGroup.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronSecurityGroup.

        功能说明：安全组名称 取值范围：0-255个字符

        :return: The name of this NeutronSecurityGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronSecurityGroup.

        功能说明：安全组名称 取值范围：0-255个字符

        :param name: The name of this NeutronSecurityGroup.
        :type: str
        """
        self._name = name

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this NeutronSecurityGroup.

        安全组规则，详情参见Security Group Rule对象

        :return: The security_group_rules of this NeutronSecurityGroup.
        :rtype: list[NeutronSecurityGroupRule]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this NeutronSecurityGroup.

        安全组规则，详情参见Security Group Rule对象

        :param security_group_rules: The security_group_rules of this NeutronSecurityGroup.
        :type: list[NeutronSecurityGroupRule]
        """
        self._security_group_rules = security_group_rules

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronSecurityGroup.

        项目ID

        :return: The tenant_id of this NeutronSecurityGroup.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronSecurityGroup.

        项目ID

        :param tenant_id: The tenant_id of this NeutronSecurityGroup.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronSecurityGroup.

        项目ID

        :return: The project_id of this NeutronSecurityGroup.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronSecurityGroup.

        项目ID

        :param project_id: The project_id of this NeutronSecurityGroup.
        :type: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this NeutronSecurityGroup.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this NeutronSecurityGroup.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NeutronSecurityGroup.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this NeutronSecurityGroup.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NeutronSecurityGroup.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this NeutronSecurityGroup.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NeutronSecurityGroup.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this NeutronSecurityGroup.
        :type: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, NeutronSecurityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
