# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class VodClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(VodClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvod.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "VodClient":
            raise TypeError("client type error, support client type is VodClient")

        return ClientBuilder(clazz)

    def cancel_asset_transcode_task(self, request):
        """取消媒资转码任务

        取消媒资转码任务，只能取消排队中的转码任务。

        :param CancelAssetTranscodeTaskRequest request
        :return: CancelAssetTranscodeTaskResponse
        """
        return self.cancel_asset_transcode_task_with_http_info(request)

    def cancel_asset_transcode_task_with_http_info(self, request):
        """取消媒资转码任务

        取消媒资转码任务，只能取消排队中的转码任务。

        :param CancelAssetTranscodeTaskRequest request
        :return: CancelAssetTranscodeTaskResponse
        """

        all_params = ['asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/process',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelAssetTranscodeTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_extract_audio_task(self, request):
        """取消提取音频任务

        取消提取音频任务，只有排队中的提取音频任务才可以取消。

        :param CancelExtractAudioTaskRequest request
        :return: CancelExtractAudioTaskResponse
        """
        return self.cancel_extract_audio_task_with_http_info(request)

    def cancel_extract_audio_task_with_http_info(self, request):
        """取消提取音频任务

        取消提取音频任务，只有排队中的提取音频任务才可以取消。

        :param CancelExtractAudioTaskRequest request
        :return: CancelExtractAudioTaskResponse
        """

        all_params = ['asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/extract_audio',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelExtractAudioTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_md5_duplication(self, request):
        """上传检验

        校验媒资文件是否已存储于视频点播服务中。

        :param CheckMd5DuplicationRequest request
        :return: CheckMd5DuplicationResponse
        """
        return self.check_md5_duplication_with_http_info(request)

    def check_md5_duplication_with_http_info(self, request):
        """上传检验

        校验媒资文件是否已存储于视频点播服务中。

        :param CheckMd5DuplicationRequest request
        :return: CheckMd5DuplicationResponse
        """

        all_params = ['size', 'md5']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'md5' in local_var_params:
            query_params.append(('md5', local_var_params['md5']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/duplication',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckMd5DuplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def confirm_asset_upload(self, request):
        """确认媒资上传

        媒资分段上传完成后，需要调用此接口通知点播服务媒资上传的状态，表示媒资上传创建完成。 

        :param ConfirmAssetUploadRequest request
        :return: ConfirmAssetUploadResponse
        """
        return self.confirm_asset_upload_with_http_info(request)

    def confirm_asset_upload_with_http_info(self, request):
        """确认媒资上传

        媒资分段上传完成后，需要调用此接口通知点播服务媒资上传的状态，表示媒资上传创建完成。 

        :param ConfirmAssetUploadRequest request
        :return: ConfirmAssetUploadResponse
        """

        all_params = ['confirm_asset_upload_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/status/uploaded',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConfirmAssetUploadResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def confirm_image_upload(self, request):
        """确认水印图片上传

        ## 典型场景 ##   确认水印图片上传调用此接口<br/>  ## 接口功能 ##   确认水印图片是否已经上传至对象存储<br/>  ## 接口约束 ##   无。<br/> 

        :param ConfirmImageUploadRequest request
        :return: ConfirmImageUploadResponse
        """
        return self.confirm_image_upload_with_http_info(request)

    def confirm_image_upload_with_http_info(self, request):
        """确认水印图片上传

        ## 典型场景 ##   确认水印图片上传调用此接口<br/>  ## 接口功能 ##   确认水印图片是否已经上传至对象存储<br/>  ## 接口约束 ##   无。<br/> 

        :param ConfirmImageUploadRequest request
        :return: ConfirmImageUploadResponse
        """

        all_params = ['confirm_image_upload_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/watermark/status/uploaded',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConfirmImageUploadResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_asset_by_file_upload(self, request):
        """创建媒资：上传方式

        调用该接口创建媒资时，需要将对应的媒资文件上传到点播服务的OBS桶中。  若上传的单媒资文件大小小于20M，则可以直接用PUT方法对该接口返回的地址进行上传。具体使用方法请参考[示例1：媒资上传（20M以下）](https://support.huaweicloud.com/api-vod/vod_04_0195.html)。  若上传的单个媒资大小大于20M，则需要进行二进制流分割后上传，该接口的具体使用方法请参考[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。

        :param CreateAssetByFileUploadRequest request
        :return: CreateAssetByFileUploadResponse
        """
        return self.create_asset_by_file_upload_with_http_info(request)

    def create_asset_by_file_upload_with_http_info(self, request):
        """创建媒资：上传方式

        调用该接口创建媒资时，需要将对应的媒资文件上传到点播服务的OBS桶中。  若上传的单媒资文件大小小于20M，则可以直接用PUT方法对该接口返回的地址进行上传。具体使用方法请参考[示例1：媒资上传（20M以下）](https://support.huaweicloud.com/api-vod/vod_04_0195.html)。  若上传的单个媒资大小大于20M，则需要进行二进制流分割后上传，该接口的具体使用方法请参考[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。

        :param CreateAssetByFileUploadRequest request
        :return: CreateAssetByFileUploadResponse
        """

        all_params = ['create_asset_by_file_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAssetByFileUploadResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_asset_category(self, request):
        """创建媒资分类

        ## 功能介绍 ##   创建媒资分类。<br/>  ## 接口约束 ##   最大支持三级分类，每个分类最多支持创建128个子分类。<br/> 

        :param CreateAssetCategoryRequest request
        :return: CreateAssetCategoryResponse
        """
        return self.create_asset_category_with_http_info(request)

    def create_asset_category_with_http_info(self, request):
        """创建媒资分类

        ## 功能介绍 ##   创建媒资分类。<br/>  ## 接口约束 ##   最大支持三级分类，每个分类最多支持创建128个子分类。<br/> 

        :param CreateAssetCategoryRequest request
        :return: CreateAssetCategoryResponse
        """

        all_params = ['create_category_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/category',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAssetCategoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_asset_process_task(self, request):
        """媒资处理

        实现视频转码、截图、加密等处理。既可以同时启动多种操作，也可以只启动一种操作。 

        :param CreateAssetProcessTaskRequest request
        :return: CreateAssetProcessTaskResponse
        """
        return self.create_asset_process_task_with_http_info(request)

    def create_asset_process_task_with_http_info(self, request):
        """媒资处理

        实现视频转码、截图、加密等处理。既可以同时启动多种操作，也可以只启动一种操作。 

        :param CreateAssetProcessTaskRequest request
        :return: CreateAssetProcessTaskResponse
        """

        all_params = ['asset_process_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/process',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAssetProcessTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_asset_review_task(self, request):
        """创建审核媒资任务

        ## 功能介绍 ## 对上传的媒资进行审核。审核后，可以调用[查询媒资详细信息](https://support.huaweicloud.com/api-vod/vod_04_0202.html)接口查看审核结果。  ## 接口约束 ## 目前“华东-上海二”区域的点播服务暂不支持此功能。

        :param CreateAssetReviewTaskRequest request
        :return: CreateAssetReviewTaskResponse
        """
        return self.create_asset_review_task_with_http_info(request)

    def create_asset_review_task_with_http_info(self, request):
        """创建审核媒资任务

        ## 功能介绍 ## 对上传的媒资进行审核。审核后，可以调用[查询媒资详细信息](https://support.huaweicloud.com/api-vod/vod_04_0202.html)接口查看审核结果。  ## 接口约束 ## 目前“华东-上海二”区域的点播服务暂不支持此功能。

        :param CreateAssetReviewTaskRequest request
        :return: CreateAssetReviewTaskResponse
        """

        all_params = ['asset_review_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/review',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAssetReviewTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_extract_audio_task(self, request):
        """音频提取

        用于从已有视频文件中提取音频。 

        :param CreateExtractAudioTaskRequest request
        :return: CreateExtractAudioTaskResponse
        """
        return self.create_extract_audio_task_with_http_info(request)

    def create_extract_audio_task_with_http_info(self, request):
        """音频提取

        用于从已有视频文件中提取音频。 

        :param CreateExtractAudioTaskRequest request
        :return: CreateExtractAudioTaskResponse
        """

        all_params = ['extract_audio_task_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/extract_audio',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateExtractAudioTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_template_group(self, request):
        """创建自定义模板组

        ## 典型场景 ##   创建自定义模板组时调用此接口。<br/>  ## 接口功能 ##   创建模板组。<br/>  ## 接口约束 ##   无。<br/> 

        :param CreateTemplateGroupRequest request
        :return: CreateTemplateGroupResponse
        """
        return self.create_template_group_with_http_info(request)

    def create_template_group_with_http_info(self, request):
        """创建自定义模板组

        ## 典型场景 ##   创建自定义模板组时调用此接口。<br/>  ## 接口功能 ##   创建模板组。<br/>  ## 接口约束 ##   无。<br/> 

        :param CreateTemplateGroupRequest request
        :return: CreateTemplateGroupResponse
        """

        all_params = ['trans_template_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/template_group/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_watermark_template(self, request):
        """创建水印模板

        ## 典型场景 ##   创建水印模板调用此接口<br/>  ## 接口功能 ##   创建水印模板<br/>  ## 接口约束 ##   无。<br/> 

        :param CreateWatermarkTemplateRequest request
        :return: CreateWatermarkTemplateResponse
        """
        return self.create_watermark_template_with_http_info(request)

    def create_watermark_template_with_http_info(self, request):
        """创建水印模板

        ## 典型场景 ##   创建水印模板调用此接口<br/>  ## 接口功能 ##   创建水印模板<br/>  ## 接口约束 ##   无。<br/> 

        :param CreateWatermarkTemplateRequest request
        :return: CreateWatermarkTemplateResponse
        """

        all_params = ['create_watermark_template_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/template/watermark',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_asset_category(self, request):
        """删除媒资分类

        删除媒资分类。 

        :param DeleteAssetCategoryRequest request
        :return: DeleteAssetCategoryResponse
        """
        return self.delete_asset_category_with_http_info(request)

    def delete_asset_category_with_http_info(self, request):
        """删除媒资分类

        删除媒资分类。 

        :param DeleteAssetCategoryRequest request
        :return: DeleteAssetCategoryResponse
        """

        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/category',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAssetCategoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_assets(self, request):
        """删除媒资

        ## 功能介绍 ## 删除媒资。  ## 接口约束 ## 正在处理中的媒资不支持删除，包括转码中、审核中、截图中等。

        :param DeleteAssetsRequest request
        :return: DeleteAssetsResponse
        """
        return self.delete_assets_with_http_info(request)

    def delete_assets_with_http_info(self, request):
        """删除媒资

        ## 功能介绍 ## 删除媒资。  ## 接口约束 ## 正在处理中的媒资不支持删除，包括转码中、审核中、截图中等。

        :param DeleteAssetsRequest request
        :return: DeleteAssetsResponse
        """

        all_params = ['asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
            collection_formats['asset_id'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAssetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_template_group(self, request):
        """删除自定义模板组

        ## 典型场景 ##   删除自定义模板组接口。<br/>  ## 接口功能 ##   删除自定义模板组。<br/>  ## 接口约束 ##   无。<br/> 

        :param DeleteTemplateGroupRequest request
        :return: DeleteTemplateGroupResponse
        """
        return self.delete_template_group_with_http_info(request)

    def delete_template_group_with_http_info(self, request):
        """删除自定义模板组

        ## 典型场景 ##   删除自定义模板组接口。<br/>  ## 接口功能 ##   删除自定义模板组。<br/>  ## 接口约束 ##   无。<br/> 

        :param DeleteTemplateGroupRequest request
        :return: DeleteTemplateGroupResponse
        """

        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/template_group/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_watermark_template(self, request):
        """删除水印模板

        ## 典型场景 ##   删除水印模板<br/>  ## 接口功能 ##   删除水印模板<br/>  ## 接口约束 ##   无<br/> 

        :param DeleteWatermarkTemplateRequest request
        :return: DeleteWatermarkTemplateResponse
        """
        return self.delete_watermark_template_with_http_info(request)

    def delete_watermark_template_with_http_info(self, request):
        """删除水印模板

        ## 典型场景 ##   删除水印模板<br/>  ## 接口功能 ##   删除水印模板<br/>  ## 接口约束 ##   无<br/> 

        :param DeleteWatermarkTemplateRequest request
        :return: DeleteWatermarkTemplateResponse
        """

        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/template/watermark',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_asset_category(self, request):
        """查询指定分类信息

        查询指定分类信息，及其子分类（即下一级分类）的列表。

        :param ListAssetCategoryRequest request
        :return: ListAssetCategoryResponse
        """
        return self.list_asset_category_with_http_info(request)

    def list_asset_category_with_http_info(self, request):
        """查询指定分类信息

        查询指定分类信息，及其子分类（即下一级分类）的列表。

        :param ListAssetCategoryRequest request
        :return: ListAssetCategoryResponse
        """

        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/category',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAssetCategoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_asset_list(self, request):
        """查询媒资列表

        查询媒资列表，列表中的每一条记录包含媒资的概要信息。

        :param ListAssetListRequest request
        :return: ListAssetListResponse
        """
        return self.list_asset_list_with_http_info(request)

    def list_asset_list_with_http_info(self, request):
        """查询媒资列表

        查询媒资列表，列表中的每一条记录包含媒资的概要信息。

        :param ListAssetListRequest request
        :return: ListAssetListResponse
        """

        all_params = ['asset_id', 'status', 'start_time', 'end_time', 'category_id', 'tags', 'query_string', 'media_type', 'page', 'size', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
            collection_formats['asset_id'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'category_id' in local_var_params:
            query_params.append(('category_id', local_var_params['category_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'query_string' in local_var_params:
            query_params.append(('query_string', local_var_params['query_string']))
        if 'media_type' in local_var_params:
            query_params.append(('media_type', local_var_params['media_type']))
            collection_formats['media_type'] = 'csv'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAssetListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_template_group(self, request):
        """查询模板组列表

        ## 典型场景 ##   查询模板组列表调用此接口。<br/>  ## 接口功能 ##   查询模板组列表。<br/>  ## 接口约束 ##   无。<br/> 

        :param ListTemplateGroupRequest request
        :return: ListTemplateGroupResponse
        """
        return self.list_template_group_with_http_info(request)

    def list_template_group_with_http_info(self, request):
        """查询模板组列表

        ## 典型场景 ##   查询模板组列表调用此接口。<br/>  ## 接口功能 ##   查询模板组列表。<br/>  ## 接口约束 ##   无。<br/> 

        :param ListTemplateGroupRequest request
        :return: ListTemplateGroupResponse
        """

        all_params = ['group_id', 'status', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/template_group/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_top_statistics(self, request):
        """查询TopN媒资信息

        查询指定域名在指定日期播放次数排名Top 100的媒资统计数据。

        :param ListTopStatisticsRequest request
        :return: ListTopStatisticsResponse
        """
        return self.list_top_statistics_with_http_info(request)

    def list_top_statistics_with_http_info(self, request):
        """查询TopN媒资信息

        查询指定域名在指定日期播放次数排名Top 100的媒资统计数据。

        :param ListTopStatisticsRequest request
        :return: ListTopStatisticsResponse
        """

        all_params = ['domain', 'date']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'date' in local_var_params:
            query_params.append(('date', local_var_params['date']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/top-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTopStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_watermark_template(self, request):
        """查询水印列表

        ## 典型场景 ##   查询水印模板<br/>  ## 接口功能 ##   查询水印模板<br/>  ## 接口约束 ##   查询所有水印<br/> 

        :param ListWatermarkTemplateRequest request
        :return: ListWatermarkTemplateResponse
        """
        return self.list_watermark_template_with_http_info(request)

    def list_watermark_template_with_http_info(self, request):
        """查询水印列表

        ## 典型场景 ##   查询水印模板<br/>  ## 接口功能 ##   查询水印模板<br/>  ## 接口约束 ##   查询所有水印<br/> 

        :param ListWatermarkTemplateRequest request
        :return: ListWatermarkTemplateResponse
        """

        all_params = ['id', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/template/watermark',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def publish_asset_from_obs(self, request):
        """创建媒资：OBS转存方式

        ## 功能介绍 ##   若您在使用点播服务前，已经在OBS桶中存储了音视频文件，您可以使用该接口将存储在OBS桶中的音视频文件转存到点播服务中，使用点播服务的音视频管理功能。调用该接口前，您需要调用[桶授权](https://support.huaweicloud.com/api-vod/vod_04_0199.html)接口，将存储音视频文件的OBS桶授权给点播服务。<br/>  ## 接口约束 ##   由于不同区域的云服务不能互连，所以待转存的OBS桶和点播服务必须在同一区域，如“华北-北京四”OBS桶中的音视频只能转存到“华北-北京四”点播服务中。<br/>

        :param PublishAssetFromObsRequest request
        :return: PublishAssetFromObsResponse
        """
        return self.publish_asset_from_obs_with_http_info(request)

    def publish_asset_from_obs_with_http_info(self, request):
        """创建媒资：OBS转存方式

        ## 功能介绍 ##   若您在使用点播服务前，已经在OBS桶中存储了音视频文件，您可以使用该接口将存储在OBS桶中的音视频文件转存到点播服务中，使用点播服务的音视频管理功能。调用该接口前，您需要调用[桶授权](https://support.huaweicloud.com/api-vod/vod_04_0199.html)接口，将存储音视频文件的OBS桶授权给点播服务。<br/>  ## 接口约束 ##   由于不同区域的云服务不能互连，所以待转存的OBS桶和点播服务必须在同一区域，如“华北-北京四”OBS桶中的音视频只能转存到“华北-北京四”点播服务中。<br/>

        :param PublishAssetFromObsRequest request
        :return: PublishAssetFromObsResponse
        """

        all_params = ['publish_asset_from_obs_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/reproduction',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='PublishAssetFromObsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def publish_assets(self, request):
        """媒资发布

        将媒资设置为发布状态。支持批量发布。 

        :param PublishAssetsRequest request
        :return: PublishAssetsResponse
        """
        return self.publish_assets_with_http_info(request)

    def publish_assets_with_http_info(self, request):
        """媒资发布

        将媒资设置为发布状态。支持批量发布。 

        :param PublishAssetsRequest request
        :return: PublishAssetsResponse
        """

        all_params = ['publish_asset_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/status/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='PublishAssetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_asset_detail(self, request):
        """查询指定媒资的详细信息

        查询指定媒资的详细信息。

        :param ShowAssetDetailRequest request
        :return: ShowAssetDetailResponse
        """
        return self.show_asset_detail_with_http_info(request)

    def show_asset_detail_with_http_info(self, request):
        """查询指定媒资的详细信息

        查询指定媒资的详细信息。

        :param ShowAssetDetailRequest request
        :return: ShowAssetDetailResponse
        """

        all_params = ['asset_id', 'categories']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
        if 'categories' in local_var_params:
            query_params.append(('categories', local_var_params['categories']))
            collection_formats['categories'] = 'csv'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAssetDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_asset_meta(self, request):
        """查询媒资信息

        查询媒资信息，支持指定媒资ID、分类、状态、起止时间查询。

        :param ShowAssetMetaRequest request
        :return: ShowAssetMetaResponse
        """
        return self.show_asset_meta_with_http_info(request)

    def show_asset_meta_with_http_info(self, request):
        """查询媒资信息

        查询媒资信息，支持指定媒资ID、分类、状态、起止时间查询。

        :param ShowAssetMetaRequest request
        :return: ShowAssetMetaResponse
        """

        all_params = ['asset_id', 'status', 'transcode_status', 'asset_status', 'start_time', 'end_time', 'category_id', 'tags', 'query_string', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
            collection_formats['asset_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'transcode_status' in local_var_params:
            query_params.append(('transcodeStatus', local_var_params['transcode_status']))
            collection_formats['transcodeStatus'] = 'multi'
        if 'asset_status' in local_var_params:
            query_params.append(('assetStatus', local_var_params['asset_status']))
            collection_formats['assetStatus'] = 'multi'
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'category_id' in local_var_params:
            query_params.append(('category_id', local_var_params['category_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'query_string' in local_var_params:
            query_params.append(('query_string', local_var_params['query_string']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAssetMetaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_asset_temp_authority(self, request):
        """获取分段上传授权

        客户端请求创建媒资时，如果媒资文件超过20MB，需采用分段的方式向OBS上传，在每次与OBS交互前，客户端需通过此接口获取到授权方可与OBS交互。  该接口可以获取[初始化多段上传任务](https://support.huaweicloud.com/api-obs/obs_04_0098.html)、[上传段](https://support.huaweicloud.com/api-obs/obs_04_0099.html)、[合并段](https://support.huaweicloud.com/api-obs/obs_04_0102.html)、[列举已上传段](https://support.huaweicloud.com/api-obs/obs_04_0101.html)、[取消段合并](https://support.huaweicloud.com/api-obs/obs_04_0103.html)的带有临时授权的URL，用户需要根据OBS的接口文档配置相应请求的HTTP请求方法、请求头、请求体，然后请求对应的带有临时授权的URL。  视频分段上传方式和OBS的接口文档保持一致，包括HTTP请求方法、请求头、请求体等各种入参，此接口的作用是为用户生成带有鉴权信息的URL（鉴权信息即query_str），用来替换OBS接口中对应的URL，临时给用户开通向点播服务的桶上传文件的权限。  调用获取授权接口时需要传入bucket、object_key、http_verb，其中bucket和object_key是由[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的bucket和object，http_verb需要根据指定的操作选择。

        :param ShowAssetTempAuthorityRequest request
        :return: ShowAssetTempAuthorityResponse
        """
        return self.show_asset_temp_authority_with_http_info(request)

    def show_asset_temp_authority_with_http_info(self, request):
        """获取分段上传授权

        客户端请求创建媒资时，如果媒资文件超过20MB，需采用分段的方式向OBS上传，在每次与OBS交互前，客户端需通过此接口获取到授权方可与OBS交互。  该接口可以获取[初始化多段上传任务](https://support.huaweicloud.com/api-obs/obs_04_0098.html)、[上传段](https://support.huaweicloud.com/api-obs/obs_04_0099.html)、[合并段](https://support.huaweicloud.com/api-obs/obs_04_0102.html)、[列举已上传段](https://support.huaweicloud.com/api-obs/obs_04_0101.html)、[取消段合并](https://support.huaweicloud.com/api-obs/obs_04_0103.html)的带有临时授权的URL，用户需要根据OBS的接口文档配置相应请求的HTTP请求方法、请求头、请求体，然后请求对应的带有临时授权的URL。  视频分段上传方式和OBS的接口文档保持一致，包括HTTP请求方法、请求头、请求体等各种入参，此接口的作用是为用户生成带有鉴权信息的URL（鉴权信息即query_str），用来替换OBS接口中对应的URL，临时给用户开通向点播服务的桶上传文件的权限。  调用获取授权接口时需要传入bucket、object_key、http_verb，其中bucket和object_key是由[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的bucket和object，http_verb需要根据指定的操作选择。

        :param ShowAssetTempAuthorityRequest request
        :return: ShowAssetTempAuthorityResponse
        """

        all_params = ['http_verb', 'bucket', 'object_key', 'content_type', 'content_md5', 'upload_id', 'part_number']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'http_verb' in local_var_params:
            query_params.append(('http_verb', local_var_params['http_verb']))
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))
        if 'object_key' in local_var_params:
            query_params.append(('object_key', local_var_params['object_key']))
        if 'content_type' in local_var_params:
            query_params.append(('content_type', local_var_params['content_type']))
        if 'content_md5' in local_var_params:
            query_params.append(('content_md5', local_var_params['content_md5']))
        if 'upload_id' in local_var_params:
            query_params.append(('upload_id', local_var_params['upload_id']))
        if 'part_number' in local_var_params:
            query_params.append(('part_number', local_var_params['part_number']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.1/{project_id}/asset/authority',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAssetTempAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cdn_statistics(self, request):
        """查询CDN统计信息

        查询CDN的统计数据，包括流量、峰值带宽、请求总数、请求命中率、流量命中率。

        :param ShowCdnStatisticsRequest request
        :return: ShowCdnStatisticsResponse
        """
        return self.show_cdn_statistics_with_http_info(request)

    def show_cdn_statistics_with_http_info(self, request):
        """查询CDN统计信息

        查询CDN的统计数据，包括流量、峰值带宽、请求总数、请求命中率、流量命中率。

        :param ShowCdnStatisticsRequest request
        :return: ShowCdnStatisticsResponse
        """

        all_params = ['stat_type', 'domain', 'start_time', 'end_time', 'interval']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/cdn-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCdnStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vod_statistics(self, request):
        """查询源站统计信息

        查询点播源站的统计数据，包括流量、存储空间、转码时长。

        :param ShowVodStatisticsRequest request
        :return: ShowVodStatisticsResponse
        """
        return self.show_vod_statistics_with_http_info(request)

    def show_vod_statistics_with_http_info(self, request):
        """查询源站统计信息

        查询点播源站的统计数据，包括流量、存储空间、转码时长。

        :param ShowVodStatisticsRequest request
        :return: ShowVodStatisticsResponse
        """

        all_params = ['start_time', 'end_time', 'interval']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/vod-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVodStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def unpublish_assets(self, request):
        """媒资发布取消

        将媒资设置为未发布状态。 

        :param UnpublishAssetsRequest request
        :return: UnpublishAssetsResponse
        """
        return self.unpublish_assets_with_http_info(request)

    def unpublish_assets_with_http_info(self, request):
        """媒资发布取消

        将媒资设置为未发布状态。 

        :param UnpublishAssetsRequest request
        :return: UnpublishAssetsResponse
        """

        all_params = ['unpublish_asset_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/status/unpublish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UnpublishAssetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_asset(self, request):
        """视频更新

        媒资创建后，单独上传封面、更新视频文件或更新已有封面。 如果是更新视频文件，更新完后要通过[确认媒资上传](https://support.huaweicloud.com/api-vod/vod_04_0198.html)接口通知点播服务。 如果是更新封面或单独上传封面，则不需通知。 更新视频可以使用分段上传，具体方式可以参考[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。

        :param UpdateAssetRequest request
        :return: UpdateAssetResponse
        """
        return self.update_asset_with_http_info(request)

    def update_asset_with_http_info(self, request):
        """视频更新

        媒资创建后，单独上传封面、更新视频文件或更新已有封面。 如果是更新视频文件，更新完后要通过[确认媒资上传](https://support.huaweicloud.com/api-vod/vod_04_0198.html)接口通知点播服务。 如果是更新封面或单独上传封面，则不需通知。 更新视频可以使用分段上传，具体方式可以参考[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。

        :param UpdateAssetRequest request
        :return: UpdateAssetResponse
        """

        all_params = ['upload_asset_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_asset_category(self, request):
        """修改媒资分类

        修改媒资分类。 

        :param UpdateAssetCategoryRequest request
        :return: UpdateAssetCategoryResponse
        """
        return self.update_asset_category_with_http_info(request)

    def update_asset_category_with_http_info(self, request):
        """修改媒资分类

        修改媒资分类。 

        :param UpdateAssetCategoryRequest request
        :return: UpdateAssetCategoryResponse
        """

        all_params = ['update_category_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/category',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAssetCategoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_asset_meta(self, request):
        """修改媒资属性

        修改媒资属性。 

        :param UpdateAssetMetaRequest request
        :return: UpdateAssetMetaResponse
        """
        return self.update_asset_meta_with_http_info(request)

    def update_asset_meta_with_http_info(self, request):
        """修改媒资属性

        修改媒资属性。 

        :param UpdateAssetMetaRequest request
        :return: UpdateAssetMetaResponse
        """

        all_params = ['update_asset_meta_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAssetMetaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_bucket_authorized(self, request):
        """桶授权

        用户可以通过该接口将OBS桶授权给点播服务或取消点播服务的授权。 

        :param UpdateBucketAuthorizedRequest request
        :return: UpdateBucketAuthorizedResponse
        """
        return self.update_bucket_authorized_with_http_info(request)

    def update_bucket_authorized_with_http_info(self, request):
        """桶授权

        用户可以通过该接口将OBS桶授权给点播服务或取消点播服务的授权。 

        :param UpdateBucketAuthorizedRequest request
        :return: UpdateBucketAuthorizedResponse
        """

        all_params = ['update_bucket_authorized_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/authority',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateBucketAuthorizedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_cover_by_thumbnail(self, request):
        """设置封面

        将视频截图生成的某张图片设置成封面。

        :param UpdateCoverByThumbnailRequest request
        :return: UpdateCoverByThumbnailResponse
        """
        return self.update_cover_by_thumbnail_with_http_info(request)

    def update_cover_by_thumbnail_with_http_info(self, request):
        """设置封面

        将视频截图生成的某张图片设置成封面。

        :param UpdateCoverByThumbnailRequest request
        :return: UpdateCoverByThumbnailResponse
        """

        all_params = ['update_cover_by_thumbnail_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/cover',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCoverByThumbnailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_template_group(self, request):
        """修改模板组

        ## 典型场景 ##  修改模板组接口。<br/>  ## 接口功能 ##   修改模板组。<br/>  ## 接口约束 ##   无。<br/> 

        :param UpdateTemplateGroupRequest request
        :return: UpdateTemplateGroupResponse
        """
        return self.update_template_group_with_http_info(request)

    def update_template_group_with_http_info(self, request):
        """修改模板组

        ## 典型场景 ##  修改模板组接口。<br/>  ## 接口功能 ##   修改模板组。<br/>  ## 接口约束 ##   无。<br/> 

        :param UpdateTemplateGroupRequest request
        :return: UpdateTemplateGroupResponse
        """

        all_params = ['trans_template_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/template_group/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_watermark_template(self, request):
        """修改水印模板

        ## 典型场景 ##   修改水印模板<br/>  ## 接口功能 ##   修改水印模板<br/>  ## 接口约束 ##   无<br/> 

        :param UpdateWatermarkTemplateRequest request
        :return: UpdateWatermarkTemplateResponse
        """
        return self.update_watermark_template_with_http_info(request)

    def update_watermark_template_with_http_info(self, request):
        """修改水印模板

        ## 典型场景 ##   修改水印模板<br/>  ## 接口功能 ##   修改水印模板<br/>  ## 接口约束 ##   无<br/> 

        :param UpdateWatermarkTemplateRequest request
        :return: UpdateWatermarkTemplateResponse
        """

        all_params = ['update_watermark_template_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/template/watermark',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def upload_meta_data_by_url(self, request):
        """创建媒资：URL拉取注入

        基于音视频源文件URL，将音视频文件离线拉取上传到点播服务。 

        :param UploadMetaDataByUrlRequest request
        :return: UploadMetaDataByUrlResponse
        """
        return self.upload_meta_data_by_url_with_http_info(request)

    def upload_meta_data_by_url_with_http_info(self, request):
        """创建媒资：URL拉取注入

        基于音视频源文件URL，将音视频文件离线拉取上传到点播服务。 

        :param UploadMetaDataByUrlRequest request
        :return: UploadMetaDataByUrlResponse
        """

        all_params = ['upload_meta_data_by_url_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/upload_by_url',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UploadMetaDataByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_preheating_asset(self, request):
        """CDN预热

        媒资发布后，可通过指定媒资ID或URL向CDN预热。用户初次请求时，将由CDN节点提供请求媒资，加快用户下载缓存时间，提高用户体验。

        :param CreatePreheatingAssetRequest request
        :return: CreatePreheatingAssetResponse
        """
        return self.create_preheating_asset_with_http_info(request)

    def create_preheating_asset_with_http_info(self, request):
        """CDN预热

        媒资发布后，可通过指定媒资ID或URL向CDN预热。用户初次请求时，将由CDN节点提供请求媒资，加快用户下载缓存时间，提高用户体验。

        :param CreatePreheatingAssetRequest request
        :return: CreatePreheatingAssetResponse
        """

        all_params = ['create_preheating_asset_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/preheating',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePreheatingAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_preheating_asset(self, request):
        """查询CDN预热

        查询预热结果。 

        :param ShowPreheatingAssetRequest request
        :return: ShowPreheatingAssetResponse
        """
        return self.show_preheating_asset_with_http_info(request)

    def show_preheating_asset_with_http_info(self, request):
        """查询CDN预热

        查询预热结果。 

        :param ShowPreheatingAssetRequest request
        :return: ShowPreheatingAssetResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/preheating',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPreheatingAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_asset_cipher(self, request):
        """密钥查询接口

        终端播放HLS加密视频时，向租户管理系统请求密钥，租户管理系统先查询其本地有没有已缓存的密钥，没有时则调用此接口向VOD查询。该接口的具体使用场景请参见[通过HLS加密防止视频泄露](https://support.huaweicloud.com/bestpractice-vod/vod_10_0004.html)。

        :param ShowAssetCipherRequest request
        :return: ShowAssetCipherResponse
        """
        return self.show_asset_cipher_with_http_info(request)

    def show_asset_cipher_with_http_info(self, request):
        """密钥查询接口

        终端播放HLS加密视频时，向租户管理系统请求密钥，租户管理系统先查询其本地有没有已缓存的密钥，没有时则调用此接口向VOD查询。该接口的具体使用场景请参见[通过HLS加密防止视频泄露](https://support.huaweicloud.com/bestpractice-vod/vod_10_0004.html)。

        :param ShowAssetCipherRequest request
        :return: ShowAssetCipherResponse
        """

        all_params = ['asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/ciphers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAssetCipherResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_take_over_task(self, request):
        """创建媒资：OBS托管方式

        通过存量托管的方式，将已存储在OBS桶中的音视频文件同步到点播服务。  OBS托管方式分为增量托管和存量托管，增量托管暂只支持通过视频点播控制台配置，配置后，若OBS有新增音视频文件，则会自动同步到点播服务中，具体请参见[增量托管](https://support.huaweicloud.com/usermanual-vod/vod010032.html)。两个托管方式都需要先将对应的OBS桶授权给点播服务，具体请参见[桶授权](https://support.huaweicloud.com/usermanual-vod/vod010031.html)。 

        :param CreateTakeOverTaskRequest request
        :return: CreateTakeOverTaskResponse
        """
        return self.create_take_over_task_with_http_info(request)

    def create_take_over_task_with_http_info(self, request):
        """创建媒资：OBS托管方式

        通过存量托管的方式，将已存储在OBS桶中的音视频文件同步到点播服务。  OBS托管方式分为增量托管和存量托管，增量托管暂只支持通过视频点播控制台配置，配置后，若OBS有新增音视频文件，则会自动同步到点播服务中，具体请参见[增量托管](https://support.huaweicloud.com/usermanual-vod/vod010032.html)。两个托管方式都需要先将对应的OBS桶授权给点播服务，具体请参见[桶授权](https://support.huaweicloud.com/usermanual-vod/vod010031.html)。 

        :param CreateTakeOverTaskRequest request
        :return: CreateTakeOverTaskResponse
        """

        all_params = ['create_take_over_task_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/obs/host/stock/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTakeOverTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_take_over_task(self, request):
        """查询托管任务

        ## 典型场景 ##   查询托管任务<br/>  ## 接口功能 ##   查询托管任务<br/>  ## 接口约束 ##<br/> 

        :param ListTakeOverTaskRequest request
        :return: ListTakeOverTaskResponse
        """
        return self.list_take_over_task_with_http_info(request)

    def list_take_over_task_with_http_info(self, request):
        """查询托管任务

        ## 典型场景 ##   查询托管任务<br/>  ## 接口功能 ##   查询托管任务<br/>  ## 接口约束 ##<br/> 

        :param ListTakeOverTaskRequest request
        :return: ListTakeOverTaskResponse
        """

        all_params = ['status', 'task_id', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/obs/host/stock/task',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTakeOverTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_take_over_asset_details(self, request):
        """查询托管媒资详情

        ## 典型场景 ##   查询托管媒资详情<br/>  ## 接口功能 ##   查询托管媒资详情<br/>  ## 接口约束 ##<br/> 

        :param ShowTakeOverAssetDetailsRequest request
        :return: ShowTakeOverAssetDetailsResponse
        """
        return self.show_take_over_asset_details_with_http_info(request)

    def show_take_over_asset_details_with_http_info(self, request):
        """查询托管媒资详情

        ## 典型场景 ##   查询托管媒资详情<br/>  ## 接口功能 ##   查询托管媒资详情<br/>  ## 接口约束 ##<br/> 

        :param ShowTakeOverAssetDetailsRequest request
        :return: ShowTakeOverAssetDetailsResponse
        """

        all_params = ['source_bucket', 'source_object']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source_bucket' in local_var_params:
            query_params.append(('source_bucket', local_var_params['source_bucket']))
        if 'source_object' in local_var_params:
            query_params.append(('source_object', local_var_params['source_object']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/obs/host/task/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTakeOverAssetDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_take_over_task_details(self, request):
        """查询托管任务详情

        ## 典型场景 ##   查询托管任务详情<br/>  ## 接口功能 ##   查询托管任务详情<br/>  ## 接口约束 ##<br/> 

        :param ShowTakeOverTaskDetailsRequest request
        :return: ShowTakeOverTaskDetailsResponse
        """
        return self.show_take_over_task_details_with_http_info(request)

    def show_take_over_task_details_with_http_info(self, request):
        """查询托管任务详情

        ## 典型场景 ##   查询托管任务详情<br/>  ## 接口功能 ##   查询托管任务详情<br/>  ## 接口约束 ##<br/> 

        :param ShowTakeOverTaskDetailsRequest request
        :return: ShowTakeOverTaskDetailsResponse
        """

        all_params = ['task_id', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/asset/obs/host/stock/task/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTakeOverTaskDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)