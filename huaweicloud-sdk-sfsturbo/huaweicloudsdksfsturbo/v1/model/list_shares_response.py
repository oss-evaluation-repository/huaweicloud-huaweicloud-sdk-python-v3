# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'shares': 'list[Shares]',
        'count': 'int'
    }

    attribute_map = {
        'shares': 'shares',
        'count': 'count'
    }

    def __init__(self, shares=None, count=None):
        """ListSharesResponse - a model defined in huaweicloud sdk"""
        
        super(ListSharesResponse, self).__init__()

        self._shares = None
        self._count = None
        self.discriminator = None

        if shares is not None:
            self.shares = shares
        if count is not None:
            self.count = count

    @property
    def shares(self):
        """Gets the shares of this ListSharesResponse.

        SFS Turbo文件系统的列表。

        :return: The shares of this ListSharesResponse.
        :rtype: list[Shares]
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """Sets the shares of this ListSharesResponse.

        SFS Turbo文件系统的列表。

        :param shares: The shares of this ListSharesResponse.
        :type: list[Shares]
        """
        self._shares = shares

    @property
    def count(self):
        """Gets the count of this ListSharesResponse.

        SFS Turbo文件系统的数量。

        :return: The count of this ListSharesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSharesResponse.

        SFS Turbo文件系统的数量。

        :param count: The count of this ListSharesResponse.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, ListSharesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other