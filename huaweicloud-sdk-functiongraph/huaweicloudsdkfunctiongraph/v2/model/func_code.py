# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuncCode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file': 'str',
        'link': 'str'
    }

    attribute_map = {
        'file': 'file',
        'link': 'link'
    }

    def __init__(self, file=None, link=None):
        """FuncCode

        The model defined in huaweicloud sdk

        :param file: 函数代码，当CodeTye为inline/zip/jar时必选，且代码必须要进行base64编码。
        :type file: str
        :param link: 函数代码链接。
        :type link: str
        """
        
        

        self._file = None
        self._link = None
        self.discriminator = None

        if file is not None:
            self.file = file
        if link is not None:
            self.link = link

    @property
    def file(self):
        """Gets the file of this FuncCode.

        函数代码，当CodeTye为inline/zip/jar时必选，且代码必须要进行base64编码。

        :return: The file of this FuncCode.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FuncCode.

        函数代码，当CodeTye为inline/zip/jar时必选，且代码必须要进行base64编码。

        :param file: The file of this FuncCode.
        :type file: str
        """
        self._file = file

    @property
    def link(self):
        """Gets the link of this FuncCode.

        函数代码链接。

        :return: The link of this FuncCode.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this FuncCode.

        函数代码链接。

        :param link: The link of this FuncCode.
        :type link: str
        """
        self._link = link

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
        if not isinstance(other, FuncCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
