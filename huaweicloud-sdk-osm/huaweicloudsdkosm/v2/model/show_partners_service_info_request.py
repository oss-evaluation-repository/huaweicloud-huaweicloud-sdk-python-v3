# coding: utf-8

import pprint
import re

import six





class ShowPartnersServiceInfoRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'case_sub_type_id': 'str',
        'product_id': 'str',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'case_sub_type_id': 'case_sub_type_id',
        'product_id': 'product_id',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, case_sub_type_id=None, product_id=None, x_site=None, x_language=None, x_time_zone=None):
        """ShowPartnersServiceInfoRequest - a model defined in huaweicloud sdk"""
        
        

        self._case_sub_type_id = None
        self._product_id = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        if case_sub_type_id is not None:
            self.case_sub_type_id = case_sub_type_id
        if product_id is not None:
            self.product_id = product_id
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def case_sub_type_id(self):
        """Gets the case_sub_type_id of this ShowPartnersServiceInfoRequest.

        工单子类

        :return: The case_sub_type_id of this ShowPartnersServiceInfoRequest.
        :rtype: str
        """
        return self._case_sub_type_id

    @case_sub_type_id.setter
    def case_sub_type_id(self, case_sub_type_id):
        """Sets the case_sub_type_id of this ShowPartnersServiceInfoRequest.

        工单子类

        :param case_sub_type_id: The case_sub_type_id of this ShowPartnersServiceInfoRequest.
        :type: str
        """
        self._case_sub_type_id = case_sub_type_id

    @property
    def product_id(self):
        """Gets the product_id of this ShowPartnersServiceInfoRequest.

        ISV产品Id

        :return: The product_id of this ShowPartnersServiceInfoRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowPartnersServiceInfoRequest.

        ISV产品Id

        :param product_id: The product_id of this ShowPartnersServiceInfoRequest.
        :type: str
        """
        self._product_id = product_id

    @property
    def x_site(self):
        """Gets the x_site of this ShowPartnersServiceInfoRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this ShowPartnersServiceInfoRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ShowPartnersServiceInfoRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this ShowPartnersServiceInfoRequest.
        :type: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ShowPartnersServiceInfoRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this ShowPartnersServiceInfoRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowPartnersServiceInfoRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this ShowPartnersServiceInfoRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this ShowPartnersServiceInfoRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this ShowPartnersServiceInfoRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this ShowPartnersServiceInfoRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this ShowPartnersServiceInfoRequest.
        :type: str
        """
        self._x_time_zone = x_time_zone

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowPartnersServiceInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other