# coding: utf-8

import re
import six





class UpdateCoverByThumbnailReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'thumbnail_url': 'str'
    }

    attribute_map = {
        'thumbnail_url': 'thumbnailUrl'
    }

    def __init__(self, thumbnail_url=None):
        """UpdateCoverByThumbnailReq - a model defined in huaweicloud sdk"""
        
        

        self._thumbnail_url = None
        self.discriminator = None

        self.thumbnail_url = thumbnail_url

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this UpdateCoverByThumbnailReq.

        截图文件的URL。  需要根据媒资ID调用[查询媒资详细信息](https://support.huaweicloud.com/api-vod/vod_04_0202.html)接口获取媒资的截图文件URL。

        :return: The thumbnail_url of this UpdateCoverByThumbnailReq.
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this UpdateCoverByThumbnailReq.

        截图文件的URL。  需要根据媒资ID调用[查询媒资详细信息](https://support.huaweicloud.com/api-vod/vod_04_0202.html)接口获取媒资的截图文件URL。

        :param thumbnail_url: The thumbnail_url of this UpdateCoverByThumbnailReq.
        :type: str
        """
        self._thumbnail_url = thumbnail_url

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
        if not isinstance(other, UpdateCoverByThumbnailReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
