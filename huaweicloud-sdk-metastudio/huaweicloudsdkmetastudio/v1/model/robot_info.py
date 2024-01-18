# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RobotInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'robot_id': 'str',
        'name': 'str',
        'app_id': 'str',
        'app_type': 'int',
        'concurrency': 'int',
        'create_time': 'str',
        'update_time': 'str',
        'region': 'int',
        'cbs_project_id': 'str'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'name': 'name',
        'app_id': 'app_id',
        'app_type': 'app_type',
        'concurrency': 'concurrency',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'region': 'region',
        'cbs_project_id': 'cbs_project_id'
    }

    def __init__(self, robot_id=None, name=None, app_id=None, app_type=None, concurrency=None, create_time=None, update_time=None, region=None, cbs_project_id=None):
        """RobotInfo

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param name: 应用名称。
        :type name: str
        :param app_id: 第三方应用ID。
        :type app_id: str
        :param app_type: 对接第三方应用厂商类型。 &gt; 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动
        :type app_type: int
        :param concurrency: 对话的并发数
        :type concurrency: int
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param region: CBS所在区域
        :type region: int
        :param cbs_project_id: CBS所在区域的projectId
        :type cbs_project_id: str
        """
        
        

        self._robot_id = None
        self._name = None
        self._app_id = None
        self._app_type = None
        self._concurrency = None
        self._create_time = None
        self._update_time = None
        self._region = None
        self._cbs_project_id = None
        self.discriminator = None

        if robot_id is not None:
            self.robot_id = robot_id
        if name is not None:
            self.name = name
        if app_id is not None:
            self.app_id = app_id
        if app_type is not None:
            self.app_type = app_type
        if concurrency is not None:
            self.concurrency = concurrency
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if region is not None:
            self.region = region
        if cbs_project_id is not None:
            self.cbs_project_id = cbs_project_id

    @property
    def robot_id(self):
        """Gets the robot_id of this RobotInfo.

        应用ID。

        :return: The robot_id of this RobotInfo.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this RobotInfo.

        应用ID。

        :param robot_id: The robot_id of this RobotInfo.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def name(self):
        """Gets the name of this RobotInfo.

        应用名称。

        :return: The name of this RobotInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RobotInfo.

        应用名称。

        :param name: The name of this RobotInfo.
        :type name: str
        """
        self._name = name

    @property
    def app_id(self):
        """Gets the app_id of this RobotInfo.

        第三方应用ID。

        :return: The app_id of this RobotInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this RobotInfo.

        第三方应用ID。

        :param app_id: The app_id of this RobotInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_type(self):
        """Gets the app_type of this RobotInfo.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动

        :return: The app_type of this RobotInfo.
        :rtype: int
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this RobotInfo.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动

        :param app_type: The app_type of this RobotInfo.
        :type app_type: int
        """
        self._app_type = app_type

    @property
    def concurrency(self):
        """Gets the concurrency of this RobotInfo.

        对话的并发数

        :return: The concurrency of this RobotInfo.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this RobotInfo.

        对话的并发数

        :param concurrency: The concurrency of this RobotInfo.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def create_time(self):
        """Gets the create_time of this RobotInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this RobotInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RobotInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this RobotInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this RobotInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this RobotInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RobotInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this RobotInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def region(self):
        """Gets the region of this RobotInfo.

        CBS所在区域

        :return: The region of this RobotInfo.
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RobotInfo.

        CBS所在区域

        :param region: The region of this RobotInfo.
        :type region: int
        """
        self._region = region

    @property
    def cbs_project_id(self):
        """Gets the cbs_project_id of this RobotInfo.

        CBS所在区域的projectId

        :return: The cbs_project_id of this RobotInfo.
        :rtype: str
        """
        return self._cbs_project_id

    @cbs_project_id.setter
    def cbs_project_id(self, cbs_project_id):
        """Sets the cbs_project_id of this RobotInfo.

        CBS所在区域的projectId

        :param cbs_project_id: The cbs_project_id of this RobotInfo.
        :type cbs_project_id: str
        """
        self._cbs_project_id = cbs_project_id

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
        if not isinstance(other, RobotInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
