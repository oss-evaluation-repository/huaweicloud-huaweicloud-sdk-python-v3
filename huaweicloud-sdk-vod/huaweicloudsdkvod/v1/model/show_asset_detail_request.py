# coding: utf-8

import re
import six





class ShowAssetDetailRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'categories': 'categories'
    }

    def __init__(self, asset_id=None, categories=None):
        """ShowAssetDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._asset_id = None
        self._categories = None
        self.discriminator = None

        self.asset_id = asset_id
        if categories is not None:
            self.categories = categories

    @property
    def asset_id(self):
        """Gets the asset_id of this ShowAssetDetailRequest.

        媒资ID。

        :return: The asset_id of this ShowAssetDetailRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ShowAssetDetailRequest.

        媒资ID。

        :param asset_id: The asset_id of this ShowAssetDetailRequest.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def categories(self):
        """Gets the categories of this ShowAssetDetailRequest.

        查询的信息类型。 - 为空时表示查询所有信息。 - 不为空时支持同时查询一个或者多个类型的信息，取值如下： - - base_info：媒资基本信息。 - - transcode_info：转码结果信息。 - - thumbnail_info：截图结果信息。 - - review_info：审核结果信息。

        :return: The categories of this ShowAssetDetailRequest.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ShowAssetDetailRequest.

        查询的信息类型。 - 为空时表示查询所有信息。 - 不为空时支持同时查询一个或者多个类型的信息，取值如下： - - base_info：媒资基本信息。 - - transcode_info：转码结果信息。 - - thumbnail_info：截图结果信息。 - - review_info：审核结果信息。

        :param categories: The categories of this ShowAssetDetailRequest.
        :type: list[str]
        """
        self._categories = categories

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
        if not isinstance(other, ShowAssetDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
