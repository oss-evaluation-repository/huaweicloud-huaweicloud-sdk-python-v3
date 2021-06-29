# coding: utf-8

import pprint
import re

import six





class Common:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pvc': 'str',
        'pvc_version': 'str',
        'video_codec': 'str',
        'audio_codec': 'str',
        'hls_interval': 'int'
    }

    attribute_map = {
        'pvc': 'pvc',
        'pvc_version': 'pvc_version',
        'video_codec': 'video_codec',
        'audio_codec': 'audio_codec',
        'hls_interval': 'hls_interval'
    }

    def __init__(self, pvc=None, pvc_version=None, video_codec=None, audio_codec=None, hls_interval=None):
        """Common - a model defined in huaweicloud sdk"""
        
        

        self._pvc = None
        self._pvc_version = None
        self._video_codec = None
        self._audio_codec = None
        self._hls_interval = None
        self.discriminator = None

        self.pvc = pvc
        if pvc_version is not None:
            self.pvc_version = pvc_version
        if video_codec is not None:
            self.video_codec = video_codec
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if hls_interval is not None:
            self.hls_interval = hls_interval

    @property
    def pvc(self):
        """Gets the pvc of this Common.

        pvc开关<br/> 

        :return: The pvc of this Common.
        :rtype: str
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """Sets the pvc of this Common.

        pvc开关<br/> 

        :param pvc: The pvc of this Common.
        :type: str
        """
        self._pvc = pvc

    @property
    def pvc_version(self):
        """Gets the pvc_version of this Common.

        pvc版本<br/> 

        :return: The pvc_version of this Common.
        :rtype: str
        """
        return self._pvc_version

    @pvc_version.setter
    def pvc_version(self, pvc_version):
        """Sets the pvc_version of this Common.

        pvc版本<br/> 

        :param pvc_version: The pvc_version of this Common.
        :type: str
        """
        self._pvc_version = pvc_version

    @property
    def video_codec(self):
        """Gets the video_codec of this Common.

        视频编码格式<br/> 

        :return: The video_codec of this Common.
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this Common.

        视频编码格式<br/> 

        :param video_codec: The video_codec of this Common.
        :type: str
        """
        self._video_codec = video_codec

    @property
    def audio_codec(self):
        """Gets the audio_codec of this Common.

        音频编码格式(有效值范围)<br/> AUDIO_CODECTYPE_AAC=1 (default)<br/> AUDIO_CODECTYPE_HEAAC1=2<br/> AUDIO_CODECTYPE_HEAAC2=3<br/> AUDIO_CODECTYPE_MP3=4<br/> 

        :return: The audio_codec of this Common.
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this Common.

        音频编码格式(有效值范围)<br/> AUDIO_CODECTYPE_AAC=1 (default)<br/> AUDIO_CODECTYPE_HEAAC1=2<br/> AUDIO_CODECTYPE_HEAAC2=3<br/> AUDIO_CODECTYPE_MP3=4<br/> 

        :param audio_codec: The audio_codec of this Common.
        :type: str
        """
        self._audio_codec = audio_codec

    @property
    def hls_interval(self):
        """Gets the hls_interval of this Common.

        分片时长(默认为5秒)<br/> 

        :return: The hls_interval of this Common.
        :rtype: int
        """
        return self._hls_interval

    @hls_interval.setter
    def hls_interval(self, hls_interval):
        """Sets the hls_interval of this Common.

        分片时长(默认为5秒)<br/> 

        :param hls_interval: The hls_interval of this Common.
        :type: int
        """
        self._hls_interval = hls_interval

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
        if not isinstance(other, Common):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other