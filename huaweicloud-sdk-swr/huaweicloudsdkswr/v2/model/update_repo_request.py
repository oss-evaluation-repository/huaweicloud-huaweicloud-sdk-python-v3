# coding: utf-8

import re
import six





class UpdateRepoRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'body': 'UpdateRepoRequestBody'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'body': 'body'
    }

    def __init__(self, namespace=None, repository=None, body=None):
        """UpdateRepoRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._repository = None
        self._body = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        if body is not None:
            self.body = body

    @property
    def namespace(self):
        """Gets the namespace of this UpdateRepoRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this UpdateRepoRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this UpdateRepoRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this UpdateRepoRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this UpdateRepoRequest.

        镜像仓库名称。小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，小数点、斜杠、下划线、中划线不能直接相连），小写字母或数字结尾，1-128个字符。

        :return: The repository of this UpdateRepoRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this UpdateRepoRequest.

        镜像仓库名称。小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，小数点、斜杠、下划线、中划线不能直接相连），小写字母或数字结尾，1-128个字符。

        :param repository: The repository of this UpdateRepoRequest.
        :type: str
        """
        self._repository = repository

    @property
    def body(self):
        """Gets the body of this UpdateRepoRequest.


        :return: The body of this UpdateRepoRequest.
        :rtype: UpdateRepoRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateRepoRequest.


        :param body: The body of this UpdateRepoRequest.
        :type: UpdateRepoRequestBody
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateRepoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
