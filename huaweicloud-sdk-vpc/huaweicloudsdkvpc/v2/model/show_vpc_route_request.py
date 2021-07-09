# coding: utf-8

import re
import six





class ShowVpcRouteRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'route_id': 'str'
    }

    attribute_map = {
        'route_id': 'route_id'
    }

    def __init__(self, route_id=None):
        """ShowVpcRouteRequest - a model defined in huaweicloud sdk"""
        
        

        self._route_id = None
        self.discriminator = None

        self.route_id = route_id

    @property
    def route_id(self):
        """Gets the route_id of this ShowVpcRouteRequest.

        路由ID

        :return: The route_id of this ShowVpcRouteRequest.
        :rtype: str
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        """Sets the route_id of this ShowVpcRouteRequest.

        路由ID

        :param route_id: The route_id of this ShowVpcRouteRequest.
        :type: str
        """
        self._route_id = route_id

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
        if not isinstance(other, ShowVpcRouteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
