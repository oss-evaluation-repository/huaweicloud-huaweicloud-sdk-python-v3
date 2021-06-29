# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class BatchUpdateUserResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'all_counts': 'int',
        'results': 'list[QueryUserResp]'
    }

    attribute_map = {
        'all_counts': 'all_counts',
        'results': 'results'
    }

    def __init__(self, all_counts=None, results=None):
        """BatchUpdateUserResponse - a model defined in huaweicloud sdk"""
        
        super(BatchUpdateUserResponse, self).__init__()

        self._all_counts = None
        self._results = None
        self.discriminator = None

        if all_counts is not None:
            self.all_counts = all_counts
        if results is not None:
            self.results = results

    @property
    def all_counts(self):
        """Gets the all_counts of this BatchUpdateUserResponse.

        总数

        :return: The all_counts of this BatchUpdateUserResponse.
        :rtype: int
        """
        return self._all_counts

    @all_counts.setter
    def all_counts(self, all_counts):
        """Sets the all_counts of this BatchUpdateUserResponse.

        总数

        :param all_counts: The all_counts of this BatchUpdateUserResponse.
        :type: int
        """
        self._all_counts = all_counts

    @property
    def results(self):
        """Gets the results of this BatchUpdateUserResponse.

        迁移用户信息

        :return: The results of this BatchUpdateUserResponse.
        :rtype: list[QueryUserResp]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this BatchUpdateUserResponse.

        迁移用户信息

        :param results: The results of this BatchUpdateUserResponse.
        :type: list[QueryUserResp]
        """
        self._results = results

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchUpdateUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other