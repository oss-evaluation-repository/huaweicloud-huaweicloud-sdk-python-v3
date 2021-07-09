# coding: utf-8

import re
import six





class ComponentModify:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'source': 'SourceObject',
        'build': 'Build'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'source': 'source',
        'build': 'build'
    }

    def __init__(self, name=None, description=None, source=None, build=None):
        """ComponentModify - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._source = None
        self._build = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build

    @property
    def name(self):
        """Gets the name of this ComponentModify.

        应用组件名称。

        :return: The name of this ComponentModify.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentModify.

        应用组件名称。

        :param name: The name of this ComponentModify.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ComponentModify.

        描述。

        :return: The description of this ComponentModify.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComponentModify.

        描述。

        :param description: The description of this ComponentModify.
        :type: str
        """
        self._description = description

    @property
    def source(self):
        """Gets the source of this ComponentModify.


        :return: The source of this ComponentModify.
        :rtype: SourceObject
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ComponentModify.


        :param source: The source of this ComponentModify.
        :type: SourceObject
        """
        self._source = source

    @property
    def build(self):
        """Gets the build of this ComponentModify.


        :return: The build of this ComponentModify.
        :rtype: Build
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ComponentModify.


        :param build: The build of this ComponentModify.
        :type: Build
        """
        self._build = build

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
        if not isinstance(other, ComponentModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
