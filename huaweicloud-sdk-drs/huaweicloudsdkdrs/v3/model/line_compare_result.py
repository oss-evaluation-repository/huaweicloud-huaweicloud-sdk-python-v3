# coding: utf-8

import re
import six





class LineCompareResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'compare_task_id': 'str',
        'line_compare_overview': 'list[LineCompareResultOverview]',
        'line_compare_overview_count': 'int',
        'line_compare_details': 'list[LineCompareResultDetails]',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'compare_task_id': 'compare_task_id',
        'line_compare_overview': 'line_compare_overview',
        'line_compare_overview_count': 'line_compare_overview_count',
        'line_compare_details': 'line_compare_details',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, compare_task_id=None, line_compare_overview=None, line_compare_overview_count=None, line_compare_details=None, error_code=None, error_msg=None):
        """LineCompareResult - a model defined in huaweicloud sdk"""
        
        

        self._compare_task_id = None
        self._line_compare_overview = None
        self._line_compare_overview_count = None
        self._line_compare_details = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if compare_task_id is not None:
            self.compare_task_id = compare_task_id
        if line_compare_overview is not None:
            self.line_compare_overview = line_compare_overview
        if line_compare_overview_count is not None:
            self.line_compare_overview_count = line_compare_overview_count
        if line_compare_details is not None:
            self.line_compare_details = line_compare_details
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def compare_task_id(self):
        """Gets the compare_task_id of this LineCompareResult.

        行对比任务的id。

        :return: The compare_task_id of this LineCompareResult.
        :rtype: str
        """
        return self._compare_task_id

    @compare_task_id.setter
    def compare_task_id(self, compare_task_id):
        """Sets the compare_task_id of this LineCompareResult.

        行对比任务的id。

        :param compare_task_id: The compare_task_id of this LineCompareResult.
        :type: str
        """
        self._compare_task_id = compare_task_id

    @property
    def line_compare_overview(self):
        """Gets the line_compare_overview of this LineCompareResult.

        行对比结果概览。

        :return: The line_compare_overview of this LineCompareResult.
        :rtype: list[LineCompareResultOverview]
        """
        return self._line_compare_overview

    @line_compare_overview.setter
    def line_compare_overview(self, line_compare_overview):
        """Sets the line_compare_overview of this LineCompareResult.

        行对比结果概览。

        :param line_compare_overview: The line_compare_overview of this LineCompareResult.
        :type: list[LineCompareResultOverview]
        """
        self._line_compare_overview = line_compare_overview

    @property
    def line_compare_overview_count(self):
        """Gets the line_compare_overview_count of this LineCompareResult.

        行对比结果概览总数。

        :return: The line_compare_overview_count of this LineCompareResult.
        :rtype: int
        """
        return self._line_compare_overview_count

    @line_compare_overview_count.setter
    def line_compare_overview_count(self, line_compare_overview_count):
        """Sets the line_compare_overview_count of this LineCompareResult.

        行对比结果概览总数。

        :param line_compare_overview_count: The line_compare_overview_count of this LineCompareResult.
        :type: int
        """
        self._line_compare_overview_count = line_compare_overview_count

    @property
    def line_compare_details(self):
        """Gets the line_compare_details of this LineCompareResult.

        行对比结果详情。

        :return: The line_compare_details of this LineCompareResult.
        :rtype: list[LineCompareResultDetails]
        """
        return self._line_compare_details

    @line_compare_details.setter
    def line_compare_details(self, line_compare_details):
        """Sets the line_compare_details of this LineCompareResult.

        行对比结果详情。

        :param line_compare_details: The line_compare_details of this LineCompareResult.
        :type: list[LineCompareResultDetails]
        """
        self._line_compare_details = line_compare_details

    @property
    def error_code(self):
        """Gets the error_code of this LineCompareResult.

        错误码。

        :return: The error_code of this LineCompareResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this LineCompareResult.

        错误码。

        :param error_code: The error_code of this LineCompareResult.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this LineCompareResult.

        错误信息。

        :return: The error_msg of this LineCompareResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this LineCompareResult.

        错误信息。

        :param error_msg: The error_msg of this LineCompareResult.
        :type: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, LineCompareResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
