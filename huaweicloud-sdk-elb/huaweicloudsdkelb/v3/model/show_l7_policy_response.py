# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowL7PolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'l7policy': 'L7Policy'
    }

    attribute_map = {
        'request_id': 'request_id',
        'l7policy': 'l7policy'
    }

    def __init__(self, request_id=None, l7policy=None):
        """ShowL7PolicyResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。  注：自动生成 。
        :type request_id: str
        :param l7policy: 
        :type l7policy: :class:`huaweicloudsdkelb.v3.L7Policy`
        """
        
        super(ShowL7PolicyResponse, self).__init__()

        self._request_id = None
        self._l7policy = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if l7policy is not None:
            self.l7policy = l7policy

    @property
    def request_id(self):
        """Gets the request_id of this ShowL7PolicyResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ShowL7PolicyResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowL7PolicyResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ShowL7PolicyResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def l7policy(self):
        """Gets the l7policy of this ShowL7PolicyResponse.


        :return: The l7policy of this ShowL7PolicyResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.L7Policy`
        """
        return self._l7policy

    @l7policy.setter
    def l7policy(self, l7policy):
        """Sets the l7policy of this ShowL7PolicyResponse.


        :param l7policy: The l7policy of this ShowL7PolicyResponse.
        :type l7policy: :class:`huaweicloudsdkelb.v3.L7Policy`
        """
        self._l7policy = l7policy

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
        if not isinstance(other, ShowL7PolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
