# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'assets': 'list[DigitalAssetInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'assets': 'assets',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, count=None, assets=None, x_request_id=None):
        """ListAssetsResponse

        The model defined in huaweicloud sdk

        :param count: 资产总数。
        :type count: int
        :param assets: 资产信息列表。
        :type assets: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListAssetsResponse, self).__init__()

        self._count = None
        self._assets = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if assets is not None:
            self.assets = assets
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        """Gets the count of this ListAssetsResponse.

        资产总数。

        :return: The count of this ListAssetsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAssetsResponse.

        资产总数。

        :param count: The count of this ListAssetsResponse.
        :type count: int
        """
        self._count = count

    @property
    def assets(self):
        """Gets the assets of this ListAssetsResponse.

        资产信息列表。

        :return: The assets of this ListAssetsResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetInfo`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this ListAssetsResponse.

        资产信息列表。

        :param assets: The assets of this ListAssetsResponse.
        :type assets: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetInfo`]
        """
        self._assets = assets

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListAssetsResponse.

        :return: The x_request_id of this ListAssetsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListAssetsResponse.

        :param x_request_id: The x_request_id of this ListAssetsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListAssetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
