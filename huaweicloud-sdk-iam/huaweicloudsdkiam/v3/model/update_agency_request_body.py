# coding: utf-8

import re
import six





class UpdateAgencyRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'agency': 'UpdateAgencyOption'
    }

    attribute_map = {
        'agency': 'agency'
    }

    def __init__(self, agency=None):
        """UpdateAgencyRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._agency = None
        self.discriminator = None

        self.agency = agency

    @property
    def agency(self):
        """Gets the agency of this UpdateAgencyRequestBody.


        :return: The agency of this UpdateAgencyRequestBody.
        :rtype: UpdateAgencyOption
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this UpdateAgencyRequestBody.


        :param agency: The agency of this UpdateAgencyRequestBody.
        :type: UpdateAgencyOption
        """
        self._agency = agency

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
        if not isinstance(other, UpdateAgencyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
