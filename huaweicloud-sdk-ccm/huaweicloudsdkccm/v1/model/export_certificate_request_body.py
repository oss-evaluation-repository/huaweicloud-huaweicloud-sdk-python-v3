# coding: utf-8

import re
import six





class ExportCertificateRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_compressed': 'str',
        'type': 'str'
    }

    attribute_map = {
        'is_compressed': 'is_compressed',
        'type': 'type'
    }

    def __init__(self, is_compressed=None, type=None):
        """ExportCertificateRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._is_compressed = None
        self._type = None
        self.discriminator = None

        if is_compressed is not None:
            self.is_compressed = is_compressed
        if type is not None:
            self.type = type

    @property
    def is_compressed(self):
        """Gets the is_compressed of this ExportCertificateRequestBody.

        是否压缩

        :return: The is_compressed of this ExportCertificateRequestBody.
        :rtype: str
        """
        return self._is_compressed

    @is_compressed.setter
    def is_compressed(self, is_compressed):
        """Sets the is_compressed of this ExportCertificateRequestBody.

        是否压缩

        :param is_compressed: The is_compressed of this ExportCertificateRequestBody.
        :type: str
        """
        self._is_compressed = is_compressed

    @property
    def type(self):
        """Gets the type of this ExportCertificateRequestBody.

        导出类型

        :return: The type of this ExportCertificateRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExportCertificateRequestBody.

        导出类型

        :param type: The type of this ExportCertificateRequestBody.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, ExportCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other