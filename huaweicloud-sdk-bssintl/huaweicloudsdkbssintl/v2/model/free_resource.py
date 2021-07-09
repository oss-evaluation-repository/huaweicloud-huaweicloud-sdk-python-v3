# coding: utf-8

import re
import six





class FreeResource:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'free_resource_id': 'str',
        'usage_type_name': 'str',
        'amount': 'float',
        'original_amount': 'float',
        'measure_id': 'int'
    }

    attribute_map = {
        'free_resource_id': 'free_resource_id',
        'usage_type_name': 'usage_type_name',
        'amount': 'amount',
        'original_amount': 'original_amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, free_resource_id=None, usage_type_name=None, amount=None, original_amount=None, measure_id=None):
        """FreeResource - a model defined in huaweicloud sdk"""
        
        

        self._free_resource_id = None
        self._usage_type_name = None
        self._amount = None
        self._original_amount = None
        self._measure_id = None
        self.discriminator = None

        if free_resource_id is not None:
            self.free_resource_id = free_resource_id
        if usage_type_name is not None:
            self.usage_type_name = usage_type_name
        if amount is not None:
            self.amount = amount
        if original_amount is not None:
            self.original_amount = original_amount
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def free_resource_id(self):
        """Gets the free_resource_id of this FreeResource.

        |参数名称：免费资源ID| |参数约束及描述：免费资源ID|

        :return: The free_resource_id of this FreeResource.
        :rtype: str
        """
        return self._free_resource_id

    @free_resource_id.setter
    def free_resource_id(self, free_resource_id):
        """Sets the free_resource_id of this FreeResource.

        |参数名称：免费资源ID| |参数约束及描述：免费资源ID|

        :param free_resource_id: The free_resource_id of this FreeResource.
        :type: str
        """
        self._free_resource_id = free_resource_id

    @property
    def usage_type_name(self):
        """Gets the usage_type_name of this FreeResource.

        |参数名称：使用量类型名称| |参数约束及描述：使用量类型名称|

        :return: The usage_type_name of this FreeResource.
        :rtype: str
        """
        return self._usage_type_name

    @usage_type_name.setter
    def usage_type_name(self, usage_type_name):
        """Sets the usage_type_name of this FreeResource.

        |参数名称：使用量类型名称| |参数约束及描述：使用量类型名称|

        :param usage_type_name: The usage_type_name of this FreeResource.
        :type: str
        """
        self._usage_type_name = usage_type_name

    @property
    def amount(self):
        """Gets the amount of this FreeResource.

        |参数名称：免费资源剩余额度| |参数约束及描述：免费资源剩余额度，如果是可重置套餐包，是指当前重置周期内的剩余量|

        :return: The amount of this FreeResource.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FreeResource.

        |参数名称：免费资源剩余额度| |参数约束及描述：免费资源剩余额度，如果是可重置套餐包，是指当前重置周期内的剩余量|

        :param amount: The amount of this FreeResource.
        :type: float
        """
        self._amount = amount

    @property
    def original_amount(self):
        """Gets the original_amount of this FreeResource.

        |参数名称：免费资源原始额度| |参数约束及描述：免费资源原始额度，针对可重置套餐包，是指每个重置周期内的总量|

        :return: The original_amount of this FreeResource.
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this FreeResource.

        |参数名称：免费资源原始额度| |参数约束及描述：免费资源原始额度，针对可重置套餐包，是指每个重置周期内的总量|

        :param original_amount: The original_amount of this FreeResource.
        :type: float
        """
        self._original_amount = original_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this FreeResource.

        |参数名称：度量单位| |参数约束及描述：度量单位，免费资源套餐额度度量单位|

        :return: The measure_id of this FreeResource.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this FreeResource.

        |参数名称：度量单位| |参数约束及描述：度量单位，免费资源套餐额度度量单位|

        :param measure_id: The measure_id of this FreeResource.
        :type: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, FreeResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
