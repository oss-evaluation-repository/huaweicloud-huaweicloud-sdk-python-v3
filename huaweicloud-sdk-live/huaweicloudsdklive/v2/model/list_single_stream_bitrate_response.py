# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSingleStreamBitrateResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bitrate_info_list': 'list[V2BitrateInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'bitrate_info_list': 'bitrate_info_list',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, bitrate_info_list=None, x_request_id=None):
        """ListSingleStreamBitrateResponse - a model defined in huaweicloud sdk"""
        
        super(ListSingleStreamBitrateResponse, self).__init__()

        self._bitrate_info_list = None
        self._x_request_id = None
        self.discriminator = None

        if bitrate_info_list is not None:
            self.bitrate_info_list = bitrate_info_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def bitrate_info_list(self):
        """Gets the bitrate_info_list of this ListSingleStreamBitrateResponse.

        用量详情。

        :return: The bitrate_info_list of this ListSingleStreamBitrateResponse.
        :rtype: list[V2BitrateInfo]
        """
        return self._bitrate_info_list

    @bitrate_info_list.setter
    def bitrate_info_list(self, bitrate_info_list):
        """Sets the bitrate_info_list of this ListSingleStreamBitrateResponse.

        用量详情。

        :param bitrate_info_list: The bitrate_info_list of this ListSingleStreamBitrateResponse.
        :type: list[V2BitrateInfo]
        """
        self._bitrate_info_list = bitrate_info_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListSingleStreamBitrateResponse.


        :return: The x_request_id of this ListSingleStreamBitrateResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListSingleStreamBitrateResponse.


        :param x_request_id: The x_request_id of this ListSingleStreamBitrateResponse.
        :type: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListSingleStreamBitrateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
