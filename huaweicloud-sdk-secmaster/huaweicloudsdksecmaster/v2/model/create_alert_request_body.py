# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_object': 'CreateAlert'
    }

    attribute_map = {
        'data_object': 'data_object'
    }

    def __init__(self, data_object=None):
        """CreateAlertRequestBody

        The model defined in huaweicloud sdk

        :param data_object: 
        :type data_object: :class:`huaweicloudsdksecmaster.v2.CreateAlert`
        """
        
        

        self._data_object = None
        self.discriminator = None

        if data_object is not None:
            self.data_object = data_object

    @property
    def data_object(self):
        """Gets the data_object of this CreateAlertRequestBody.

        :return: The data_object of this CreateAlertRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAlert`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        """Sets the data_object of this CreateAlertRequestBody.

        :param data_object: The data_object of this CreateAlertRequestBody.
        :type data_object: :class:`huaweicloudsdksecmaster.v2.CreateAlert`
        """
        self._data_object = data_object

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
        if not isinstance(other, CreateAlertRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
