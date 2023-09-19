# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDigitalHumanBusinessCardRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'x_app_user_id': 'str',
        'body': 'CreateDigitalHumanBusinessCardReq'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_app_user_id': 'X-App-UserId',
        'body': 'body'
    }

    def __init__(self, job_id=None, x_app_user_id=None, body=None):
        """UpdateDigitalHumanBusinessCardRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        :param body: Body of the UpdateDigitalHumanBusinessCardRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalHumanBusinessCardReq`
        """
        
        

        self._job_id = None
        self._x_app_user_id = None
        self._body = None
        self.discriminator = None

        self.job_id = job_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if body is not None:
            self.body = body

    @property
    def job_id(self):
        """Gets the job_id of this UpdateDigitalHumanBusinessCardRequest.

        任务ID。

        :return: The job_id of this UpdateDigitalHumanBusinessCardRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateDigitalHumanBusinessCardRequest.

        任务ID。

        :param job_id: The job_id of this UpdateDigitalHumanBusinessCardRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this UpdateDigitalHumanBusinessCardRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this UpdateDigitalHumanBusinessCardRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this UpdateDigitalHumanBusinessCardRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this UpdateDigitalHumanBusinessCardRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def body(self):
        """Gets the body of this UpdateDigitalHumanBusinessCardRequest.

        :return: The body of this UpdateDigitalHumanBusinessCardRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalHumanBusinessCardReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDigitalHumanBusinessCardRequest.

        :param body: The body of this UpdateDigitalHumanBusinessCardRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalHumanBusinessCardReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateDigitalHumanBusinessCardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
