# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSpecifiedApiVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'api_version': 'str'
    }

    attribute_map = {
        'api_version': 'api_version'
    }

    def __init__(self, api_version=None):
        """ShowSpecifiedApiVersionRequest

        The model defined in huaweicloud sdk

        :param api_version: API版本号。例如: v1。
        :type api_version: str
        """
        
        

        self._api_version = None
        self.discriminator = None

        self.api_version = api_version

    @property
    def api_version(self):
        """Gets the api_version of this ShowSpecifiedApiVersionRequest.

        API版本号。例如: v1。

        :return: The api_version of this ShowSpecifiedApiVersionRequest.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ShowSpecifiedApiVersionRequest.

        API版本号。例如: v1。

        :param api_version: The api_version of this ShowSpecifiedApiVersionRequest.
        :type api_version: str
        """
        self._api_version = api_version

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
        if not isinstance(other, ShowSpecifiedApiVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
