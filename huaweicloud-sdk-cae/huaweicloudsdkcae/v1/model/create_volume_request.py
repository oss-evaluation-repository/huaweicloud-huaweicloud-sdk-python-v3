# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVolumeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_environment_id': 'str',
        'x_enterprise_project_id': 'str',
        'body': 'CreateVolumeReq'
    }

    attribute_map = {
        'x_environment_id': 'X-Environment-ID',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'body': 'body'
    }

    def __init__(self, x_environment_id=None, x_enterprise_project_id=None, body=None):
        """CreateVolumeRequest

        The model defined in huaweicloud sdk

        :param x_environment_id: 环境id。
        :type x_environment_id: str
        :param x_enterprise_project_id: 租户的企业项目id。
        :type x_enterprise_project_id: str
        :param body: Body of the CreateVolumeRequest
        :type body: :class:`huaweicloudsdkcae.v1.CreateVolumeReq`
        """
        
        

        self._x_environment_id = None
        self._x_enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.x_environment_id = x_environment_id
        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def x_environment_id(self):
        """Gets the x_environment_id of this CreateVolumeRequest.

        环境id。

        :return: The x_environment_id of this CreateVolumeRequest.
        :rtype: str
        """
        return self._x_environment_id

    @x_environment_id.setter
    def x_environment_id(self, x_environment_id):
        """Sets the x_environment_id of this CreateVolumeRequest.

        环境id。

        :param x_environment_id: The x_environment_id of this CreateVolumeRequest.
        :type x_environment_id: str
        """
        self._x_environment_id = x_environment_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this CreateVolumeRequest.

        租户的企业项目id。

        :return: The x_enterprise_project_id of this CreateVolumeRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this CreateVolumeRequest.

        租户的企业项目id。

        :param x_enterprise_project_id: The x_enterprise_project_id of this CreateVolumeRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def body(self):
        """Gets the body of this CreateVolumeRequest.


        :return: The body of this CreateVolumeRequest.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateVolumeReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateVolumeRequest.


        :param body: The body of this CreateVolumeRequest.
        :type body: :class:`huaweicloudsdkcae.v1.CreateVolumeReq`
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
        if not isinstance(other, CreateVolumeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other