# coding: utf-8

import re
import six





class CreateTakeOverTaskReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'object': 'str',
        'suffix': 'list[str]',
        'template_group_name': 'str',
        'workflow_name': 'str',
        'host_type': 'int',
        'output_bucket': 'str',
        'output_path': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'object': 'object',
        'suffix': 'suffix',
        'template_group_name': 'template_group_name',
        'workflow_name': 'workflow_name',
        'host_type': 'host_type',
        'output_bucket': 'output_bucket',
        'output_path': 'output_path'
    }

    def __init__(self, bucket=None, object=None, suffix=None, template_group_name=None, workflow_name=None, host_type=None, output_bucket=None, output_path=None):
        """CreateTakeOverTaskReq - a model defined in huaweicloud sdk"""
        
        

        self._bucket = None
        self._object = None
        self._suffix = None
        self._template_group_name = None
        self._workflow_name = None
        self._host_type = None
        self._output_bucket = None
        self._output_path = None
        self.discriminator = None

        self.bucket = bucket
        self.object = object
        if suffix is not None:
            self.suffix = suffix
        if template_group_name is not None:
            self.template_group_name = template_group_name
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if host_type is not None:
            self.host_type = host_type
        if output_bucket is not None:
            self.output_bucket = output_bucket
        if output_path is not None:
            self.output_path = output_path

    @property
    def bucket(self):
        """Gets the bucket of this CreateTakeOverTaskReq.

        源桶名。

        :return: The bucket of this CreateTakeOverTaskReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this CreateTakeOverTaskReq.

        源桶名。

        :param bucket: The bucket of this CreateTakeOverTaskReq.
        :type: str
        """
        self._bucket = bucket

    @property
    def object(self):
        """Gets the object of this CreateTakeOverTaskReq.

        源目录名或源文件名。

        :return: The object of this CreateTakeOverTaskReq.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this CreateTakeOverTaskReq.

        源目录名或源文件名。

        :param object: The object of this CreateTakeOverTaskReq.
        :type: str
        """
        self._object = object

    @property
    def suffix(self):
        """Gets the suffix of this CreateTakeOverTaskReq.

        批量托管时的文件后缀名列表。不传或传空值时，表示托管所有音视频文件，不进行后缀名过滤。

        :return: The suffix of this CreateTakeOverTaskReq.
        :rtype: list[str]
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this CreateTakeOverTaskReq.

        批量托管时的文件后缀名列表。不传或传空值时，表示托管所有音视频文件，不进行后缀名过滤。

        :param suffix: The suffix of this CreateTakeOverTaskReq.
        :type: list[str]
        """
        self._suffix = suffix

    @property
    def template_group_name(self):
        """Gets the template_group_name of this CreateTakeOverTaskReq.

        转码模板组名称。  若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见转码设置。  > 若同时设置了“**template_group_name**”和“**workflow_name**”字段，则“**template_group_name**”字段生效。

        :return: The template_group_name of this CreateTakeOverTaskReq.
        :rtype: str
        """
        return self._template_group_name

    @template_group_name.setter
    def template_group_name(self, template_group_name):
        """Sets the template_group_name of this CreateTakeOverTaskReq.

        转码模板组名称。  若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见转码设置。  > 若同时设置了“**template_group_name**”和“**workflow_name**”字段，则“**template_group_name**”字段生效。

        :param template_group_name: The template_group_name of this CreateTakeOverTaskReq.
        :type: str
        """
        self._template_group_name = template_group_name

    @property
    def workflow_name(self):
        """Gets the workflow_name of this CreateTakeOverTaskReq.

        工作流名称。  若不为空，则使用指定的工作流对上传的音视频进行处理，您可以在视频点播控制台配置工作流，具体请参见[工作流设置](https://support.huaweicloud.com/usermanual-vod/vod010041.html)。

        :return: The workflow_name of this CreateTakeOverTaskReq.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this CreateTakeOverTaskReq.

        工作流名称。  若不为空，则使用指定的工作流对上传的音视频进行处理，您可以在视频点播控制台配置工作流，具体请参见[工作流设置](https://support.huaweicloud.com/usermanual-vod/vod010041.html)。

        :param workflow_name: The workflow_name of this CreateTakeOverTaskReq.
        :type: str
        """
        self._workflow_name = workflow_name

    @property
    def host_type(self):
        """Gets the host_type of this CreateTakeOverTaskReq.

        表示音视频处理后生成的媒资文件所存储的位置类型。  取值如下所示： - 0：表示存储到点播桶。 - 1：表示存储在租户桶。 - 2：表示存储到租户桶，并且存储路径与源文件一致。

        :return: The host_type of this CreateTakeOverTaskReq.
        :rtype: int
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this CreateTakeOverTaskReq.

        表示音视频处理后生成的媒资文件所存储的位置类型。  取值如下所示： - 0：表示存储到点播桶。 - 1：表示存储在租户桶。 - 2：表示存储到租户桶，并且存储路径与源文件一致。

        :param host_type: The host_type of this CreateTakeOverTaskReq.
        :type: int
        """
        self._host_type = host_type

    @property
    def output_bucket(self):
        """Gets the output_bucket of this CreateTakeOverTaskReq.

        输出桶名，host_type为1时必选

        :return: The output_bucket of this CreateTakeOverTaskReq.
        :rtype: str
        """
        return self._output_bucket

    @output_bucket.setter
    def output_bucket(self, output_bucket):
        """Sets the output_bucket of this CreateTakeOverTaskReq.

        输出桶名，host_type为1时必选

        :param output_bucket: The output_bucket of this CreateTakeOverTaskReq.
        :type: str
        """
        self._output_bucket = output_bucket

    @property
    def output_path(self):
        """Gets the output_path of this CreateTakeOverTaskReq.

        输出路径名，host_type为1时必选

        :return: The output_path of this CreateTakeOverTaskReq.
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """Sets the output_path of this CreateTakeOverTaskReq.

        输出路径名，host_type为1时必选

        :param output_path: The output_path of this CreateTakeOverTaskReq.
        :type: str
        """
        self._output_path = output_path

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
        if not isinstance(other, CreateTakeOverTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
