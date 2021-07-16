# coding: utf-8

import re
import six





class MigrateNodesSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'os': 'str',
        'extend_param': 'MigrateNodeExtendParam',
        'login': 'Login',
        'nodes': 'list[NodeItem]'
    }

    attribute_map = {
        'os': 'os',
        'extend_param': 'extendParam',
        'login': 'login',
        'nodes': 'nodes'
    }

    def __init__(self, os=None, extend_param=None, login=None, nodes=None):
        """MigrateNodesSpec - a model defined in huaweicloud sdk"""
        
        

        self._os = None
        self._extend_param = None
        self._login = None
        self._nodes = None
        self.discriminator = None

        self.os = os
        if extend_param is not None:
            self.extend_param = extend_param
        self.login = login
        if nodes is not None:
            self.nodes = nodes

    @property
    def os(self):
        """Gets the os of this MigrateNodesSpec.

        操作系统类型，须精确到版本号。 当指定“alpha.cce/NodeImageID”参数时，“os”参数必须和用户自定义镜像的操作系统一致。 

        :return: The os of this MigrateNodesSpec.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this MigrateNodesSpec.

        操作系统类型，须精确到版本号。 当指定“alpha.cce/NodeImageID”参数时，“os”参数必须和用户自定义镜像的操作系统一致。 

        :param os: The os of this MigrateNodesSpec.
        :type: str
        """
        self._os = os

    @property
    def extend_param(self):
        """Gets the extend_param of this MigrateNodesSpec.


        :return: The extend_param of this MigrateNodesSpec.
        :rtype: MigrateNodeExtendParam
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this MigrateNodesSpec.


        :param extend_param: The extend_param of this MigrateNodesSpec.
        :type: MigrateNodeExtendParam
        """
        self._extend_param = extend_param

    @property
    def login(self):
        """Gets the login of this MigrateNodesSpec.


        :return: The login of this MigrateNodesSpec.
        :rtype: Login
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this MigrateNodesSpec.


        :param login: The login of this MigrateNodesSpec.
        :type: Login
        """
        self._login = login

    @property
    def nodes(self):
        """Gets the nodes of this MigrateNodesSpec.

        待操作节点列表

        :return: The nodes of this MigrateNodesSpec.
        :rtype: list[NodeItem]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this MigrateNodesSpec.

        待操作节点列表

        :param nodes: The nodes of this MigrateNodesSpec.
        :type: list[NodeItem]
        """
        self._nodes = nodes

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
        if not isinstance(other, MigrateNodesSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other