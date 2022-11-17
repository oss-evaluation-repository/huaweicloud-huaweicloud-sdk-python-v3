# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipOperateProtectReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'status': 'int',
        'ip_infos': 'list[EipOperateProtectReqIpInfos]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'status': 'status',
        'ip_infos': 'ip_infos'
    }

    def __init__(self, object_id=None, status=None, ip_infos=None):
        """EipOperateProtectReq

        The model defined in huaweicloud sdk

        :param object_id: 防护对象ID
        :type object_id: str
        :param status: EIP状态
        :type status: int
        :param ip_infos: EIP信息列表
        :type ip_infos: list[:class:`huaweicloudsdkcfw.v1.EipOperateProtectReqIpInfos`]
        """
        
        

        self._object_id = None
        self._status = None
        self._ip_infos = None
        self.discriminator = None

        self.object_id = object_id
        self.status = status
        self.ip_infos = ip_infos

    @property
    def object_id(self):
        """Gets the object_id of this EipOperateProtectReq.

        防护对象ID

        :return: The object_id of this EipOperateProtectReq.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this EipOperateProtectReq.

        防护对象ID

        :param object_id: The object_id of this EipOperateProtectReq.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def status(self):
        """Gets the status of this EipOperateProtectReq.

        EIP状态

        :return: The status of this EipOperateProtectReq.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EipOperateProtectReq.

        EIP状态

        :param status: The status of this EipOperateProtectReq.
        :type status: int
        """
        self._status = status

    @property
    def ip_infos(self):
        """Gets the ip_infos of this EipOperateProtectReq.

        EIP信息列表

        :return: The ip_infos of this EipOperateProtectReq.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.EipOperateProtectReqIpInfos`]
        """
        return self._ip_infos

    @ip_infos.setter
    def ip_infos(self, ip_infos):
        """Sets the ip_infos of this EipOperateProtectReq.

        EIP信息列表

        :param ip_infos: The ip_infos of this EipOperateProtectReq.
        :type ip_infos: list[:class:`huaweicloudsdkcfw.v1.EipOperateProtectReqIpInfos`]
        """
        self._ip_infos = ip_infos

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
        if not isinstance(other, EipOperateProtectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other