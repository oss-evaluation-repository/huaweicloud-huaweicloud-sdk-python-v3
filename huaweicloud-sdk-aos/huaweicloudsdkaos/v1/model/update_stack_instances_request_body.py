# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStackInstancesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_set_id': 'str',
        'deployment_targets': 'DeploymentTargets',
        'var_overrides': 'VarOverridesPrimitiveTypeHolderVarOverrides',
        'operation_preferences': 'OperationPreferences'
    }

    attribute_map = {
        'stack_set_id': 'stack_set_id',
        'deployment_targets': 'deployment_targets',
        'var_overrides': 'var_overrides',
        'operation_preferences': 'operation_preferences'
    }

    def __init__(self, stack_set_id=None, deployment_targets=None, var_overrides=None, operation_preferences=None):
        """UpdateStackInstancesRequestBody

        The model defined in huaweicloud sdk

        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param deployment_targets: 
        :type deployment_targets: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        :param var_overrides: 
        :type var_overrides: :class:`huaweicloudsdkaos.v1.VarOverridesPrimitiveTypeHolderVarOverrides`
        :param operation_preferences: 
        :type operation_preferences: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        """
        
        

        self._stack_set_id = None
        self._deployment_targets = None
        self._var_overrides = None
        self._operation_preferences = None
        self.discriminator = None

        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        self.deployment_targets = deployment_targets
        if var_overrides is not None:
            self.var_overrides = var_overrides
        if operation_preferences is not None:
            self.operation_preferences = operation_preferences

    @property
    def stack_set_id(self):
        """Gets the stack_set_id of this UpdateStackInstancesRequestBody.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this UpdateStackInstancesRequestBody.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        """Sets the stack_set_id of this UpdateStackInstancesRequestBody.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this UpdateStackInstancesRequestBody.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def deployment_targets(self):
        """Gets the deployment_targets of this UpdateStackInstancesRequestBody.

        :return: The deployment_targets of this UpdateStackInstancesRequestBody.
        :rtype: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        return self._deployment_targets

    @deployment_targets.setter
    def deployment_targets(self, deployment_targets):
        """Sets the deployment_targets of this UpdateStackInstancesRequestBody.

        :param deployment_targets: The deployment_targets of this UpdateStackInstancesRequestBody.
        :type deployment_targets: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        self._deployment_targets = deployment_targets

    @property
    def var_overrides(self):
        """Gets the var_overrides of this UpdateStackInstancesRequestBody.

        :return: The var_overrides of this UpdateStackInstancesRequestBody.
        :rtype: :class:`huaweicloudsdkaos.v1.VarOverridesPrimitiveTypeHolderVarOverrides`
        """
        return self._var_overrides

    @var_overrides.setter
    def var_overrides(self, var_overrides):
        """Sets the var_overrides of this UpdateStackInstancesRequestBody.

        :param var_overrides: The var_overrides of this UpdateStackInstancesRequestBody.
        :type var_overrides: :class:`huaweicloudsdkaos.v1.VarOverridesPrimitiveTypeHolderVarOverrides`
        """
        self._var_overrides = var_overrides

    @property
    def operation_preferences(self):
        """Gets the operation_preferences of this UpdateStackInstancesRequestBody.

        :return: The operation_preferences of this UpdateStackInstancesRequestBody.
        :rtype: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        """
        return self._operation_preferences

    @operation_preferences.setter
    def operation_preferences(self, operation_preferences):
        """Sets the operation_preferences of this UpdateStackInstancesRequestBody.

        :param operation_preferences: The operation_preferences of this UpdateStackInstancesRequestBody.
        :type operation_preferences: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        """
        self._operation_preferences = operation_preferences

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
        if not isinstance(other, UpdateStackInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
