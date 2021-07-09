# coding: utf-8

import re
import six





class ReviewInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'suggestion': 'str',
        'text': 'TextReviewRet',
        'cover': 'list[PictureReviewRet]',
        'video': 'list[PictureReviewRet]',
        'exec_desc': 'str',
        'review_status': 'str'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'text': 'text',
        'cover': 'cover',
        'video': 'video',
        'exec_desc': 'exec_desc',
        'review_status': 'review_status'
    }

    def __init__(self, suggestion=None, text=None, cover=None, video=None, exec_desc=None, review_status=None):
        """ReviewInfo - a model defined in huaweicloud sdk"""
        
        

        self._suggestion = None
        self._text = None
        self._cover = None
        self._video = None
        self._exec_desc = None
        self._review_status = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if text is not None:
            self.text = text
        if cover is not None:
            self.cover = cover
        if video is not None:
            self.video = video
        if exec_desc is not None:
            self.exec_desc = exec_desc
        self.review_status = review_status

    @property
    def suggestion(self):
        """Gets the suggestion of this ReviewInfo.

        检测结果是否通过。  取值如下： - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过。 - review：需要人工复检。  > 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。

        :return: The suggestion of this ReviewInfo.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ReviewInfo.

        检测结果是否通过。  取值如下： - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过。 - review：需要人工复检。  > 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。

        :param suggestion: The suggestion of this ReviewInfo.
        :type: str
        """
        self._suggestion = suggestion

    @property
    def text(self):
        """Gets the text of this ReviewInfo.


        :return: The text of this ReviewInfo.
        :rtype: TextReviewRet
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ReviewInfo.


        :param text: The text of this ReviewInfo.
        :type: TextReviewRet
        """
        self._text = text

    @property
    def cover(self):
        """Gets the cover of this ReviewInfo.

        封面检测结果。

        :return: The cover of this ReviewInfo.
        :rtype: list[PictureReviewRet]
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """Sets the cover of this ReviewInfo.

        封面检测结果。

        :param cover: The cover of this ReviewInfo.
        :type: list[PictureReviewRet]
        """
        self._cover = cover

    @property
    def video(self):
        """Gets the video of this ReviewInfo.

        视频检测结果。

        :return: The video of this ReviewInfo.
        :rtype: list[PictureReviewRet]
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this ReviewInfo.

        视频检测结果。

        :param video: The video of this ReviewInfo.
        :type: list[PictureReviewRet]
        """
        self._video = video

    @property
    def exec_desc(self):
        """Gets the exec_desc of this ReviewInfo.

        执行情况描述。

        :return: The exec_desc of this ReviewInfo.
        :rtype: str
        """
        return self._exec_desc

    @exec_desc.setter
    def exec_desc(self, exec_desc):
        """Sets the exec_desc of this ReviewInfo.

        执行情况描述。

        :param exec_desc: The exec_desc of this ReviewInfo.
        :type: str
        """
        self._exec_desc = exec_desc

    @property
    def review_status(self):
        """Gets the review_status of this ReviewInfo.

        审核状态。  取值如下： - UN_REVIEW：未审核 - REVIEWING：审核中 - REVIEW_SUSPICIOUS：审核可疑，需要人工审核 - REVIEW_PASSED：审核通过 - REVIEW_FAILED：审核失败。 - REVIEW_BLOCKED：已屏蔽。

        :return: The review_status of this ReviewInfo.
        :rtype: str
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        """Sets the review_status of this ReviewInfo.

        审核状态。  取值如下： - UN_REVIEW：未审核 - REVIEWING：审核中 - REVIEW_SUSPICIOUS：审核可疑，需要人工审核 - REVIEW_PASSED：审核通过 - REVIEW_FAILED：审核失败。 - REVIEW_BLOCKED：已屏蔽。

        :param review_status: The review_status of this ReviewInfo.
        :type: str
        """
        self._review_status = review_status

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
        if not isinstance(other, ReviewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
