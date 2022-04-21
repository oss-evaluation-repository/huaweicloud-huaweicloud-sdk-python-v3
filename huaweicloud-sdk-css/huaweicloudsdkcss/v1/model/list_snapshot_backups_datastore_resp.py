# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotBackupsDatastoreResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, type=None, version=None):
        """ListSnapshotBackupsDatastoreResp

        The model defined in huaweicloud sdk

        :param type: 支持类型：elasticsearch。
        :type type: str
        :param version: 引擎版本号。当前引擎版本为5.5.1、6.2.3、6.5.4、7.1.1、7.6.2、7.9.3。
        :type version: str
        """
        
        

        self._type = None
        self._version = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def type(self):
        """Gets the type of this ListSnapshotBackupsDatastoreResp.

        支持类型：elasticsearch。

        :return: The type of this ListSnapshotBackupsDatastoreResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListSnapshotBackupsDatastoreResp.

        支持类型：elasticsearch。

        :param type: The type of this ListSnapshotBackupsDatastoreResp.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListSnapshotBackupsDatastoreResp.

        引擎版本号。当前引擎版本为5.5.1、6.2.3、6.5.4、7.1.1、7.6.2、7.9.3。

        :return: The version of this ListSnapshotBackupsDatastoreResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListSnapshotBackupsDatastoreResp.

        引擎版本号。当前引擎版本为5.5.1、6.2.3、6.5.4、7.1.1、7.6.2、7.9.3。

        :param version: The version of this ListSnapshotBackupsDatastoreResp.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ListSnapshotBackupsDatastoreResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
