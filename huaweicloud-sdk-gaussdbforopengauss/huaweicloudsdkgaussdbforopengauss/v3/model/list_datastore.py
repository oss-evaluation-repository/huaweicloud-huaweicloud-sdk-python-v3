# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatastore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, type=None, version=None):
        """ListDatastore

        The model defined in huaweicloud sdk

        :param type: 数据库引擎。
        :type type: str
        :param version: 数据库版本。
        :type version: str
        """
        
        

        self._type = None
        self._version = None
        self.discriminator = None

        self.type = type
        self.version = version

    @property
    def type(self):
        """Gets the type of this ListDatastore.

        数据库引擎。

        :return: The type of this ListDatastore.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListDatastore.

        数据库引擎。

        :param type: The type of this ListDatastore.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListDatastore.

        数据库版本。

        :return: The version of this ListDatastore.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListDatastore.

        数据库版本。

        :param version: The version of this ListDatastore.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ListDatastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
