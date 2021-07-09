# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListLabelsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'label_list': 'list[CaseLabelInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'label_list': 'label_list'
    }

    def __init__(self, total_count=None, label_list=None):
        """ListLabelsResponse - a model defined in huaweicloud sdk"""
        
        super(ListLabelsResponse, self).__init__()

        self._total_count = None
        self._label_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if label_list is not None:
            self.label_list = label_list

    @property
    def total_count(self):
        """Gets the total_count of this ListLabelsResponse.

        总数

        :return: The total_count of this ListLabelsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListLabelsResponse.

        总数

        :param total_count: The total_count of this ListLabelsResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def label_list(self):
        """Gets the label_list of this ListLabelsResponse.

        标签列表

        :return: The label_list of this ListLabelsResponse.
        :rtype: list[CaseLabelInfo]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        """Sets the label_list of this ListLabelsResponse.

        标签列表

        :param label_list: The label_list of this ListLabelsResponse.
        :type: list[CaseLabelInfo]
        """
        self._label_list = label_list

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
        if not isinstance(other, ListLabelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
