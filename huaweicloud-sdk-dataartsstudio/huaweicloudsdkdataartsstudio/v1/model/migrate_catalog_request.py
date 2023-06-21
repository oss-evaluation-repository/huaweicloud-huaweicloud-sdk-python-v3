# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateCatalogRequest:

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
        'catalog_id': 'str',
        'body': 'CatalogMoveParaDTO'
    }

    attribute_map = {
        'workspace': 'workspace',
        'catalog_id': 'catalog_id',
        'body': 'body'
    }

    def __init__(self, workspace=None, catalog_id=None, body=None):
        """MigrateCatalogRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param catalog_id: 目录编号
        :type catalog_id: str
        :param body: Body of the MigrateCatalogRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.CatalogMoveParaDTO`
        """
        
        

        self._workspace = None
        self._catalog_id = None
        self._body = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.catalog_id = catalog_id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this MigrateCatalogRequest.

        工作空间id

        :return: The workspace of this MigrateCatalogRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this MigrateCatalogRequest.

        工作空间id

        :param workspace: The workspace of this MigrateCatalogRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def catalog_id(self):
        """Gets the catalog_id of this MigrateCatalogRequest.

        目录编号

        :return: The catalog_id of this MigrateCatalogRequest.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this MigrateCatalogRequest.

        目录编号

        :param catalog_id: The catalog_id of this MigrateCatalogRequest.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def body(self):
        """Gets the body of this MigrateCatalogRequest.

        :return: The body of this MigrateCatalogRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CatalogMoveParaDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this MigrateCatalogRequest.

        :param body: The body of this MigrateCatalogRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.CatalogMoveParaDTO`
        """
        self._body = body

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
        if not isinstance(other, MigrateCatalogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
