# coding: utf-8

import re
import six





class CreateVpcResourceTagRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tag': 'ResourceTag'
    }

    attribute_map = {
        'tag': 'tag'
    }

    def __init__(self, tag=None):
        """CreateVpcResourceTagRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._tag = None
        self.discriminator = None

        self.tag = tag

    @property
    def tag(self):
        """Gets the tag of this CreateVpcResourceTagRequestBody.


        :return: The tag of this CreateVpcResourceTagRequestBody.
        :rtype: ResourceTag
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CreateVpcResourceTagRequestBody.


        :param tag: The tag of this CreateVpcResourceTagRequestBody.
        :type: ResourceTag
        """
        self._tag = tag

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
        if not isinstance(other, CreateVpcResourceTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
