# coding: utf-8

import pprint
import re

import six


class NeutronUpdateRouterOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'name': 'str',
        'admin_state_up': 'bool',
        'external_gateway_info': 'ExternalGatewayInfoOption',
        'routes': 'list[Route]'
    }

    attribute_map = {
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'external_gateway_info': 'external_gateway_info',
        'routes': 'routes'
    }

    def __init__(self, name=None, admin_state_up=True, external_gateway_info=None, routes=None):  # noqa: E501
        """NeutronUpdateRouterOption - a model defined in huaweicloud sdk"""

        self._name = None
        self._admin_state_up = None
        self._external_gateway_info = None
        self._routes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if external_gateway_info is not None:
            self.external_gateway_info = external_gateway_info
        if routes is not None:
            self.routes = routes

    @property
    def name(self):
        """Gets the name of this NeutronUpdateRouterOption.

        功能说明：路由器的名称。 取值范围：0-64个字符，仅支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。 约束：如果name非空，则name不能重复。

        :return: The name of this NeutronUpdateRouterOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronUpdateRouterOption.

        功能说明：路由器的名称。 取值范围：0-64个字符，仅支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。 约束：如果name非空，则name不能重复。

        :param name: The name of this NeutronUpdateRouterOption.
        :type: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronUpdateRouterOption.

        功能说明：资源的管理状态。 取值范围：true、false 约束：只支持true

        :return: The admin_state_up of this NeutronUpdateRouterOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronUpdateRouterOption.

        功能说明：资源的管理状态。 取值范围：true、false 约束：只支持true

        :param admin_state_up: The admin_state_up of this NeutronUpdateRouterOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def external_gateway_info(self):
        """Gets the external_gateway_info of this NeutronUpdateRouterOption.


        :return: The external_gateway_info of this NeutronUpdateRouterOption.
        :rtype: ExternalGatewayInfoOption
        """
        return self._external_gateway_info

    @external_gateway_info.setter
    def external_gateway_info(self, external_gateway_info):
        """Sets the external_gateway_info of this NeutronUpdateRouterOption.


        :param external_gateway_info: The external_gateway_info of this NeutronUpdateRouterOption.
        :type: ExternalGatewayInfoOption
        """
        self._external_gateway_info = external_gateway_info

    @property
    def routes(self):
        """Gets the routes of this NeutronUpdateRouterOption.

        功能说明：路由信息，见ListRoute详细说明

        :return: The routes of this NeutronUpdateRouterOption.
        :rtype: list[Route]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this NeutronUpdateRouterOption.

        功能说明：路由信息，见ListRoute详细说明

        :param routes: The routes of this NeutronUpdateRouterOption.
        :type: list[Route]
        """
        self._routes = routes

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NeutronUpdateRouterOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
