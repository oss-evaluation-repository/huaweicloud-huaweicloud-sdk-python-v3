# coding: utf-8

import re
import six





class CreateRepoRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'repository': 'str',
        'is_public': 'bool',
        'category': 'str',
        'description': 'str'
    }

    attribute_map = {
        'repository': 'repository',
        'is_public': 'is_public',
        'category': 'category',
        'description': 'description'
    }

    def __init__(self, repository=None, is_public=None, category=None, description=None):
        """CreateRepoRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._repository = None
        self._is_public = None
        self._category = None
        self._description = None
        self.discriminator = None

        self.repository = repository
        self.is_public = is_public
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description

    @property
    def repository(self):
        """Gets the repository of this CreateRepoRequestBody.

        镜像仓库名称。小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，小数点、斜杠、下划线、中划线不能直接相连），小写字母或数字结尾，1-128个字符。

        :return: The repository of this CreateRepoRequestBody.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this CreateRepoRequestBody.

        镜像仓库名称。小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，小数点、斜杠、下划线、中划线不能直接相连），小写字母或数字结尾，1-128个字符。

        :param repository: The repository of this CreateRepoRequestBody.
        :type: str
        """
        self._repository = repository

    @property
    def is_public(self):
        """Gets the is_public of this CreateRepoRequestBody.

        是否为公共仓库，可选值为true或false。

        :return: The is_public of this CreateRepoRequestBody.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this CreateRepoRequestBody.

        是否为公共仓库，可选值为true或false。

        :param is_public: The is_public of this CreateRepoRequestBody.
        :type: bool
        """
        self._is_public = is_public

    @property
    def category(self):
        """Gets the category of this CreateRepoRequestBody.

        仓库类型，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。

        :return: The category of this CreateRepoRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CreateRepoRequestBody.

        仓库类型，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。

        :param category: The category of this CreateRepoRequestBody.
        :type: str
        """
        self._category = category

    @property
    def description(self):
        """Gets the description of this CreateRepoRequestBody.

        镜像仓库的描述信息。

        :return: The description of this CreateRepoRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRepoRequestBody.

        镜像仓库的描述信息。

        :param description: The description of this CreateRepoRequestBody.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, CreateRepoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
