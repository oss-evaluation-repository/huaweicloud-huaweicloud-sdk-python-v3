# coding: utf-8

import pprint
import re

import six





class ListCertificatesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'pagesize': 'int',
        'name': 'str',
        'host': 'bool',
        'exp_status': 'int'
    }

    attribute_map = {
        'page': 'page',
        'pagesize': 'pagesize',
        'name': 'name',
        'host': 'host',
        'exp_status': 'exp_status'
    }

    def __init__(self, page=None, pagesize=None, name=None, host=None, exp_status=None):
        """ListCertificatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._page = None
        self._pagesize = None
        self._name = None
        self._host = None
        self._exp_status = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if exp_status is not None:
            self.exp_status = exp_status

    @property
    def page(self):
        """Gets the page of this ListCertificatesRequest.

        page

        :return: The page of this ListCertificatesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCertificatesRequest.

        page

        :param page: The page of this ListCertificatesRequest.
        :type: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListCertificatesRequest.

        pagesize

        :return: The pagesize of this ListCertificatesRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListCertificatesRequest.

        pagesize

        :param pagesize: The pagesize of this ListCertificatesRequest.
        :type: int
        """
        self._pagesize = pagesize

    @property
    def name(self):
        """Gets the name of this ListCertificatesRequest.

        证书名称

        :return: The name of this ListCertificatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCertificatesRequest.

        证书名称

        :param name: The name of this ListCertificatesRequest.
        :type: str
        """
        self._name = name

    @property
    def host(self):
        """Gets the host of this ListCertificatesRequest.

        是否获取证书关联的域名

        :return: The host of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListCertificatesRequest.

        是否获取证书关联的域名

        :param host: The host of this ListCertificatesRequest.
        :type: bool
        """
        self._host = host

    @property
    def exp_status(self):
        """Gets the exp_status of this ListCertificatesRequest.

        证书过期状态，0-未过期，1-已过期，2-即将过期

        :return: The exp_status of this ListCertificatesRequest.
        :rtype: int
        """
        return self._exp_status

    @exp_status.setter
    def exp_status(self, exp_status):
        """Sets the exp_status of this ListCertificatesRequest.

        证书过期状态，0-未过期，1-已过期，2-即将过期

        :param exp_status: The exp_status of this ListCertificatesRequest.
        :type: int
        """
        self._exp_status = exp_status

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
        if not isinstance(other, ListCertificatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other