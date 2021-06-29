# coding: utf-8

import pprint
import re

import six





class ListEnvironmentsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, offset=None, limit=None):
        """ListEnvironmentsRequest - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        self.offset = offset
        self.limit = limit

    @property
    def project_id(self):
        """Gets the project_id of this ListEnvironmentsRequest.

        devcloud的项目ID

        :return: The project_id of this ListEnvironmentsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListEnvironmentsRequest.

        devcloud的项目ID

        :param project_id: The project_id of this ListEnvironmentsRequest.
        :type: str
        """
        self._project_id = project_id

    @property
    def offset(self):
        """Gets the offset of this ListEnvironmentsRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListEnvironmentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnvironmentsRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListEnvironmentsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEnvironmentsRequest.

        每页显示的条目数量,最大支持200条

        :return: The limit of this ListEnvironmentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnvironmentsRequest.

        每页显示的条目数量,最大支持200条

        :param limit: The limit of this ListEnvironmentsRequest.
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListEnvironmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other