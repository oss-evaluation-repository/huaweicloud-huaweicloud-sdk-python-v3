# coding: utf-8

import re
import six





class AgencyV2:


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
        'name': 'str',
        'duration': 'str',
        'trust_domain_name': 'str',
        'trust_domain_id': 'str',
        'create_time': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'duration': 'duration',
        'trust_domain_name': 'trust_domain_name',
        'trust_domain_id': 'trust_domain_id',
        'create_time': 'create_time',
        'expire_time': 'expire_time'
    }

    def __init__(self, id=None, name=None, duration=None, trust_domain_name=None, trust_domain_id=None, create_time=None, expire_time=None):
        """AgencyV2 - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._duration = None
        self._trust_domain_name = None
        self._trust_domain_id = None
        self._create_time = None
        self._expire_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if duration is not None:
            self.duration = duration
        if trust_domain_name is not None:
            self.trust_domain_name = trust_domain_name
        if trust_domain_id is not None:
            self.trust_domain_id = trust_domain_id
        if create_time is not None:
            self.create_time = create_time
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def id(self):
        """Gets the id of this AgencyV2.

        委托id

        :return: The id of this AgencyV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgencyV2.

        委托id

        :param id: The id of this AgencyV2.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AgencyV2.

        委托名称

        :return: The name of this AgencyV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgencyV2.

        委托名称

        :param name: The name of this AgencyV2.
        :type: str
        """
        self._name = name

    @property
    def duration(self):
        """Gets the duration of this AgencyV2.

        委托的期限

        :return: The duration of this AgencyV2.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AgencyV2.

        委托的期限

        :param duration: The duration of this AgencyV2.
        :type: str
        """
        self._duration = duration

    @property
    def trust_domain_name(self):
        """Gets the trust_domain_name of this AgencyV2.

        委托的账号名称

        :return: The trust_domain_name of this AgencyV2.
        :rtype: str
        """
        return self._trust_domain_name

    @trust_domain_name.setter
    def trust_domain_name(self, trust_domain_name):
        """Sets the trust_domain_name of this AgencyV2.

        委托的账号名称

        :param trust_domain_name: The trust_domain_name of this AgencyV2.
        :type: str
        """
        self._trust_domain_name = trust_domain_name

    @property
    def trust_domain_id(self):
        """Gets the trust_domain_id of this AgencyV2.

        委托的账号id

        :return: The trust_domain_id of this AgencyV2.
        :rtype: str
        """
        return self._trust_domain_id

    @trust_domain_id.setter
    def trust_domain_id(self, trust_domain_id):
        """Sets the trust_domain_id of this AgencyV2.

        委托的账号id

        :param trust_domain_id: The trust_domain_id of this AgencyV2.
        :type: str
        """
        self._trust_domain_id = trust_domain_id

    @property
    def create_time(self):
        """Gets the create_time of this AgencyV2.

        创建时间

        :return: The create_time of this AgencyV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AgencyV2.

        创建时间

        :param create_time: The create_time of this AgencyV2.
        :type: str
        """
        self._create_time = create_time

    @property
    def expire_time(self):
        """Gets the expire_time of this AgencyV2.

        超期时间

        :return: The expire_time of this AgencyV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this AgencyV2.

        超期时间

        :param expire_time: The expire_time of this AgencyV2.
        :type: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, AgencyV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
