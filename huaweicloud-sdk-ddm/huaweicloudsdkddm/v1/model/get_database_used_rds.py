# coding: utf-8

import re
import six





class GetDatabaseUsedRds:


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
        'status': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'error_msg': 'error_msg'
    }

    def __init__(self, id=None, name=None, status=None, error_msg=None):
        """GetDatabaseUsedRds - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._status = None
        self._error_msg = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def id(self):
        """Gets the id of this GetDatabaseUsedRds.

        关联RDS节点ID。

        :return: The id of this GetDatabaseUsedRds.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetDatabaseUsedRds.

        关联RDS节点ID。

        :param id: The id of this GetDatabaseUsedRds.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this GetDatabaseUsedRds.

        关联RDS名称

        :return: The name of this GetDatabaseUsedRds.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetDatabaseUsedRds.

        关联RDS名称

        :param name: The name of this GetDatabaseUsedRds.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this GetDatabaseUsedRds.

        关联RDS状态。

        :return: The status of this GetDatabaseUsedRds.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetDatabaseUsedRds.

        关联RDS状态。

        :param status: The status of this GetDatabaseUsedRds.
        :type: str
        """
        self._status = status

    @property
    def error_msg(self):
        """Gets the error_msg of this GetDatabaseUsedRds.

        响应信息，若无异常信息则不返回该参数。

        :return: The error_msg of this GetDatabaseUsedRds.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this GetDatabaseUsedRds.

        响应信息，若无异常信息则不返回该参数。

        :param error_msg: The error_msg of this GetDatabaseUsedRds.
        :type: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, GetDatabaseUsedRds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
