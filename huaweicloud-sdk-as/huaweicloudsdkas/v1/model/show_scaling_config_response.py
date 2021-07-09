# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowScalingConfigResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_configuration': 'ScalingConfiguration'
    }

    attribute_map = {
        'scaling_configuration': 'scaling_configuration'
    }

    def __init__(self, scaling_configuration=None):
        """ShowScalingConfigResponse - a model defined in huaweicloud sdk"""
        
        super(ShowScalingConfigResponse, self).__init__()

        self._scaling_configuration = None
        self.discriminator = None

        if scaling_configuration is not None:
            self.scaling_configuration = scaling_configuration

    @property
    def scaling_configuration(self):
        """Gets the scaling_configuration of this ShowScalingConfigResponse.


        :return: The scaling_configuration of this ShowScalingConfigResponse.
        :rtype: ScalingConfiguration
        """
        return self._scaling_configuration

    @scaling_configuration.setter
    def scaling_configuration(self, scaling_configuration):
        """Sets the scaling_configuration of this ShowScalingConfigResponse.


        :param scaling_configuration: The scaling_configuration of this ShowScalingConfigResponse.
        :type: ScalingConfiguration
        """
        self._scaling_configuration = scaling_configuration

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
        if not isinstance(other, ShowScalingConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
