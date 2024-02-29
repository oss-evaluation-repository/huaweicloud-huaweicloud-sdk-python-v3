# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistObjectIdsModifierDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[int]',
        'modifier': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'modifier': 'modifier'
    }

    def __init__(self, ids=None, modifier=None):
        """PersistObjectIdsModifierDTO

        The model defined in huaweicloud sdk

        :param ids: ID列表。
        :type ids: list[int]
        :param modifier: 修改人。
        :type modifier: str
        """
        
        

        self._ids = None
        self._modifier = None
        self.discriminator = None

        self.ids = ids
        if modifier is not None:
            self.modifier = modifier

    @property
    def ids(self):
        """Gets the ids of this PersistObjectIdsModifierDTO.

        ID列表。

        :return: The ids of this PersistObjectIdsModifierDTO.
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this PersistObjectIdsModifierDTO.

        ID列表。

        :param ids: The ids of this PersistObjectIdsModifierDTO.
        :type ids: list[int]
        """
        self._ids = ids

    @property
    def modifier(self):
        """Gets the modifier of this PersistObjectIdsModifierDTO.

        修改人。

        :return: The modifier of this PersistObjectIdsModifierDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this PersistObjectIdsModifierDTO.

        修改人。

        :param modifier: The modifier of this PersistObjectIdsModifierDTO.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, PersistObjectIdsModifierDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
