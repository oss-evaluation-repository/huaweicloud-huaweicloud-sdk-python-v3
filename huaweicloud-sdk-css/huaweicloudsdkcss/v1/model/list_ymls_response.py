# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListYmlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'config_list': 'list[ConfigList]'
    }

    attribute_map = {
        'config_list': 'configList'
    }

    def __init__(self, config_list=None):
        """ListYmlsResponse

        The model defined in huaweicloud sdk

        :param config_list: 配置列表。
        :type config_list: list[:class:`huaweicloudsdkcss.v1.ConfigList`]
        """
        
        super(ListYmlsResponse, self).__init__()

        self._config_list = None
        self.discriminator = None

        if config_list is not None:
            self.config_list = config_list

    @property
    def config_list(self):
        """Gets the config_list of this ListYmlsResponse.

        配置列表。

        :return: The config_list of this ListYmlsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ConfigList`]
        """
        return self._config_list

    @config_list.setter
    def config_list(self, config_list):
        """Sets the config_list of this ListYmlsResponse.

        配置列表。

        :param config_list: The config_list of this ListYmlsResponse.
        :type config_list: list[:class:`huaweicloudsdkcss.v1.ConfigList`]
        """
        self._config_list = config_list

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
        if not isinstance(other, ListYmlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
