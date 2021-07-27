# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostRequest:


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
        'hostname': 'str',
        'policyname': 'str'
    }

    attribute_map = {
        'page': 'page',
        'pagesize': 'pagesize',
        'hostname': 'hostname',
        'policyname': 'policyname'
    }

    def __init__(self, page=None, pagesize=None, hostname=None, policyname=None):
        """ListHostRequest - a model defined in huaweicloud sdk"""
        
        

        self._page = None
        self._pagesize = None
        self._hostname = None
        self._policyname = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if hostname is not None:
            self.hostname = hostname
        if policyname is not None:
            self.policyname = policyname

    @property
    def page(self):
        """Gets the page of this ListHostRequest.

        页码

        :return: The page of this ListHostRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListHostRequest.

        页码

        :param page: The page of this ListHostRequest.
        :type: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListHostRequest.

        单页条数

        :return: The pagesize of this ListHostRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListHostRequest.

        单页条数

        :param pagesize: The pagesize of this ListHostRequest.
        :type: int
        """
        self._pagesize = pagesize

    @property
    def hostname(self):
        """Gets the hostname of this ListHostRequest.

        域名

        :return: The hostname of this ListHostRequest.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ListHostRequest.

        域名

        :param hostname: The hostname of this ListHostRequest.
        :type: str
        """
        self._hostname = hostname

    @property
    def policyname(self):
        """Gets the policyname of this ListHostRequest.

        策略名

        :return: The policyname of this ListHostRequest.
        :rtype: str
        """
        return self._policyname

    @policyname.setter
    def policyname(self, policyname):
        """Sets the policyname of this ListHostRequest.

        策略名

        :param policyname: The policyname of this ListHostRequest.
        :type: str
        """
        self._policyname = policyname

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
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other