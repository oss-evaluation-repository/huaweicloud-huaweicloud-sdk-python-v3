# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JudgementResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'output': 'str',
        'file_id': 'str',
        'image_id': 'str'
    }

    attribute_map = {
        'output': 'output',
        'file_id': 'file_id',
        'image_id': 'image_id'
    }

    def __init__(self, output=None, file_id=None, image_id=None):
        """JudgementResult - a model defined in huaweicloud sdk"""
        
        

        self._output = None
        self._file_id = None
        self._image_id = None
        self.discriminator = None

        self.output = output
        self.file_id = file_id
        self.image_id = image_id

    @property
    def output(self):
        """Gets the output of this JudgementResult.

        标准类型输出结果

        :return: The output of this JudgementResult.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this JudgementResult.

        标准类型输出结果

        :param output: The output of this JudgementResult.
        :type: str
        """
        self._output = output

    @property
    def file_id(self):
        """Gets the file_id of this JudgementResult.

        文件形式输出的文件id，可根据文件id下载详情

        :return: The file_id of this JudgementResult.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this JudgementResult.

        文件形式输出的文件id，可根据文件id下载详情

        :param file_id: The file_id of this JudgementResult.
        :type: str
        """
        self._file_id = file_id

    @property
    def image_id(self):
        """Gets the image_id of this JudgementResult.

        图片形式输出的图片id，可根据图片id下载详情

        :return: The image_id of this JudgementResult.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this JudgementResult.

        图片形式输出的图片id，可根据图片id下载详情

        :param image_id: The image_id of this JudgementResult.
        :type: str
        """
        self._image_id = image_id

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
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JudgementResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other