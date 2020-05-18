# coding: utf-8

import pprint
import re

import six


class ListSnapshotsDetailsRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'status': 'str',
        'id': 'str',
        'dedicated_storage_name': 'str',
        'dedicated_storage_id': 'str',
        'service_type': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'status': 'status',
        'id': 'id',
        'dedicated_storage_name': 'dedicated_storage_name',
        'dedicated_storage_id': 'dedicated_storage_id',
        'service_type': 'service_type',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, offset=None, limit=None, name=None, status=None, id=None, dedicated_storage_name=None, dedicated_storage_id=None, service_type=None, enterprise_project_id=None):  # noqa: E501
        """ListSnapshotsDetailsRequest - a model defined in huaweicloud sdk"""

        self._offset = None
        self._limit = None
        self._name = None
        self._status = None
        self._id = None
        self._dedicated_storage_name = None
        self._dedicated_storage_id = None
        self._service_type = None
        self._enterprise_project_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if dedicated_storage_name is not None:
            self.dedicated_storage_name = dedicated_storage_name
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if service_type is not None:
            self.service_type = service_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListSnapshotsDetailsRequest.


        :return: The offset of this ListSnapshotsDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSnapshotsDetailsRequest.


        :param offset: The offset of this ListSnapshotsDetailsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSnapshotsDetailsRequest.


        :return: The limit of this ListSnapshotsDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSnapshotsDetailsRequest.


        :param limit: The limit of this ListSnapshotsDetailsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListSnapshotsDetailsRequest.


        :return: The name of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListSnapshotsDetailsRequest.


        :param name: The name of this ListSnapshotsDetailsRequest.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListSnapshotsDetailsRequest.


        :return: The status of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSnapshotsDetailsRequest.


        :param status: The status of this ListSnapshotsDetailsRequest.
        :type: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this ListSnapshotsDetailsRequest.


        :return: The id of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSnapshotsDetailsRequest.


        :param id: The id of this ListSnapshotsDetailsRequest.
        :type: str
        """
        self._id = id

    @property
    def dedicated_storage_name(self):
        """Gets the dedicated_storage_name of this ListSnapshotsDetailsRequest.


        :return: The dedicated_storage_name of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._dedicated_storage_name

    @dedicated_storage_name.setter
    def dedicated_storage_name(self, dedicated_storage_name):
        """Sets the dedicated_storage_name of this ListSnapshotsDetailsRequest.


        :param dedicated_storage_name: The dedicated_storage_name of this ListSnapshotsDetailsRequest.
        :type: str
        """
        self._dedicated_storage_name = dedicated_storage_name

    @property
    def dedicated_storage_id(self):
        """Gets the dedicated_storage_id of this ListSnapshotsDetailsRequest.


        :return: The dedicated_storage_id of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        """Sets the dedicated_storage_id of this ListSnapshotsDetailsRequest.


        :param dedicated_storage_id: The dedicated_storage_id of this ListSnapshotsDetailsRequest.
        :type: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def service_type(self):
        """Gets the service_type of this ListSnapshotsDetailsRequest.


        :return: The service_type of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ListSnapshotsDetailsRequest.


        :param service_type: The service_type of this ListSnapshotsDetailsRequest.
        :type: str
        """
        self._service_type = service_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListSnapshotsDetailsRequest.


        :return: The enterprise_project_id of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListSnapshotsDetailsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListSnapshotsDetailsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListSnapshotsDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
