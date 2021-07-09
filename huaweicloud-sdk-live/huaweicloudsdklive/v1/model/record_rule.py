# coding: utf-8

import re
import six





class RecordRule:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'record_type': 'str',
        'plan_record_time': 'PlanRecordTime',
        'default_record_config': 'DefaultRecordConfig',
        'create_time': 'date',
        'update_time': 'date'
    }

    attribute_map = {
        'id': 'id',
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'record_type': 'record_type',
        'plan_record_time': 'plan_record_time',
        'default_record_config': 'default_record_config',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, publish_domain=None, app=None, stream=None, record_type=None, plan_record_time=None, default_record_config=None, create_time=None, update_time=None):
        """RecordRule - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._publish_domain = None
        self._app = None
        self._stream = None
        self._record_type = None
        self._plan_record_time = None
        self._default_record_config = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.publish_domain = publish_domain
        self.app = app
        self.stream = stream
        if record_type is not None:
            self.record_type = record_type
        if plan_record_time is not None:
            self.plan_record_time = plan_record_time
        if default_record_config is not None:
            self.default_record_config = default_record_config
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this RecordRule.

        规则id，由服务端返回。创建或修改的时候不携带

        :return: The id of this RecordRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecordRule.

        规则id，由服务端返回。创建或修改的时候不携带

        :param id: The id of this RecordRule.
        :type: str
        """
        self._id = id

    @property
    def publish_domain(self):
        """Gets the publish_domain of this RecordRule.

        直播推流域名

        :return: The publish_domain of this RecordRule.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this RecordRule.

        直播推流域名

        :param publish_domain: The publish_domain of this RecordRule.
        :type: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this RecordRule.

        应用名，如果任意应用填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :return: The app of this RecordRule.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this RecordRule.

        应用名，如果任意应用填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :param app: The app of this RecordRule.
        :type: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this RecordRule.

        录制的流名，如果任意流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*

        :return: The stream of this RecordRule.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this RecordRule.

        录制的流名，如果任意流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*

        :param stream: The stream of this RecordRule.
        :type: str
        """
        self._stream = stream

    @property
    def record_type(self):
        """Gets the record_type of this RecordRule.

        录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD, ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD: 持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD: 命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。命令控制的接口参考/v1/{project_id}/record/control - PLAN_RECORD: 计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD: 按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。租户提供的接口定义参考：/customer-record-ondemand-url 

        :return: The record_type of this RecordRule.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this RecordRule.

        录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD, ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD: 持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD: 命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。命令控制的接口参考/v1/{project_id}/record/control - PLAN_RECORD: 计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD: 按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。租户提供的接口定义参考：/customer-record-ondemand-url 

        :param record_type: The record_type of this RecordRule.
        :type: str
        """
        self._record_type = record_type

    @property
    def plan_record_time(self):
        """Gets the plan_record_time of this RecordRule.


        :return: The plan_record_time of this RecordRule.
        :rtype: PlanRecordTime
        """
        return self._plan_record_time

    @plan_record_time.setter
    def plan_record_time(self, plan_record_time):
        """Sets the plan_record_time of this RecordRule.


        :param plan_record_time: The plan_record_time of this RecordRule.
        :type: PlanRecordTime
        """
        self._plan_record_time = plan_record_time

    @property
    def default_record_config(self):
        """Gets the default_record_config of this RecordRule.


        :return: The default_record_config of this RecordRule.
        :rtype: DefaultRecordConfig
        """
        return self._default_record_config

    @default_record_config.setter
    def default_record_config(self, default_record_config):
        """Sets the default_record_config of this RecordRule.


        :param default_record_config: The default_record_config of this RecordRule.
        :type: DefaultRecordConfig
        """
        self._default_record_config = default_record_config

    @property
    def create_time(self):
        """Gets the create_time of this RecordRule.

        创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :return: The create_time of this RecordRule.
        :rtype: date
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RecordRule.

        创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :param create_time: The create_time of this RecordRule.
        :type: date
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this RecordRule.

        修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :return: The update_time of this RecordRule.
        :rtype: date
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RecordRule.

        修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :param update_time: The update_time of this RecordRule.
        :type: date
        """
        self._update_time = update_time

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
        if not isinstance(other, RecordRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
