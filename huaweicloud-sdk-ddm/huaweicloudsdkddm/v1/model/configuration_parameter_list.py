# coding: utf-8

import re
import six





class ConfigurationParameterList:


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
        'value': 'str',
        'need_restart': 'str',
        'read_only': 'str',
        'value_range': 'str',
        'data_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'need_restart': 'need_restart',
        'read_only': 'read_only',
        'value_range': 'value_range',
        'data_type': 'data_type',
        'description': 'description'
    }

    def __init__(self, name=None, value=None, need_restart=None, read_only=None, value_range=None, data_type=None, description=None):
        """ConfigurationParameterList - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._value = None
        self._need_restart = None
        self._read_only = None
        self._value_range = None
        self._data_type = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if need_restart is not None:
            self.need_restart = need_restart
        if read_only is not None:
            self.read_only = read_only
        if value_range is not None:
            self.value_range = value_range
        if data_type is not None:
            self.data_type = data_type
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ConfigurationParameterList.

        参数名称。

        :return: The name of this ConfigurationParameterList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationParameterList.

        参数名称。

        :param name: The name of this ConfigurationParameterList.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this ConfigurationParameterList.

        参数值。

        :return: The value of this ConfigurationParameterList.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConfigurationParameterList.

        参数值。

        :param value: The value of this ConfigurationParameterList.
        :type: str
        """
        self._value = value

    @property
    def need_restart(self):
        """Gets the need_restart of this ConfigurationParameterList.

        是否需要重启实例。

        :return: The need_restart of this ConfigurationParameterList.
        :rtype: str
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        """Sets the need_restart of this ConfigurationParameterList.

        是否需要重启实例。

        :param need_restart: The need_restart of this ConfigurationParameterList.
        :type: str
        """
        self._need_restart = need_restart

    @property
    def read_only(self):
        """Gets the read_only of this ConfigurationParameterList.

        参数是否只读。

        :return: The read_only of this ConfigurationParameterList.
        :rtype: str
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this ConfigurationParameterList.

        参数是否只读。

        :param read_only: The read_only of this ConfigurationParameterList.
        :type: str
        """
        self._read_only = read_only

    @property
    def value_range(self):
        """Gets the value_range of this ConfigurationParameterList.

        参数取值范围。

        :return: The value_range of this ConfigurationParameterList.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this ConfigurationParameterList.

        参数取值范围。

        :param value_range: The value_range of this ConfigurationParameterList.
        :type: str
        """
        self._value_range = value_range

    @property
    def data_type(self):
        """Gets the data_type of this ConfigurationParameterList.

        参数类型。

        :return: The data_type of this ConfigurationParameterList.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ConfigurationParameterList.

        参数类型。

        :param data_type: The data_type of this ConfigurationParameterList.
        :type: str
        """
        self._data_type = data_type

    @property
    def description(self):
        """Gets the description of this ConfigurationParameterList.

        参数描述。

        :return: The description of this ConfigurationParameterList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationParameterList.

        参数描述。

        :param description: The description of this ConfigurationParameterList.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, ConfigurationParameterList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
