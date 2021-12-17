# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalysisModelRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'display_name': 'str',
        'type': 'str',
        'transform': 'TransformModel',
        'aggregate': 'AggregateModel',
        'stream': 'StreamModel'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'type': 'type',
        'transform': 'transform',
        'aggregate': 'aggregate',
        'stream': 'stream'
    }

    def __init__(self, name=None, display_name=None, type=None, transform=None, aggregate=None, stream=None):
        """AnalysisModelRequest - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._display_name = None
        self._type = None
        self._transform = None
        self._aggregate = None
        self._stream = None
        self.discriminator = None

        self.name = name
        if display_name is not None:
            self.display_name = display_name
        self.type = type
        if transform is not None:
            self.transform = transform
        if aggregate is not None:
            self.aggregate = aggregate
        if stream is not None:
            self.stream = stream

    @property
    def name(self):
        """Gets the name of this AnalysisModelRequest.

        分析任务名称，正则：\"^[a-zA-Z][a-zA-Z0-9_]{0,63}$\"

        :return: The name of this AnalysisModelRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalysisModelRequest.

        分析任务名称，正则：\"^[a-zA-Z][a-zA-Z0-9_]{0,63}$\"

        :param name: The name of this AnalysisModelRequest.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this AnalysisModelRequest.

        分析任务显示名称，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\"

        :return: The display_name of this AnalysisModelRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AnalysisModelRequest.

        分析任务显示名称，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\"

        :param display_name: The display_name of this AnalysisModelRequest.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this AnalysisModelRequest.

        分析任务类型，转换计算（transform）、聚合计算（aggregate）、流计算（stream）

        :return: The type of this AnalysisModelRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AnalysisModelRequest.

        分析任务类型，转换计算（transform）、聚合计算（aggregate）、流计算（stream）

        :param type: The type of this AnalysisModelRequest.
        :type: str
        """
        self._type = type

    @property
    def transform(self):
        """Gets the transform of this AnalysisModelRequest.


        :return: The transform of this AnalysisModelRequest.
        :rtype: TransformModel
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this AnalysisModelRequest.


        :param transform: The transform of this AnalysisModelRequest.
        :type: TransformModel
        """
        self._transform = transform

    @property
    def aggregate(self):
        """Gets the aggregate of this AnalysisModelRequest.


        :return: The aggregate of this AnalysisModelRequest.
        :rtype: AggregateModel
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        """Sets the aggregate of this AnalysisModelRequest.


        :param aggregate: The aggregate of this AnalysisModelRequest.
        :type: AggregateModel
        """
        self._aggregate = aggregate

    @property
    def stream(self):
        """Gets the stream of this AnalysisModelRequest.


        :return: The stream of this AnalysisModelRequest.
        :rtype: StreamModel
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this AnalysisModelRequest.


        :param stream: The stream of this AnalysisModelRequest.
        :type: StreamModel
        """
        self._stream = stream

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalysisModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
