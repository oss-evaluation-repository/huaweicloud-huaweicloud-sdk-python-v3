# coding: utf-8

import pprint
import re

import six





class QualityInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'video': 'VideoTemplateInfo',
        'audio': 'AudioTemplateInfo',
        'format': 'str'
    }

    attribute_map = {
        'video': 'video',
        'audio': 'audio',
        'format': 'format'
    }

    def __init__(self, video=None, audio=None, format=None):
        """QualityInfo - a model defined in huaweicloud sdk"""
        
        

        self._video = None
        self._audio = None
        self._format = None
        self.discriminator = None

        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio
        self.format = format

    @property
    def video(self):
        """Gets the video of this QualityInfo.


        :return: The video of this QualityInfo.
        :rtype: VideoTemplateInfo
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this QualityInfo.


        :param video: The video of this QualityInfo.
        :type: VideoTemplateInfo
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this QualityInfo.


        :return: The audio of this QualityInfo.
        :rtype: AudioTemplateInfo
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this QualityInfo.


        :param audio: The audio of this QualityInfo.
        :type: AudioTemplateInfo
        """
        self._audio = audio

    @property
    def format(self):
        """Gets the format of this QualityInfo.

        格式<br/> 

        :return: The format of this QualityInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this QualityInfo.

        格式<br/> 

        :param format: The format of this QualityInfo.
        :type: str
        """
        self._format = format

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
        if not isinstance(other, QualityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other