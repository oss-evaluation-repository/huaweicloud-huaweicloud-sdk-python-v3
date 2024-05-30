# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCertificateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'certificate_id': 'str',
        'body': 'UpdateCertificateDTO'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'certificate_id': 'certificate_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, certificate_id=None, body=None):
        """UpdateCertificateRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。
        :type instance_id: str
        :param certificate_id: CA证书ID，在上传CA证书时由平台分配的唯一标识。
        :type certificate_id: str
        :param body: Body of the UpdateCertificateRequest
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateCertificateDTO`
        """
        
        

        self._instance_id = None
        self._certificate_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.certificate_id = certificate_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateCertificateRequest.

        实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :return: The instance_id of this UpdateCertificateRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateCertificateRequest.

        实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :param instance_id: The instance_id of this UpdateCertificateRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this UpdateCertificateRequest.

        CA证书ID，在上传CA证书时由平台分配的唯一标识。

        :return: The certificate_id of this UpdateCertificateRequest.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this UpdateCertificateRequest.

        CA证书ID，在上传CA证书时由平台分配的唯一标识。

        :param certificate_id: The certificate_id of this UpdateCertificateRequest.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def body(self):
        """Gets the body of this UpdateCertificateRequest.

        :return: The body of this UpdateCertificateRequest.
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateCertificateDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateCertificateRequest.

        :param body: The body of this UpdateCertificateRequest.
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateCertificateDTO`
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
        if not isinstance(other, UpdateCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other