# coding: utf-8

import re
import six





class Links:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'rel': 'str',
        'href': 'str'
    }

    attribute_map = {
        'rel': 'rel',
        'href': 'href'
    }

    def __init__(self, rel=None, href=None):
        """Links - a model defined in huaweicloud sdk"""
        
        

        self._rel = None
        self._href = None
        self.discriminator = None

        if rel is not None:
            self.rel = rel
        if href is not None:
            self.href = href

    @property
    def rel(self):
        """Gets the rel of this Links.

        快捷链接标记名称

        :return: The rel of this Links.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this Links.

        快捷链接标记名称

        :param rel: The rel of this Links.
        :type: str
        """
        self._rel = rel

    @property
    def href(self):
        """Gets the href of this Links.

        对应快捷链接

        :return: The href of this Links.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Links.

        对应快捷链接

        :param href: The href of this Links.
        :type: str
        """
        self._href = href

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
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
