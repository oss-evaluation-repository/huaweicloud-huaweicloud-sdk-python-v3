# coding: utf-8

import re
import six





class SetBackupPolicyRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backup_policy': 'BackupPolicy',
        'reserve_backups': 'bool'
    }

    attribute_map = {
        'backup_policy': 'backup_policy',
        'reserve_backups': 'reserve_backups'
    }

    def __init__(self, backup_policy=None, reserve_backups=None):
        """SetBackupPolicyRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._backup_policy = None
        self._reserve_backups = None
        self.discriminator = None

        self.backup_policy = backup_policy
        if reserve_backups is not None:
            self.reserve_backups = reserve_backups

    @property
    def backup_policy(self):
        """Gets the backup_policy of this SetBackupPolicyRequestBody.


        :return: The backup_policy of this SetBackupPolicyRequestBody.
        :rtype: BackupPolicy
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        """Sets the backup_policy of this SetBackupPolicyRequestBody.


        :param backup_policy: The backup_policy of this SetBackupPolicyRequestBody.
        :type: BackupPolicy
        """
        self._backup_policy = backup_policy

    @property
    def reserve_backups(self):
        """Gets the reserve_backups of this SetBackupPolicyRequestBody.

        仅关闭备份策略时有效。  - true（默认），表示保留自动备份和差异备份。 - false，表示关闭备份策略的同时，删除已有的自动备份和差异备份。

        :return: The reserve_backups of this SetBackupPolicyRequestBody.
        :rtype: bool
        """
        return self._reserve_backups

    @reserve_backups.setter
    def reserve_backups(self, reserve_backups):
        """Sets the reserve_backups of this SetBackupPolicyRequestBody.

        仅关闭备份策略时有效。  - true（默认），表示保留自动备份和差异备份。 - false，表示关闭备份策略的同时，删除已有的自动备份和差异备份。

        :param reserve_backups: The reserve_backups of this SetBackupPolicyRequestBody.
        :type: bool
        """
        self._reserve_backups = reserve_backups

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
        if not isinstance(other, SetBackupPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
