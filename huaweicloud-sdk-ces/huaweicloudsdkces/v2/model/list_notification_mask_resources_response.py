# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationMaskResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[Resource]',
        'count': 'int'
    }

    attribute_map = {
        'resources': 'resources',
        'count': 'count'
    }

    def __init__(self, resources=None, count=None):
        """ListNotificationMaskResourcesResponse

        The model defined in huaweicloud sdk

        :param resources: 通知屏蔽资源列表
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        :param count: 资源总数
        :type count: int
        """
        
        super(ListNotificationMaskResourcesResponse, self).__init__()

        self._resources = None
        self._count = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if count is not None:
            self.count = count

    @property
    def resources(self):
        """Gets the resources of this ListNotificationMaskResourcesResponse.

        通知屏蔽资源列表

        :return: The resources of this ListNotificationMaskResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListNotificationMaskResourcesResponse.

        通知屏蔽资源列表

        :param resources: The resources of this ListNotificationMaskResourcesResponse.
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        self._resources = resources

    @property
    def count(self):
        """Gets the count of this ListNotificationMaskResourcesResponse.

        资源总数

        :return: The count of this ListNotificationMaskResourcesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListNotificationMaskResourcesResponse.

        资源总数

        :param count: The count of this ListNotificationMaskResourcesResponse.
        :type count: int
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
        if not isinstance(other, ListNotificationMaskResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
