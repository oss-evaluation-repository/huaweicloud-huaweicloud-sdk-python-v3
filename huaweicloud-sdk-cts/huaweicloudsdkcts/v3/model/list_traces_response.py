# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListTracesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'traces': 'list[Traces]',
        'meta_data': 'MetaData'
    }

    attribute_map = {
        'traces': 'traces',
        'meta_data': 'meta_data'
    }

    def __init__(self, traces=None, meta_data=None):
        """ListTracesResponse - a model defined in huaweicloud sdk"""
        
        super(ListTracesResponse, self).__init__()

        self._traces = None
        self._meta_data = None
        self.discriminator = None

        if traces is not None:
            self.traces = traces
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def traces(self):
        """Gets the traces of this ListTracesResponse.

        本次查询事件列表返回事件数组。

        :return: The traces of this ListTracesResponse.
        :rtype: list[Traces]
        """
        return self._traces

    @traces.setter
    def traces(self, traces):
        """Sets the traces of this ListTracesResponse.

        本次查询事件列表返回事件数组。

        :param traces: The traces of this ListTracesResponse.
        :type: list[Traces]
        """
        self._traces = traces

    @property
    def meta_data(self):
        """Gets the meta_data of this ListTracesResponse.


        :return: The meta_data of this ListTracesResponse.
        :rtype: MetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ListTracesResponse.


        :param meta_data: The meta_data of this ListTracesResponse.
        :type: MetaData
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ListTracesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
