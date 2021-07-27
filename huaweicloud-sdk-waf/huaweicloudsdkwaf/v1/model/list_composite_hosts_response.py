# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCompositeHostsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'cloud_total': 'int',
        'premium_total': 'int',
        'items': 'list[CompositeHostResponse]'
    }

    attribute_map = {
        'total': 'total',
        'cloud_total': 'cloud_total',
        'premium_total': 'premium_total',
        'items': 'items'
    }

    def __init__(self, total=None, cloud_total=None, premium_total=None, items=None):
        """ListCompositeHostsResponse - a model defined in huaweicloud sdk"""
        
        super(ListCompositeHostsResponse, self).__init__()

        self._total = None
        self._cloud_total = None
        self._premium_total = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if cloud_total is not None:
            self.cloud_total = cloud_total
        if premium_total is not None:
            self.premium_total = premium_total
        if items is not None:
            self.items = items

    @property
    def total(self):
        """Gets the total of this ListCompositeHostsResponse.

        所有防护域名的数量

        :return: The total of this ListCompositeHostsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCompositeHostsResponse.

        所有防护域名的数量

        :param total: The total of this ListCompositeHostsResponse.
        :type: int
        """
        self._total = total

    @property
    def cloud_total(self):
        """Gets the cloud_total of this ListCompositeHostsResponse.

        云模式防护域名的数量

        :return: The cloud_total of this ListCompositeHostsResponse.
        :rtype: int
        """
        return self._cloud_total

    @cloud_total.setter
    def cloud_total(self, cloud_total):
        """Sets the cloud_total of this ListCompositeHostsResponse.

        云模式防护域名的数量

        :param cloud_total: The cloud_total of this ListCompositeHostsResponse.
        :type: int
        """
        self._cloud_total = cloud_total

    @property
    def premium_total(self):
        """Gets the premium_total of this ListCompositeHostsResponse.

        独享防护域名的数量

        :return: The premium_total of this ListCompositeHostsResponse.
        :rtype: int
        """
        return self._premium_total

    @premium_total.setter
    def premium_total(self, premium_total):
        """Sets the premium_total of this ListCompositeHostsResponse.

        独享防护域名的数量

        :param premium_total: The premium_total of this ListCompositeHostsResponse.
        :type: int
        """
        self._premium_total = premium_total

    @property
    def items(self):
        """Gets the items of this ListCompositeHostsResponse.

        详细的防护域名信息

        :return: The items of this ListCompositeHostsResponse.
        :rtype: list[CompositeHostResponse]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListCompositeHostsResponse.

        详细的防护域名信息

        :param items: The items of this ListCompositeHostsResponse.
        :type: list[CompositeHostResponse]
        """
        self._items = items

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
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCompositeHostsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other