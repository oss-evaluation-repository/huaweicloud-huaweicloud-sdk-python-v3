# coding: utf-8

import re
import six





class ResizeInstanceOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'target_spec_code': 'str'
    }

    attribute_map = {
        'target_spec_code': 'target_spec_code'
    }

    def __init__(self, target_spec_code=None):
        """ResizeInstanceOption - a model defined in huaweicloud sdk"""
        
        

        self._target_spec_code = None
        self.discriminator = None

        self.target_spec_code = target_spec_code

    @property
    def target_spec_code(self):
        """Gets the target_spec_code of this ResizeInstanceOption.

        变更至新规格的资源规格编码。获取方法请参见查询所有实例规格信息中响应参数“flavors.spec_code”的值。

        :return: The target_spec_code of this ResizeInstanceOption.
        :rtype: str
        """
        return self._target_spec_code

    @target_spec_code.setter
    def target_spec_code(self, target_spec_code):
        """Sets the target_spec_code of this ResizeInstanceOption.

        变更至新规格的资源规格编码。获取方法请参见查询所有实例规格信息中响应参数“flavors.spec_code”的值。

        :param target_spec_code: The target_spec_code of this ResizeInstanceOption.
        :type: str
        """
        self._target_spec_code = target_spec_code

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
        if not isinstance(other, ResizeInstanceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
