# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCatalogDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'catalog_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'catalog_id': 'catalog_id'
    }

    def __init__(self, workspace=None, catalog_id=None):
        """ShowCatalogDetailRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param catalog_id: 目录编号
        :type catalog_id: str
        """
        
        

        self._workspace = None
        self._catalog_id = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.catalog_id = catalog_id

    @property
    def workspace(self):
        """Gets the workspace of this ShowCatalogDetailRequest.

        工作空间id

        :return: The workspace of this ShowCatalogDetailRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowCatalogDetailRequest.

        工作空间id

        :param workspace: The workspace of this ShowCatalogDetailRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def catalog_id(self):
        """Gets the catalog_id of this ShowCatalogDetailRequest.

        目录编号

        :return: The catalog_id of this ShowCatalogDetailRequest.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this ShowCatalogDetailRequest.

        目录编号

        :param catalog_id: The catalog_id of this ShowCatalogDetailRequest.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

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
        if not isinstance(other, ShowCatalogDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
