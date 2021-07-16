# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListFlavorsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'compute_flavor_groups': 'list[ComputeFlavorGroupsInfo]'
    }

    attribute_map = {
        'compute_flavor_groups': 'computeFlavorGroups'
    }

    def __init__(self, compute_flavor_groups=None):
        """ListFlavorsResponse - a model defined in huaweicloud sdk"""
        
        super(ListFlavorsResponse, self).__init__()

        self._compute_flavor_groups = None
        self.discriminator = None

        if compute_flavor_groups is not None:
            self.compute_flavor_groups = compute_flavor_groups

    @property
    def compute_flavor_groups(self):
        """Gets the compute_flavor_groups of this ListFlavorsResponse.

        计算类型规格组。

        :return: The compute_flavor_groups of this ListFlavorsResponse.
        :rtype: list[ComputeFlavorGroupsInfo]
        """
        return self._compute_flavor_groups

    @compute_flavor_groups.setter
    def compute_flavor_groups(self, compute_flavor_groups):
        """Sets the compute_flavor_groups of this ListFlavorsResponse.

        计算类型规格组。

        :param compute_flavor_groups: The compute_flavor_groups of this ListFlavorsResponse.
        :type: list[ComputeFlavorGroupsInfo]
        """
        self._compute_flavor_groups = compute_flavor_groups

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
        if not isinstance(other, ListFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other