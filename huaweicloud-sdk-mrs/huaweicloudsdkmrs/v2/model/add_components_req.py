# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddComponentsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'components_install_mode': 'list[ComponentInstallMode]'
    }

    attribute_map = {
        'components_install_mode': 'components_install_mode'
    }

    def __init__(self, components_install_mode=None):
        """AddComponentsReq

        The model defined in huaweicloud sdk

        :param components_install_mode: 组件模型详情
        :type components_install_mode: list[:class:`huaweicloudsdkmrs.v2.ComponentInstallMode`]
        """
        
        

        self._components_install_mode = None
        self.discriminator = None

        self.components_install_mode = components_install_mode

    @property
    def components_install_mode(self):
        """Gets the components_install_mode of this AddComponentsReq.

        组件模型详情

        :return: The components_install_mode of this AddComponentsReq.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.ComponentInstallMode`]
        """
        return self._components_install_mode

    @components_install_mode.setter
    def components_install_mode(self, components_install_mode):
        """Sets the components_install_mode of this AddComponentsReq.

        组件模型详情

        :param components_install_mode: The components_install_mode of this AddComponentsReq.
        :type components_install_mode: list[:class:`huaweicloudsdkmrs.v2.ComponentInstallMode`]
        """
        self._components_install_mode = components_install_mode

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
        if not isinstance(other, AddComponentsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other