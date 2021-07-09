# coding: utf-8

import re
import six





class BackupRestoreServerMapping:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'volume_id': 'volume_id'
    }

    def __init__(self, backup_id=None, volume_id=None):
        """BackupRestoreServerMapping - a model defined in huaweicloud sdk"""
        
        

        self._backup_id = None
        self._volume_id = None
        self.discriminator = None

        self.backup_id = backup_id
        self.volume_id = volume_id

    @property
    def backup_id(self):
        """Gets the backup_id of this BackupRestoreServerMapping.

        卷备份ID，可以通过控制台或者“查询指定备份”接口获取。

        :return: The backup_id of this BackupRestoreServerMapping.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this BackupRestoreServerMapping.

        卷备份ID，可以通过控制台或者“查询指定备份”接口获取。

        :param backup_id: The backup_id of this BackupRestoreServerMapping.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def volume_id(self):
        """Gets the volume_id of this BackupRestoreServerMapping.

        待恢复目标卷ID

        :return: The volume_id of this BackupRestoreServerMapping.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this BackupRestoreServerMapping.

        待恢复目标卷ID

        :param volume_id: The volume_id of this BackupRestoreServerMapping.
        :type: str
        """
        self._volume_id = volume_id

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
        if not isinstance(other, BackupRestoreServerMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
