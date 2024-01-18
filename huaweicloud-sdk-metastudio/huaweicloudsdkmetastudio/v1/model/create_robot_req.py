# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRobotReq:

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
        'app_type': 'int',
        'concurrency': 'int',
        'huawei_ei_cbs': 'HuaweiEiCbs',
        'iflytek_aiui_config': 'IflytekAiuiConfig',
        'iflytek_spark': 'IflytekSpark'
    }

    attribute_map = {
        'name': 'name',
        'app_type': 'app_type',
        'concurrency': 'concurrency',
        'huawei_ei_cbs': 'huawei_ei_cbs',
        'iflytek_aiui_config': 'iflytek_aiui_config',
        'iflytek_spark': 'iflytek_spark'
    }

    def __init__(self, name=None, app_type=None, concurrency=None, huawei_ei_cbs=None, iflytek_aiui_config=None, iflytek_spark=None):
        """CreateRobotReq

        The model defined in huaweicloud sdk

        :param name: 应用名称。
        :type name: str
        :param app_type: 对接第三方应用厂商类型。 &gt; 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动
        :type app_type: int
        :param concurrency: 对话的并发数
        :type concurrency: int
        :param huawei_ei_cbs: 
        :type huawei_ei_cbs: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        :param iflytek_aiui_config: 
        :type iflytek_aiui_config: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        :param iflytek_spark: 
        :type iflytek_spark: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        """
        
        

        self._name = None
        self._app_type = None
        self._concurrency = None
        self._huawei_ei_cbs = None
        self._iflytek_aiui_config = None
        self._iflytek_spark = None
        self.discriminator = None

        self.name = name
        self.app_type = app_type
        self.concurrency = concurrency
        if huawei_ei_cbs is not None:
            self.huawei_ei_cbs = huawei_ei_cbs
        if iflytek_aiui_config is not None:
            self.iflytek_aiui_config = iflytek_aiui_config
        if iflytek_spark is not None:
            self.iflytek_spark = iflytek_spark

    @property
    def name(self):
        """Gets the name of this CreateRobotReq.

        应用名称。

        :return: The name of this CreateRobotReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRobotReq.

        应用名称。

        :param name: The name of this CreateRobotReq.
        :type name: str
        """
        self._name = name

    @property
    def app_type(self):
        """Gets the app_type of this CreateRobotReq.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动

        :return: The app_type of this CreateRobotReq.
        :rtype: int
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this CreateRobotReq.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动

        :param app_type: The app_type of this CreateRobotReq.
        :type app_type: int
        """
        self._app_type = app_type

    @property
    def concurrency(self):
        """Gets the concurrency of this CreateRobotReq.

        对话的并发数

        :return: The concurrency of this CreateRobotReq.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this CreateRobotReq.

        对话的并发数

        :param concurrency: The concurrency of this CreateRobotReq.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def huawei_ei_cbs(self):
        """Gets the huawei_ei_cbs of this CreateRobotReq.

        :return: The huawei_ei_cbs of this CreateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        """
        return self._huawei_ei_cbs

    @huawei_ei_cbs.setter
    def huawei_ei_cbs(self, huawei_ei_cbs):
        """Sets the huawei_ei_cbs of this CreateRobotReq.

        :param huawei_ei_cbs: The huawei_ei_cbs of this CreateRobotReq.
        :type huawei_ei_cbs: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        """
        self._huawei_ei_cbs = huawei_ei_cbs

    @property
    def iflytek_aiui_config(self):
        """Gets the iflytek_aiui_config of this CreateRobotReq.

        :return: The iflytek_aiui_config of this CreateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        """
        return self._iflytek_aiui_config

    @iflytek_aiui_config.setter
    def iflytek_aiui_config(self, iflytek_aiui_config):
        """Sets the iflytek_aiui_config of this CreateRobotReq.

        :param iflytek_aiui_config: The iflytek_aiui_config of this CreateRobotReq.
        :type iflytek_aiui_config: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        """
        self._iflytek_aiui_config = iflytek_aiui_config

    @property
    def iflytek_spark(self):
        """Gets the iflytek_spark of this CreateRobotReq.

        :return: The iflytek_spark of this CreateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        """
        return self._iflytek_spark

    @iflytek_spark.setter
    def iflytek_spark(self, iflytek_spark):
        """Sets the iflytek_spark of this CreateRobotReq.

        :param iflytek_spark: The iflytek_spark of this CreateRobotReq.
        :type iflytek_spark: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        """
        self._iflytek_spark = iflytek_spark

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
        if not isinstance(other, CreateRobotReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
