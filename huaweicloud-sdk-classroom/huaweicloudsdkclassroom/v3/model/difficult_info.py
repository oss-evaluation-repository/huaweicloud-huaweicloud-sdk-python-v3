# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DifficultInfo:

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
        'degree': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'degree': 'degree'
    }

    def __init__(self, id=None, name=None, degree=None):
        """DifficultInfo

        The model defined in huaweicloud sdk

        :param id: 难度id
        :type id: str
        :param name: 难度名称
        :type name: str
        :param degree: 难度等级
        :type degree: int
        """
        
        

        self._id = None
        self._name = None
        self._degree = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.degree = degree

    @property
    def id(self):
        """Gets the id of this DifficultInfo.

        难度id

        :return: The id of this DifficultInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DifficultInfo.

        难度id

        :param id: The id of this DifficultInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DifficultInfo.

        难度名称

        :return: The name of this DifficultInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DifficultInfo.

        难度名称

        :param name: The name of this DifficultInfo.
        :type name: str
        """
        self._name = name

    @property
    def degree(self):
        """Gets the degree of this DifficultInfo.

        难度等级

        :return: The degree of this DifficultInfo.
        :rtype: int
        """
        return self._degree

    @degree.setter
    def degree(self, degree):
        """Sets the degree of this DifficultInfo.

        难度等级

        :param degree: The degree of this DifficultInfo.
        :type degree: int
        """
        self._degree = degree

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
        if not isinstance(other, DifficultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other