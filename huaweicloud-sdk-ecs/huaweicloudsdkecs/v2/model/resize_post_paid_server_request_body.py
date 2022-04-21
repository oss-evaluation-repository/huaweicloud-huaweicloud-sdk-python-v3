# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizePostPaidServerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resize': 'ResizePostPaidServerOption'
    }

    attribute_map = {
        'resize': 'resize'
    }

    def __init__(self, resize=None):
        """ResizePostPaidServerRequestBody

        The model defined in huaweicloud sdk

        :param resize: 
        :type resize: :class:`huaweicloudsdkecs.v2.ResizePostPaidServerOption`
        """
        
        

        self._resize = None
        self.discriminator = None

        self.resize = resize

    @property
    def resize(self):
        """Gets the resize of this ResizePostPaidServerRequestBody.


        :return: The resize of this ResizePostPaidServerRequestBody.
        :rtype: :class:`huaweicloudsdkecs.v2.ResizePostPaidServerOption`
        """
        return self._resize

    @resize.setter
    def resize(self, resize):
        """Sets the resize of this ResizePostPaidServerRequestBody.


        :param resize: The resize of this ResizePostPaidServerRequestBody.
        :type resize: :class:`huaweicloudsdkecs.v2.ResizePostPaidServerOption`
        """
        self._resize = resize

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
        if not isinstance(other, ResizePostPaidServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
