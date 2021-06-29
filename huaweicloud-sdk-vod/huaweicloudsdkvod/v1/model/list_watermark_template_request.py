# coding: utf-8

import pprint
import re

import six





class ListWatermarkTemplateRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'list[str]',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, id=None, page=None, size=None):
        """ListWatermarkTemplateRequest - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._page = None
        self._size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def id(self):
        """Gets the id of this ListWatermarkTemplateRequest.

        水印模板配置id，一次最多10个<br/> 

        :return: The id of this ListWatermarkTemplateRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListWatermarkTemplateRequest.

        水印模板配置id，一次最多10个<br/> 

        :param id: The id of this ListWatermarkTemplateRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def page(self):
        """Gets the page of this ListWatermarkTemplateRequest.

        分页编号。默认为0。指定id时该参数无效。<br/> 

        :return: The page of this ListWatermarkTemplateRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListWatermarkTemplateRequest.

        分页编号。默认为0。指定id时该参数无效。<br/> 

        :param page: The page of this ListWatermarkTemplateRequest.
        :type: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListWatermarkTemplateRequest.

        每页记录数。默认为10，范围[1,100]。指定id时该参数无效。<br/> 

        :return: The size of this ListWatermarkTemplateRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListWatermarkTemplateRequest.

        每页记录数。默认为10，范围[1,100]。指定id时该参数无效。<br/> 

        :param size: The size of this ListWatermarkTemplateRequest.
        :type: int
        """
        self._size = size

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
        if not isinstance(other, ListWatermarkTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other