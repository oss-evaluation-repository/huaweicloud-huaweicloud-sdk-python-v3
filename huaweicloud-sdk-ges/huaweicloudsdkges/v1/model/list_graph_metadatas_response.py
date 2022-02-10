# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGraphMetadatasResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_message': 'str',
        'error_code': 'str',
        'ges_metadata': 'GesMetaData'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'error_code': 'errorCode',
        'ges_metadata': 'gesMetadata'
    }

    def __init__(self, error_message=None, error_code=None, ges_metadata=None):
        """ListGraphMetadatasResponse - a model defined in huaweicloud sdk"""
        
        super(ListGraphMetadatasResponse, self).__init__()

        self._error_message = None
        self._error_code = None
        self._ges_metadata = None
        self.discriminator = None

        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code
        if ges_metadata is not None:
            self.ges_metadata = ges_metadata

    @property
    def error_message(self):
        """Gets the error_message of this ListGraphMetadatasResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :return: The error_message of this ListGraphMetadatasResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ListGraphMetadatasResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :param error_message: The error_message of this ListGraphMetadatasResponse.
        :type: str
        """
        self._error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this ListGraphMetadatasResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :return: The error_code of this ListGraphMetadatasResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListGraphMetadatasResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :param error_code: The error_code of this ListGraphMetadatasResponse.
        :type: str
        """
        self._error_code = error_code

    @property
    def ges_metadata(self):
        """Gets the ges_metadata of this ListGraphMetadatasResponse.


        :return: The ges_metadata of this ListGraphMetadatasResponse.
        :rtype: GesMetaData
        """
        return self._ges_metadata

    @ges_metadata.setter
    def ges_metadata(self, ges_metadata):
        """Sets the ges_metadata of this ListGraphMetadatasResponse.


        :param ges_metadata: The ges_metadata of this ListGraphMetadatasResponse.
        :type: GesMetaData
        """
        self._ges_metadata = ges_metadata

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
        if not isinstance(other, ListGraphMetadatasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other