# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreatePoolResponse(SdkResponse):


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
        'name': 'str',
        'region': 'str',
        'type': 'str',
        'vpc_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region': 'region',
        'type': 'type',
        'vpc_id': 'vpc_id',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, region=None, type=None, vpc_id=None, description=None):
        """CreatePoolResponse - a model defined in huaweicloud sdk"""
        
        super(CreatePoolResponse, self).__init__()

        self._id = None
        self._name = None
        self._region = None
        self._type = None
        self._vpc_id = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this CreatePoolResponse.

        36位标准化UUID

        :return: The id of this CreatePoolResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePoolResponse.

        36位标准化UUID

        :param id: The id of this CreatePoolResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreatePoolResponse.

        WAF独享引擎组名称

        :return: The name of this CreatePoolResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePoolResponse.

        WAF独享引擎组名称

        :param name: The name of this CreatePoolResponse.
        :type: str
        """
        self._name = name

    @property
    def region(self):
        """Gets the region of this CreatePoolResponse.

        标准化region编号

        :return: The region of this CreatePoolResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreatePoolResponse.

        标准化region编号

        :param region: The region of this CreatePoolResponse.
        :type: str
        """
        self._region = region

    @property
    def type(self):
        """Gets the type of this CreatePoolResponse.

        WAF独享引擎组类型

        :return: The type of this CreatePoolResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePoolResponse.

        WAF独享引擎组类型

        :param type: The type of this CreatePoolResponse.
        :type: str
        """
        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreatePoolResponse.

        关联的VPC ID

        :return: The vpc_id of this CreatePoolResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreatePoolResponse.

        关联的VPC ID

        :param vpc_id: The vpc_id of this CreatePoolResponse.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        """Gets the description of this CreatePoolResponse.

        注释

        :return: The description of this CreatePoolResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePoolResponse.

        注释

        :param description: The description of this CreatePoolResponse.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, CreatePoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other