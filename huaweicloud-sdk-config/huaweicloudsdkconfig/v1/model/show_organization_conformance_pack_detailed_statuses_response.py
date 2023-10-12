# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrganizationConformancePackDetailedStatusesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statuses': 'list[OrgConformancePackDetailedStatus]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'statuses': 'statuses',
        'page_info': 'page_info'
    }

    def __init__(self, statuses=None, page_info=None):
        """ShowOrganizationConformancePackDetailedStatusesResponse

        The model defined in huaweicloud sdk

        :param statuses: 组织合规规则包查询列表。
        :type statuses: list[:class:`huaweicloudsdkconfig.v1.OrgConformancePackDetailedStatus`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        
        super(ShowOrganizationConformancePackDetailedStatusesResponse, self).__init__()

        self._statuses = None
        self._page_info = None
        self.discriminator = None

        if statuses is not None:
            self.statuses = statuses
        if page_info is not None:
            self.page_info = page_info

    @property
    def statuses(self):
        """Gets the statuses of this ShowOrganizationConformancePackDetailedStatusesResponse.

        组织合规规则包查询列表。

        :return: The statuses of this ShowOrganizationConformancePackDetailedStatusesResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.OrgConformancePackDetailedStatus`]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this ShowOrganizationConformancePackDetailedStatusesResponse.

        组织合规规则包查询列表。

        :param statuses: The statuses of this ShowOrganizationConformancePackDetailedStatusesResponse.
        :type statuses: list[:class:`huaweicloudsdkconfig.v1.OrgConformancePackDetailedStatus`]
        """
        self._statuses = statuses

    @property
    def page_info(self):
        """Gets the page_info of this ShowOrganizationConformancePackDetailedStatusesResponse.

        :return: The page_info of this ShowOrganizationConformancePackDetailedStatusesResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ShowOrganizationConformancePackDetailedStatusesResponse.

        :param page_info: The page_info of this ShowOrganizationConformancePackDetailedStatusesResponse.
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ShowOrganizationConformancePackDetailedStatusesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
