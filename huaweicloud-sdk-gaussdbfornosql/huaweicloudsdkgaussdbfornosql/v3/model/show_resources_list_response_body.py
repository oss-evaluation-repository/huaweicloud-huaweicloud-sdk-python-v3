# coding: utf-8

import re
import six





class ShowResourcesListResponseBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resources': 'list[ShowResourcesDetailResponseBody]'
    }

    attribute_map = {
        'resources': 'resources'
    }

    def __init__(self, resources=None):
        """ShowResourcesListResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._resources = None
        self.discriminator = None

        self.resources = resources

    @property
    def resources(self):
        """Gets the resources of this ShowResourcesListResponseBody.

        资源列表对象。

        :return: The resources of this ShowResourcesListResponseBody.
        :rtype: list[ShowResourcesDetailResponseBody]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ShowResourcesListResponseBody.

        资源列表对象。

        :param resources: The resources of this ShowResourcesListResponseBody.
        :type: list[ShowResourcesDetailResponseBody]
        """
        self._resources = resources

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
        if not isinstance(other, ShowResourcesListResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
