# coding: utf-8

import re
import six





class DeleteInstanceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'delete_rds_data': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'delete_rds_data': 'delete_rds_data'
    }

    def __init__(self, instance_id=None, delete_rds_data=None):
        """DeleteInstanceRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._delete_rds_data = None
        self.discriminator = None

        self.instance_id = instance_id
        if delete_rds_data is not None:
            self.delete_rds_data = delete_rds_data

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteInstanceRequest.

        DDM实例ID。

        :return: The instance_id of this DeleteInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteInstanceRequest.

        DDM实例ID。

        :param instance_id: The instance_id of this DeleteInstanceRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def delete_rds_data(self):
        """Gets the delete_rds_data of this DeleteInstanceRequest.

        是否同时删除关联RDS上存储的数据。  - 取值为空或“true”：删除。 - 取值为“false”：不删除。 默认值为空。

        :return: The delete_rds_data of this DeleteInstanceRequest.
        :rtype: str
        """
        return self._delete_rds_data

    @delete_rds_data.setter
    def delete_rds_data(self, delete_rds_data):
        """Sets the delete_rds_data of this DeleteInstanceRequest.

        是否同时删除关联RDS上存储的数据。  - 取值为空或“true”：删除。 - 取值为“false”：不删除。 默认值为空。

        :param delete_rds_data: The delete_rds_data of this DeleteInstanceRequest.
        :type: str
        """
        self._delete_rds_data = delete_rds_data

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
        if not isinstance(other, DeleteInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
