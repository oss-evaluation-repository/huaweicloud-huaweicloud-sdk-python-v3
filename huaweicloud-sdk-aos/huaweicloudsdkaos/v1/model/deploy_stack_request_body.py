# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployStackRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'executor': 'str',
        'template_body': 'str',
        'template_uri': 'str',
        'vars_structure': 'list[VarsStructure]',
        'vars_body': 'str',
        'vars_uri': 'str',
        'stack_id': 'str'
    }

    attribute_map = {
        'executor': 'executor',
        'template_body': 'template_body',
        'template_uri': 'template_uri',
        'vars_structure': 'vars_structure',
        'vars_body': 'vars_body',
        'vars_uri': 'vars_uri',
        'stack_id': 'stack_id'
    }

    def __init__(self, executor=None, template_body=None, template_uri=None, vars_structure=None, vars_body=None, vars_uri=None, stack_id=None):
        """DeployStackRequestBody

        The model defined in huaweicloud sdk

        :param executor: 执行操作者的名字，将用做未来的审计工作
        :type executor: str
        :param template_body: HCL模板，描述了资源的目标状态。RF将比较此模板与当前远程资源的状态之间的区别。  template_body和template_uri 必须有且只有一个存在 
        :type template_body: str
        :param template_uri: HCL模板的OBS地址，该模板描述了资源的目标状态  OBS地址必须为同region的OBS地址，暂不支持跨region访问  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以&#x60;.tf&#x60;或者&#x60;.tfjson&#x60;结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\&quot;.zip\&quot;结尾。解压后的文件不得包含\&quot;.tfvars\&quot;文件  template_body和template_uri 必须有且只有一个存在 
        :type template_uri: str
        :param vars_structure: HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        :param vars_body: HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 
        :type vars_body: str
        :param vars_uri: HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 
        :type vars_uri: str
        :param stack_id: 资源栈（stack）的唯一Id。  此Id由RF在生成资源栈的时候生成，为UUID。  由于堆栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的堆栈，删除，再重新创建一个同名堆栈。  对于团队并行开发，用户可能希望确保，当前我操作的堆栈就是我认为的那个，而不是其他队友删除后创建的同名堆栈。因此，使用ID就可以做到强匹配。  RF保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400 
        :type stack_id: str
        """
        
        

        self._executor = None
        self._template_body = None
        self._template_uri = None
        self._vars_structure = None
        self._vars_body = None
        self._vars_uri = None
        self._stack_id = None
        self.discriminator = None

        if executor is not None:
            self.executor = executor
        if template_body is not None:
            self.template_body = template_body
        if template_uri is not None:
            self.template_uri = template_uri
        if vars_structure is not None:
            self.vars_structure = vars_structure
        if vars_body is not None:
            self.vars_body = vars_body
        if vars_uri is not None:
            self.vars_uri = vars_uri
        if stack_id is not None:
            self.stack_id = stack_id

    @property
    def executor(self):
        """Gets the executor of this DeployStackRequestBody.

        执行操作者的名字，将用做未来的审计工作

        :return: The executor of this DeployStackRequestBody.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this DeployStackRequestBody.

        执行操作者的名字，将用做未来的审计工作

        :param executor: The executor of this DeployStackRequestBody.
        :type executor: str
        """
        self._executor = executor

    @property
    def template_body(self):
        """Gets the template_body of this DeployStackRequestBody.

        HCL模板，描述了资源的目标状态。RF将比较此模板与当前远程资源的状态之间的区别。  template_body和template_uri 必须有且只有一个存在 

        :return: The template_body of this DeployStackRequestBody.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        """Sets the template_body of this DeployStackRequestBody.

        HCL模板，描述了资源的目标状态。RF将比较此模板与当前远程资源的状态之间的区别。  template_body和template_uri 必须有且只有一个存在 

        :param template_body: The template_body of this DeployStackRequestBody.
        :type template_body: str
        """
        self._template_body = template_body

    @property
    def template_uri(self):
        """Gets the template_uri of this DeployStackRequestBody.

        HCL模板的OBS地址，该模板描述了资源的目标状态  OBS地址必须为同region的OBS地址，暂不支持跨region访问  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以`.tf`或者`.tfjson`结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\".zip\"结尾。解压后的文件不得包含\".tfvars\"文件  template_body和template_uri 必须有且只有一个存在 

        :return: The template_uri of this DeployStackRequestBody.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        """Sets the template_uri of this DeployStackRequestBody.

        HCL模板的OBS地址，该模板描述了资源的目标状态  OBS地址必须为同region的OBS地址，暂不支持跨region访问  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以`.tf`或者`.tfjson`结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\".zip\"结尾。解压后的文件不得包含\".tfvars\"文件  template_body和template_uri 必须有且只有一个存在 

        :param template_uri: The template_uri of this DeployStackRequestBody.
        :type template_uri: str
        """
        self._template_uri = template_uri

    @property
    def vars_structure(self):
        """Gets the vars_structure of this DeployStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 

        :return: The vars_structure of this DeployStackRequestBody.
        :rtype: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        """Sets the vars_structure of this DeployStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 

        :param vars_structure: The vars_structure of this DeployStackRequestBody.
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

    @property
    def vars_body(self):
        """Gets the vars_body of this DeployStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 

        :return: The vars_body of this DeployStackRequestBody.
        :rtype: str
        """
        return self._vars_body

    @vars_body.setter
    def vars_body(self, vars_body):
        """Sets the vars_body of this DeployStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 

        :param vars_body: The vars_body of this DeployStackRequestBody.
        :type vars_body: str
        """
        self._vars_body = vars_body

    @property
    def vars_uri(self):
        """Gets the vars_uri of this DeployStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 

        :return: The vars_uri of this DeployStackRequestBody.
        :rtype: str
        """
        return self._vars_uri

    @vars_uri.setter
    def vars_uri(self, vars_uri):
        """Sets the vars_uri of this DeployStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * RF支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars中不应该传递任何敏感信息，RF会直接明文使用、log、展示、存储对应的vars 

        :param vars_uri: The vars_uri of this DeployStackRequestBody.
        :type vars_uri: str
        """
        self._vars_uri = vars_uri

    @property
    def stack_id(self):
        """Gets the stack_id of this DeployStackRequestBody.

        资源栈（stack）的唯一Id。  此Id由RF在生成资源栈的时候生成，为UUID。  由于堆栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的堆栈，删除，再重新创建一个同名堆栈。  对于团队并行开发，用户可能希望确保，当前我操作的堆栈就是我认为的那个，而不是其他队友删除后创建的同名堆栈。因此，使用ID就可以做到强匹配。  RF保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400 

        :return: The stack_id of this DeployStackRequestBody.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this DeployStackRequestBody.

        资源栈（stack）的唯一Id。  此Id由RF在生成资源栈的时候生成，为UUID。  由于堆栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的堆栈，删除，再重新创建一个同名堆栈。  对于团队并行开发，用户可能希望确保，当前我操作的堆栈就是我认为的那个，而不是其他队友删除后创建的同名堆栈。因此，使用ID就可以做到强匹配。  RF保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400 

        :param stack_id: The stack_id of this DeployStackRequestBody.
        :type stack_id: str
        """
        self._stack_id = stack_id

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
        if not isinstance(other, DeployStackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other