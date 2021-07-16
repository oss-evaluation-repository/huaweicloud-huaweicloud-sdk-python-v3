# coding: utf-8

import re
import six





class EngineGroupsInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'version': 'str',
        'support_azs': 'list[SupportAzsInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'support_azs': 'supportAzs'
    }

    def __init__(self, id=None, name=None, version=None, support_azs=None):
        """EngineGroupsInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._version = None
        self._support_azs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if support_azs is not None:
            self.support_azs = support_azs

    @property
    def id(self):
        """Gets the id of this EngineGroupsInfo.

        引擎id。

        :return: The id of this EngineGroupsInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EngineGroupsInfo.

        引擎id。

        :param id: The id of this EngineGroupsInfo.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EngineGroupsInfo.

        引擎名称。

        :return: The name of this EngineGroupsInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EngineGroupsInfo.

        引擎名称。

        :param name: The name of this EngineGroupsInfo.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this EngineGroupsInfo.

        引擎版本。

        :return: The version of this EngineGroupsInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EngineGroupsInfo.

        引擎版本。

        :param version: The version of this EngineGroupsInfo.
        :type: str
        """
        self._version = version

    @property
    def support_azs(self):
        """Gets the support_azs of this EngineGroupsInfo.

        可用区列表。

        :return: The support_azs of this EngineGroupsInfo.
        :rtype: list[SupportAzsInfo]
        """
        return self._support_azs

    @support_azs.setter
    def support_azs(self, support_azs):
        """Sets the support_azs of this EngineGroupsInfo.

        可用区列表。

        :param support_azs: The support_azs of this EngineGroupsInfo.
        :type: list[SupportAzsInfo]
        """
        self._support_azs = support_azs

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
        if not isinstance(other, EngineGroupsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other