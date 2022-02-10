# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevicesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name'
    }

    def __init__(self, offset=None, limit=None, name=None):
        """ListDevicesRequest - a model defined in huaweicloud sdk"""
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name

    @property
    def offset(self):
        """Gets the offset of this ListDevicesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListDevicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDevicesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListDevicesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDevicesRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :return: The limit of this ListDevicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDevicesRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :param limit: The limit of this ListDevicesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListDevicesRequest.

        设备名称，模糊匹配，只允许中英文、数字、下划线、中划线，长度1-60

        :return: The name of this ListDevicesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDevicesRequest.

        设备名称，模糊匹配，只允许中英文、数字、下划线、中划线，长度1-60

        :param name: The name of this ListDevicesRequest.
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
        if not isinstance(other, ListDevicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other