# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessConfigResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_config_id': 'str',
        'access_config_name': 'str',
        'access_config_type': 'str',
        'create_time': 'int',
        'access_config_detail': 'AccessConfigDeatil',
        'log_info': 'AccessConfigQueryLogInfo',
        'host_group_info': 'AccessConfigHostGroupIdList'
    }

    attribute_map = {
        'access_config_id': 'access_config_id',
        'access_config_name': 'access_config_name',
        'access_config_type': 'access_config_type',
        'create_time': 'create_time',
        'access_config_detail': 'access_config_detail',
        'log_info': 'log_info',
        'host_group_info': 'host_group_info'
    }

    def __init__(self, access_config_id=None, access_config_name=None, access_config_type=None, create_time=None, access_config_detail=None, log_info=None, host_group_info=None):
        """CreateAccessConfigResponse - a model defined in huaweicloud sdk"""
        
        super(CreateAccessConfigResponse, self).__init__()

        self._access_config_id = None
        self._access_config_name = None
        self._access_config_type = None
        self._create_time = None
        self._access_config_detail = None
        self._log_info = None
        self._host_group_info = None
        self.discriminator = None

        if access_config_id is not None:
            self.access_config_id = access_config_id
        if access_config_name is not None:
            self.access_config_name = access_config_name
        if access_config_type is not None:
            self.access_config_type = access_config_type
        if create_time is not None:
            self.create_time = create_time
        if access_config_detail is not None:
            self.access_config_detail = access_config_detail
        if log_info is not None:
            self.log_info = log_info
        if host_group_info is not None:
            self.host_group_info = host_group_info

    @property
    def access_config_id(self):
        """Gets the access_config_id of this CreateAccessConfigResponse.

        日志接入ID

        :return: The access_config_id of this CreateAccessConfigResponse.
        :rtype: str
        """
        return self._access_config_id

    @access_config_id.setter
    def access_config_id(self, access_config_id):
        """Sets the access_config_id of this CreateAccessConfigResponse.

        日志接入ID

        :param access_config_id: The access_config_id of this CreateAccessConfigResponse.
        :type: str
        """
        self._access_config_id = access_config_id

    @property
    def access_config_name(self):
        """Gets the access_config_name of this CreateAccessConfigResponse.

        日志接入名称

        :return: The access_config_name of this CreateAccessConfigResponse.
        :rtype: str
        """
        return self._access_config_name

    @access_config_name.setter
    def access_config_name(self, access_config_name):
        """Sets the access_config_name of this CreateAccessConfigResponse.

        日志接入名称

        :param access_config_name: The access_config_name of this CreateAccessConfigResponse.
        :type: str
        """
        self._access_config_name = access_config_name

    @property
    def access_config_type(self):
        """Gets the access_config_type of this CreateAccessConfigResponse.

        日志接入类型。AGENT：主机接入

        :return: The access_config_type of this CreateAccessConfigResponse.
        :rtype: str
        """
        return self._access_config_type

    @access_config_type.setter
    def access_config_type(self, access_config_type):
        """Sets the access_config_type of this CreateAccessConfigResponse.

        日志接入类型。AGENT：主机接入

        :param access_config_type: The access_config_type of this CreateAccessConfigResponse.
        :type: str
        """
        self._access_config_type = access_config_type

    @property
    def create_time(self):
        """Gets the create_time of this CreateAccessConfigResponse.

        创建时间

        :return: The create_time of this CreateAccessConfigResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateAccessConfigResponse.

        创建时间

        :param create_time: The create_time of this CreateAccessConfigResponse.
        :type: int
        """
        self._create_time = create_time

    @property
    def access_config_detail(self):
        """Gets the access_config_detail of this CreateAccessConfigResponse.


        :return: The access_config_detail of this CreateAccessConfigResponse.
        :rtype: AccessConfigDeatil
        """
        return self._access_config_detail

    @access_config_detail.setter
    def access_config_detail(self, access_config_detail):
        """Sets the access_config_detail of this CreateAccessConfigResponse.


        :param access_config_detail: The access_config_detail of this CreateAccessConfigResponse.
        :type: AccessConfigDeatil
        """
        self._access_config_detail = access_config_detail

    @property
    def log_info(self):
        """Gets the log_info of this CreateAccessConfigResponse.


        :return: The log_info of this CreateAccessConfigResponse.
        :rtype: AccessConfigQueryLogInfo
        """
        return self._log_info

    @log_info.setter
    def log_info(self, log_info):
        """Sets the log_info of this CreateAccessConfigResponse.


        :param log_info: The log_info of this CreateAccessConfigResponse.
        :type: AccessConfigQueryLogInfo
        """
        self._log_info = log_info

    @property
    def host_group_info(self):
        """Gets the host_group_info of this CreateAccessConfigResponse.


        :return: The host_group_info of this CreateAccessConfigResponse.
        :rtype: AccessConfigHostGroupIdList
        """
        return self._host_group_info

    @host_group_info.setter
    def host_group_info(self, host_group_info):
        """Sets the host_group_info of this CreateAccessConfigResponse.


        :param host_group_info: The host_group_info of this CreateAccessConfigResponse.
        :type: AccessConfigHostGroupIdList
        """
        self._host_group_info = host_group_info

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
        if not isinstance(other, CreateAccessConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
