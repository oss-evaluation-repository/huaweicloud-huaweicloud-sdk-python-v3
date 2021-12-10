# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeywordsAlarmRuleRespList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'keywords_alarm_rule_id': 'str',
        'keywords_alarm_rule_name': 'str',
        'keywords_alarm_rule_description': 'str',
        'condition_expression': 'str',
        'keywords_requests': 'list[KeywordsRequest]',
        'frequency': 'Frequency',
        'keywords_alarm_level': 'str',
        'keywords_alarm_send': 'bool',
        'domain_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'topics': 'list[Topics]',
        'language': 'str'
    }

    attribute_map = {
        'project_id': 'projectId',
        'keywords_alarm_rule_id': 'keywords_alarm_rule_id',
        'keywords_alarm_rule_name': 'keywords_alarm_rule_name',
        'keywords_alarm_rule_description': 'keywords_alarm_rule_description',
        'condition_expression': 'condition_expression',
        'keywords_requests': 'keywords_requests',
        'frequency': 'frequency',
        'keywords_alarm_level': 'keywords_alarm_level',
        'keywords_alarm_send': 'keywords_alarm_send',
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'topics': 'topics',
        'language': 'language'
    }

    def __init__(self, project_id=None, keywords_alarm_rule_id=None, keywords_alarm_rule_name=None, keywords_alarm_rule_description=None, condition_expression=None, keywords_requests=None, frequency=None, keywords_alarm_level=None, keywords_alarm_send=None, domain_id=None, create_time=None, update_time=None, topics=None, language=None):
        """KeywordsAlarmRuleRespList - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._keywords_alarm_rule_id = None
        self._keywords_alarm_rule_name = None
        self._keywords_alarm_rule_description = None
        self._condition_expression = None
        self._keywords_requests = None
        self._frequency = None
        self._keywords_alarm_level = None
        self._keywords_alarm_send = None
        self._domain_id = None
        self._create_time = None
        self._update_time = None
        self._topics = None
        self._language = None
        self.discriminator = None

        self.project_id = project_id
        self.keywords_alarm_rule_id = keywords_alarm_rule_id
        self.keywords_alarm_rule_name = keywords_alarm_rule_name
        self.keywords_alarm_rule_description = keywords_alarm_rule_description
        self.condition_expression = condition_expression
        self.keywords_requests = keywords_requests
        self.frequency = frequency
        self.keywords_alarm_level = keywords_alarm_level
        self.keywords_alarm_send = keywords_alarm_send
        self.domain_id = domain_id
        self.create_time = create_time
        self.update_time = update_time
        self.topics = topics
        self.language = language

    @property
    def project_id(self):
        """Gets the project_id of this KeywordsAlarmRuleRespList.

        项目id

        :return: The project_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this KeywordsAlarmRuleRespList.

        项目id

        :param project_id: The project_id of this KeywordsAlarmRuleRespList.
        :type: str
        """
        self._project_id = project_id

    @property
    def keywords_alarm_rule_id(self):
        """Gets the keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.

        关键词告警id

        :return: The keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_id

    @keywords_alarm_rule_id.setter
    def keywords_alarm_rule_id(self, keywords_alarm_rule_id):
        """Sets the keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.

        关键词告警id

        :param keywords_alarm_rule_id: The keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.
        :type: str
        """
        self._keywords_alarm_rule_id = keywords_alarm_rule_id

    @property
    def keywords_alarm_rule_name(self):
        """Gets the keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.

        关键词告警名称

        :return: The keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_name

    @keywords_alarm_rule_name.setter
    def keywords_alarm_rule_name(self, keywords_alarm_rule_name):
        """Sets the keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.

        关键词告警名称

        :param keywords_alarm_rule_name: The keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.
        :type: str
        """
        self._keywords_alarm_rule_name = keywords_alarm_rule_name

    @property
    def keywords_alarm_rule_description(self):
        """Gets the keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.

        关键词告警信息描述

        :return: The keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_description

    @keywords_alarm_rule_description.setter
    def keywords_alarm_rule_description(self, keywords_alarm_rule_description):
        """Sets the keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.

        关键词告警信息描述

        :param keywords_alarm_rule_description: The keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.
        :type: str
        """
        self._keywords_alarm_rule_description = keywords_alarm_rule_description

    @property
    def condition_expression(self):
        """Gets the condition_expression of this KeywordsAlarmRuleRespList.

        条件

        :return: The condition_expression of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        """Sets the condition_expression of this KeywordsAlarmRuleRespList.

        条件

        :param condition_expression: The condition_expression of this KeywordsAlarmRuleRespList.
        :type: str
        """
        self._condition_expression = condition_expression

    @property
    def keywords_requests(self):
        """Gets the keywords_requests of this KeywordsAlarmRuleRespList.

        关键词详细信息

        :return: The keywords_requests of this KeywordsAlarmRuleRespList.
        :rtype: list[KeywordsRequest]
        """
        return self._keywords_requests

    @keywords_requests.setter
    def keywords_requests(self, keywords_requests):
        """Sets the keywords_requests of this KeywordsAlarmRuleRespList.

        关键词详细信息

        :param keywords_requests: The keywords_requests of this KeywordsAlarmRuleRespList.
        :type: list[KeywordsRequest]
        """
        self._keywords_requests = keywords_requests

    @property
    def frequency(self):
        """Gets the frequency of this KeywordsAlarmRuleRespList.

        告警统计周期

        :return: The frequency of this KeywordsAlarmRuleRespList.
        :rtype: Frequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this KeywordsAlarmRuleRespList.

        告警统计周期

        :param frequency: The frequency of this KeywordsAlarmRuleRespList.
        :type: Frequency
        """
        self._frequency = frequency

    @property
    def keywords_alarm_level(self):
        """Gets the keywords_alarm_level of this KeywordsAlarmRuleRespList.

        告警级别

        :return: The keywords_alarm_level of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_level

    @keywords_alarm_level.setter
    def keywords_alarm_level(self, keywords_alarm_level):
        """Sets the keywords_alarm_level of this KeywordsAlarmRuleRespList.

        告警级别

        :param keywords_alarm_level: The keywords_alarm_level of this KeywordsAlarmRuleRespList.
        :type: str
        """
        self._keywords_alarm_level = keywords_alarm_level

    @property
    def keywords_alarm_send(self):
        """Gets the keywords_alarm_send of this KeywordsAlarmRuleRespList.

        是否发送

        :return: The keywords_alarm_send of this KeywordsAlarmRuleRespList.
        :rtype: bool
        """
        return self._keywords_alarm_send

    @keywords_alarm_send.setter
    def keywords_alarm_send(self, keywords_alarm_send):
        """Sets the keywords_alarm_send of this KeywordsAlarmRuleRespList.

        是否发送

        :param keywords_alarm_send: The keywords_alarm_send of this KeywordsAlarmRuleRespList.
        :type: bool
        """
        self._keywords_alarm_send = keywords_alarm_send

    @property
    def domain_id(self):
        """Gets the domain_id of this KeywordsAlarmRuleRespList.

        domainId

        :return: The domain_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeywordsAlarmRuleRespList.

        domainId

        :param domain_id: The domain_id of this KeywordsAlarmRuleRespList.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        """Gets the create_time of this KeywordsAlarmRuleRespList.

        创建时间(毫秒时间戳)

        :return: The create_time of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this KeywordsAlarmRuleRespList.

        创建时间(毫秒时间戳)

        :param create_time: The create_time of this KeywordsAlarmRuleRespList.
        :type: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this KeywordsAlarmRuleRespList.

        更新时间(毫秒时间戳)

        :return: The update_time of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this KeywordsAlarmRuleRespList.

        更新时间(毫秒时间戳)

        :param update_time: The update_time of this KeywordsAlarmRuleRespList.
        :type: int
        """
        self._update_time = update_time

    @property
    def topics(self):
        """Gets the topics of this KeywordsAlarmRuleRespList.

        主题

        :return: The topics of this KeywordsAlarmRuleRespList.
        :rtype: list[Topics]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this KeywordsAlarmRuleRespList.

        主题

        :param topics: The topics of this KeywordsAlarmRuleRespList.
        :type: list[Topics]
        """
        self._topics = topics

    @property
    def language(self):
        """Gets the language of this KeywordsAlarmRuleRespList.

        邮件附加信息是否英文

        :return: The language of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this KeywordsAlarmRuleRespList.

        邮件附加信息是否英文

        :param language: The language of this KeywordsAlarmRuleRespList.
        :type: str
        """
        self._language = language

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
        if not isinstance(other, KeywordsAlarmRuleRespList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
