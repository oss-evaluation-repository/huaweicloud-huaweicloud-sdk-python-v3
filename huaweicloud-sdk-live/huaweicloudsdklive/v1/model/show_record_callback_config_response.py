# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowRecordCallbackConfigResponse(SdkResponse):


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
        'notify_callback_url': 'str',
        'notify_event_subscription': 'list[str]',
        'on_demand_callback_url': 'str',
        'create_time': 'date',
        'update_time': 'date'
    }

    attribute_map = {
        'id': 'id',
        'publish_domain': 'publish_domain',
        'app': 'app',
        'notify_callback_url': 'notify_callback_url',
        'notify_event_subscription': 'notify_event_subscription',
        'on_demand_callback_url': 'on_demand_callback_url',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, publish_domain=None, app=None, notify_callback_url=None, notify_event_subscription=None, on_demand_callback_url=None, create_time=None, update_time=None):
        """ShowRecordCallbackConfigResponse - a model defined in huaweicloud sdk"""
        
        super(ShowRecordCallbackConfigResponse, self).__init__()

        self._id = None
        self._publish_domain = None
        self._app = None
        self._notify_callback_url = None
        self._notify_event_subscription = None
        self._on_demand_callback_url = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if publish_domain is not None:
            self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if notify_callback_url is not None:
            self.notify_callback_url = notify_callback_url
        if notify_event_subscription is not None:
            self.notify_event_subscription = notify_event_subscription
        if on_demand_callback_url is not None:
            self.on_demand_callback_url = on_demand_callback_url
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ShowRecordCallbackConfigResponse.

        配置id，由服务端返回。创建或修改的时候不携带

        :return: The id of this ShowRecordCallbackConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowRecordCallbackConfigResponse.

        配置id，由服务端返回。创建或修改的时候不携带

        :param id: The id of this ShowRecordCallbackConfigResponse.
        :type: str
        """
        self._id = id

    @property
    def publish_domain(self):
        """Gets the publish_domain of this ShowRecordCallbackConfigResponse.

        直播推流域名

        :return: The publish_domain of this ShowRecordCallbackConfigResponse.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this ShowRecordCallbackConfigResponse.

        直播推流域名

        :param publish_domain: The publish_domain of this ShowRecordCallbackConfigResponse.
        :type: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this ShowRecordCallbackConfigResponse.

        app名称。如果匹配任意需填写为*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :return: The app of this ShowRecordCallbackConfigResponse.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ShowRecordCallbackConfigResponse.

        app名称。如果匹配任意需填写为*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :param app: The app of this ShowRecordCallbackConfigResponse.
        :type: str
        """
        self._app = app

    @property
    def notify_callback_url(self):
        """Gets the notify_callback_url of this ShowRecordCallbackConfigResponse.

        录制回调通知url地址

        :return: The notify_callback_url of this ShowRecordCallbackConfigResponse.
        :rtype: str
        """
        return self._notify_callback_url

    @notify_callback_url.setter
    def notify_callback_url(self, notify_callback_url):
        """Sets the notify_callback_url of this ShowRecordCallbackConfigResponse.

        录制回调通知url地址

        :param notify_callback_url: The notify_callback_url of this ShowRecordCallbackConfigResponse.
        :type: str
        """
        self._notify_callback_url = notify_callback_url

    @property
    def notify_event_subscription(self):
        """Gets the notify_event_subscription of this ShowRecordCallbackConfigResponse.

        订阅录制通知消息。消息类型。RECORD_NEW_FILE_START开始创建新的录制文件。RECORD_FILE_COMPLETE录制文件生成完成。RECORD_OVER录制结束。RECORD_FAILED表示录制失败。如果不填写,默认订阅RECORD_FILE_COMPLETE

        :return: The notify_event_subscription of this ShowRecordCallbackConfigResponse.
        :rtype: list[str]
        """
        return self._notify_event_subscription

    @notify_event_subscription.setter
    def notify_event_subscription(self, notify_event_subscription):
        """Sets the notify_event_subscription of this ShowRecordCallbackConfigResponse.

        订阅录制通知消息。消息类型。RECORD_NEW_FILE_START开始创建新的录制文件。RECORD_FILE_COMPLETE录制文件生成完成。RECORD_OVER录制结束。RECORD_FAILED表示录制失败。如果不填写,默认订阅RECORD_FILE_COMPLETE

        :param notify_event_subscription: The notify_event_subscription of this ShowRecordCallbackConfigResponse.
        :type: list[str]
        """
        self._notify_event_subscription = notify_event_subscription

    @property
    def on_demand_callback_url(self):
        """Gets the on_demand_callback_url of this ShowRecordCallbackConfigResponse.

        按需录制回调url地址

        :return: The on_demand_callback_url of this ShowRecordCallbackConfigResponse.
        :rtype: str
        """
        return self._on_demand_callback_url

    @on_demand_callback_url.setter
    def on_demand_callback_url(self, on_demand_callback_url):
        """Sets the on_demand_callback_url of this ShowRecordCallbackConfigResponse.

        按需录制回调url地址

        :param on_demand_callback_url: The on_demand_callback_url of this ShowRecordCallbackConfigResponse.
        :type: str
        """
        self._on_demand_callback_url = on_demand_callback_url

    @property
    def create_time(self):
        """Gets the create_time of this ShowRecordCallbackConfigResponse.

        创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :return: The create_time of this ShowRecordCallbackConfigResponse.
        :rtype: date
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowRecordCallbackConfigResponse.

        创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :param create_time: The create_time of this ShowRecordCallbackConfigResponse.
        :type: date
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowRecordCallbackConfigResponse.

        修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :return: The update_time of this ShowRecordCallbackConfigResponse.
        :rtype: date
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowRecordCallbackConfigResponse.

        修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :param update_time: The update_time of this ShowRecordCallbackConfigResponse.
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowRecordCallbackConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other