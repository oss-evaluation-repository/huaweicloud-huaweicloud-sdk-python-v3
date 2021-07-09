# coding: utf-8

import re
import six





class ShowTestCaseDetailV2Request:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'testcase_number': 'str',
        'testcase_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'testcase_number': 'testcase_number',
        'testcase_id': 'testcase_id'
    }

    def __init__(self, project_id=None, testcase_number=None, testcase_id=None):
        """ShowTestCaseDetailV2Request - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._testcase_number = None
        self._testcase_id = None
        self.discriminator = None

        self.project_id = project_id
        if testcase_number is not None:
            self.testcase_number = testcase_number
        if testcase_id is not None:
            self.testcase_id = testcase_id

    @property
    def project_id(self):
        """Gets the project_id of this ShowTestCaseDetailV2Request.

        项目唯一标识，固定长度32位字符

        :return: The project_id of this ShowTestCaseDetailV2Request.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowTestCaseDetailV2Request.

        项目唯一标识，固定长度32位字符

        :param project_id: The project_id of this ShowTestCaseDetailV2Request.
        :type: str
        """
        self._project_id = project_id

    @property
    def testcase_number(self):
        """Gets the testcase_number of this ShowTestCaseDetailV2Request.

        用例编号，长度为[3-128]位字符

        :return: The testcase_number of this ShowTestCaseDetailV2Request.
        :rtype: str
        """
        return self._testcase_number

    @testcase_number.setter
    def testcase_number(self, testcase_number):
        """Sets the testcase_number of this ShowTestCaseDetailV2Request.

        用例编号，长度为[3-128]位字符

        :param testcase_number: The testcase_number of this ShowTestCaseDetailV2Request.
        :type: str
        """
        self._testcase_number = testcase_number

    @property
    def testcase_id(self):
        """Gets the testcase_id of this ShowTestCaseDetailV2Request.

        测试用例唯一标识，固定长度32位字符

        :return: The testcase_id of this ShowTestCaseDetailV2Request.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        """Sets the testcase_id of this ShowTestCaseDetailV2Request.

        测试用例唯一标识，固定长度32位字符

        :param testcase_id: The testcase_id of this ShowTestCaseDetailV2Request.
        :type: str
        """
        self._testcase_id = testcase_id

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
        if not isinstance(other, ShowTestCaseDetailV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
