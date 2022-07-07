# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpPutBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'https_status': 'str',
        'certificate_name': 'str',
        'certificate_value': 'str',
        'private_key': 'str',
        'certificate_source': 'int',
        'http2_status': 'str'
    }

    attribute_map = {
        'https_status': 'https_status',
        'certificate_name': 'certificate_name',
        'certificate_value': 'certificate_value',
        'private_key': 'private_key',
        'certificate_source': 'certificate_source',
        'http2_status': 'http2_status'
    }

    def __init__(self, https_status=None, certificate_name=None, certificate_value=None, private_key=None, certificate_source=None, http2_status=None):
        """HttpPutBody

        The model defined in huaweicloud sdk

        :param https_status: HTTPS证书是否启用。（on：开启，off：关闭）
        :type https_status: str
        :param certificate_name: 证书名字。（长度限制为3-32字符）。当证书开启时必传。
        :type certificate_name: str
        :param certificate_value: HTTPS协议使用的证书内容，当证书开启时必传。取值范围：PEM编码格式。
        :type certificate_value: str
        :param private_key: HTTPS协议使用的私钥，当证书开启时必传。取值范围：PEM编码格式。
        :type private_key: str
        :param certificate_source: 证书来源。1：代表华为云托管证书；0：表示自有证书。 默认值0。当证书开启时必传。
        :type certificate_source: int
        :param http2_status: 是否使用HTTP2.0。（on：是，off：否。）,默认关闭，https_status&#x3D;off时，该值不生效。
        :type http2_status: str
        """
        
        

        self._https_status = None
        self._certificate_name = None
        self._certificate_value = None
        self._private_key = None
        self._certificate_source = None
        self._http2_status = None
        self.discriminator = None

        if https_status is not None:
            self.https_status = https_status
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if certificate_value is not None:
            self.certificate_value = certificate_value
        if private_key is not None:
            self.private_key = private_key
        if certificate_source is not None:
            self.certificate_source = certificate_source
        if http2_status is not None:
            self.http2_status = http2_status

    @property
    def https_status(self):
        """Gets the https_status of this HttpPutBody.

        HTTPS证书是否启用。（on：开启，off：关闭）

        :return: The https_status of this HttpPutBody.
        :rtype: str
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this HttpPutBody.

        HTTPS证书是否启用。（on：开启，off：关闭）

        :param https_status: The https_status of this HttpPutBody.
        :type https_status: str
        """
        self._https_status = https_status

    @property
    def certificate_name(self):
        """Gets the certificate_name of this HttpPutBody.

        证书名字。（长度限制为3-32字符）。当证书开启时必传。

        :return: The certificate_name of this HttpPutBody.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this HttpPutBody.

        证书名字。（长度限制为3-32字符）。当证书开启时必传。

        :param certificate_name: The certificate_name of this HttpPutBody.
        :type certificate_name: str
        """
        self._certificate_name = certificate_name

    @property
    def certificate_value(self):
        """Gets the certificate_value of this HttpPutBody.

        HTTPS协议使用的证书内容，当证书开启时必传。取值范围：PEM编码格式。

        :return: The certificate_value of this HttpPutBody.
        :rtype: str
        """
        return self._certificate_value

    @certificate_value.setter
    def certificate_value(self, certificate_value):
        """Sets the certificate_value of this HttpPutBody.

        HTTPS协议使用的证书内容，当证书开启时必传。取值范围：PEM编码格式。

        :param certificate_value: The certificate_value of this HttpPutBody.
        :type certificate_value: str
        """
        self._certificate_value = certificate_value

    @property
    def private_key(self):
        """Gets the private_key of this HttpPutBody.

        HTTPS协议使用的私钥，当证书开启时必传。取值范围：PEM编码格式。

        :return: The private_key of this HttpPutBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this HttpPutBody.

        HTTPS协议使用的私钥，当证书开启时必传。取值范围：PEM编码格式。

        :param private_key: The private_key of this HttpPutBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate_source(self):
        """Gets the certificate_source of this HttpPutBody.

        证书来源。1：代表华为云托管证书；0：表示自有证书。 默认值0。当证书开启时必传。

        :return: The certificate_source of this HttpPutBody.
        :rtype: int
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        """Sets the certificate_source of this HttpPutBody.

        证书来源。1：代表华为云托管证书；0：表示自有证书。 默认值0。当证书开启时必传。

        :param certificate_source: The certificate_source of this HttpPutBody.
        :type certificate_source: int
        """
        self._certificate_source = certificate_source

    @property
    def http2_status(self):
        """Gets the http2_status of this HttpPutBody.

        是否使用HTTP2.0。（on：是，off：否。）,默认关闭，https_status=off时，该值不生效。

        :return: The http2_status of this HttpPutBody.
        :rtype: str
        """
        return self._http2_status

    @http2_status.setter
    def http2_status(self, http2_status):
        """Sets the http2_status of this HttpPutBody.

        是否使用HTTP2.0。（on：是，off：否。）,默认关闭，https_status=off时，该值不生效。

        :param http2_status: The http2_status of this HttpPutBody.
        :type http2_status: str
        """
        self._http2_status = http2_status

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
        if not isinstance(other, HttpPutBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other