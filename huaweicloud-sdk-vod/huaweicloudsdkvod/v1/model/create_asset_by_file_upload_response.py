# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateAssetByFileUploadResponse(SdkResponse):


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
        'video_upload_url': 'str',
        'cover_upload_url': 'str',
        'subtitle_upload_urls': 'list[str]',
        'target': 'FileAddr'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'video_upload_url': 'video_upload_url',
        'cover_upload_url': 'cover_upload_url',
        'subtitle_upload_urls': 'subtitle_upload_urls',
        'target': 'target'
    }

    def __init__(self, asset_id=None, video_upload_url=None, cover_upload_url=None, subtitle_upload_urls=None, target=None):
        """CreateAssetByFileUploadResponse - a model defined in huaweicloud sdk"""
        
        super(CreateAssetByFileUploadResponse, self).__init__()

        self._asset_id = None
        self._video_upload_url = None
        self._cover_upload_url = None
        self._subtitle_upload_urls = None
        self._target = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if video_upload_url is not None:
            self.video_upload_url = video_upload_url
        if cover_upload_url is not None:
            self.cover_upload_url = cover_upload_url
        if subtitle_upload_urls is not None:
            self.subtitle_upload_urls = subtitle_upload_urls
        if target is not None:
            self.target = target

    @property
    def asset_id(self):
        """Gets the asset_id of this CreateAssetByFileUploadResponse.

        媒体ID<br/> 

        :return: The asset_id of this CreateAssetByFileUploadResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this CreateAssetByFileUploadResponse.

        媒体ID<br/> 

        :param asset_id: The asset_id of this CreateAssetByFileUploadResponse.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def video_upload_url(self):
        """Gets the video_upload_url of this CreateAssetByFileUploadResponse.

        视频上传URL<br/> 

        :return: The video_upload_url of this CreateAssetByFileUploadResponse.
        :rtype: str
        """
        return self._video_upload_url

    @video_upload_url.setter
    def video_upload_url(self, video_upload_url):
        """Sets the video_upload_url of this CreateAssetByFileUploadResponse.

        视频上传URL<br/> 

        :param video_upload_url: The video_upload_url of this CreateAssetByFileUploadResponse.
        :type: str
        """
        self._video_upload_url = video_upload_url

    @property
    def cover_upload_url(self):
        """Gets the cover_upload_url of this CreateAssetByFileUploadResponse.

        封面上传地址<br/> 

        :return: The cover_upload_url of this CreateAssetByFileUploadResponse.
        :rtype: str
        """
        return self._cover_upload_url

    @cover_upload_url.setter
    def cover_upload_url(self, cover_upload_url):
        """Sets the cover_upload_url of this CreateAssetByFileUploadResponse.

        封面上传地址<br/> 

        :param cover_upload_url: The cover_upload_url of this CreateAssetByFileUploadResponse.
        :type: str
        """
        self._cover_upload_url = cover_upload_url

    @property
    def subtitle_upload_urls(self):
        """Gets the subtitle_upload_urls of this CreateAssetByFileUploadResponse.

        字幕文件上传url数组<br/> 

        :return: The subtitle_upload_urls of this CreateAssetByFileUploadResponse.
        :rtype: list[str]
        """
        return self._subtitle_upload_urls

    @subtitle_upload_urls.setter
    def subtitle_upload_urls(self, subtitle_upload_urls):
        """Sets the subtitle_upload_urls of this CreateAssetByFileUploadResponse.

        字幕文件上传url数组<br/> 

        :param subtitle_upload_urls: The subtitle_upload_urls of this CreateAssetByFileUploadResponse.
        :type: list[str]
        """
        self._subtitle_upload_urls = subtitle_upload_urls

    @property
    def target(self):
        """Gets the target of this CreateAssetByFileUploadResponse.


        :return: The target of this CreateAssetByFileUploadResponse.
        :rtype: FileAddr
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this CreateAssetByFileUploadResponse.


        :param target: The target of this CreateAssetByFileUploadResponse.
        :type: FileAddr
        """
        self._target = target

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
        if not isinstance(other, CreateAssetByFileUploadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other