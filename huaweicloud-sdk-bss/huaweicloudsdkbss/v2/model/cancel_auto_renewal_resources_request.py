# coding: utf-8

import re
import six





class CancelAutoRenewalResourcesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id'
    }

    def __init__(self, resource_id=None):
        """CancelAutoRenewalResourcesRequest - a model defined in huaweicloud sdk"""
        
        

        self._resource_id = None
        self.discriminator = None

        self.resource_id = resource_id

    @property
    def resource_id(self):
        """Gets the resource_id of this CancelAutoRenewalResourcesRequest.

        |参数名称：资源实例ID。您可以调用“查询客户包年/包月资源列表”接口获取资源ID。在取消弹性云服务器自动续费的时候，能够自动将其挂载的硬盘一并取消自动续费。| |参数的约束及描述：|

        :return: The resource_id of this CancelAutoRenewalResourcesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CancelAutoRenewalResourcesRequest.

        |参数名称：资源实例ID。您可以调用“查询客户包年/包月资源列表”接口获取资源ID。在取消弹性云服务器自动续费的时候，能够自动将其挂载的硬盘一并取消自动续费。| |参数的约束及描述：|

        :param resource_id: The resource_id of this CancelAutoRenewalResourcesRequest.
        :type: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, CancelAutoRenewalResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
