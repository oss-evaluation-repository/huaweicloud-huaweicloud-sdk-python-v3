# coding: utf-8

import re
import six





class ListResourceInstancesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'body': 'QueryTagsOption'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'body': 'body'
    }

    def __init__(self, resource_type=None, body=None):
        """ListResourceInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._resource_type = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        """Gets the resource_type of this ListResourceInstancesRequest.

        资源类型，枚举类：SCALING_GROUP_TAG。

        :return: The resource_type of this ListResourceInstancesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListResourceInstancesRequest.

        资源类型，枚举类：SCALING_GROUP_TAG。

        :param resource_type: The resource_type of this ListResourceInstancesRequest.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def body(self):
        """Gets the body of this ListResourceInstancesRequest.


        :return: The body of this ListResourceInstancesRequest.
        :rtype: QueryTagsOption
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListResourceInstancesRequest.


        :param body: The body of this ListResourceInstancesRequest.
        :type: QueryTagsOption
        """
        self._body = body

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
        if not isinstance(other, ListResourceInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
