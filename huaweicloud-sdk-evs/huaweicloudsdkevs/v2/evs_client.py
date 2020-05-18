# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

# python 2 and python 3 compatibility library
import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


class EvsClient(Client):
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
        super(EvsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkevs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def batch_create_volume_tags(self, request):
        """为指定云硬盘批量添加标签

        为指定云硬盘批量添加标签。  添加标签时，如果云硬盘的标签已存在相同key，则会覆盖已有标签。 单个云硬盘最多支持创建10个标签。

        :param BatchCreateVolumeTagsRequest request
        :return: None
        """
        return self.batch_create_volume_tags_with_http_info(request)

    def batch_create_volume_tags_with_http_info(self, request):
        """为指定云硬盘批量添加标签

        为指定云硬盘批量添加标签。  添加标签时，如果云硬盘的标签已存在相同key，则会覆盖已有标签。 单个云硬盘最多支持创建10个标签。

        :param BatchCreateVolumeTagsRequest request
        :return: None
        """

        all_params = ['volume_id', 'batch_create_volume_tags_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/{volume_id}/tags/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_delete_volume_tags(self, request):
        """为指定云硬盘批量删除标签

        为指定云硬盘批量删除标签。

        :param BatchDeleteVolumeTagsRequest request
        :return: None
        """
        return self.batch_delete_volume_tags_with_http_info(request)

    def batch_delete_volume_tags_with_http_info(self, request):
        """为指定云硬盘批量删除标签

        为指定云硬盘批量删除标签。

        :param BatchDeleteVolumeTagsRequest request
        :return: None
        """

        all_params = ['volume_id', 'batch_delete_volume_tags_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/{volume_id}/tags/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def cinder_export_to_image(self, request):
        """将云硬盘导出为镜像

        将系统盘或数据盘的数据导出为镜像。

        :param CinderExportToImageRequest request
        :return: CinderExportToImageResponse
        """
        return self.cinder_export_to_image_with_http_info(request)

    def cinder_export_to_image_with_http_info(self, request):
        """将云硬盘导出为镜像

        将系统盘或数据盘的数据导出为镜像。

        :param CinderExportToImageRequest request
        :return: tuple(CinderExportToImageResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['volume_id', 'cinder_export_to_image_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/volumes/{volume_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CinderExportToImageResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def cinder_list_availability_zones(self, request):
        """查询所有的可用分区信息

        查询所有的可用分区信息。

        :param CinderListAvailabilityZonesRequest request
        :return: CinderListAvailabilityZonesResponse
        """
        return self.cinder_list_availability_zones_with_http_info(request)

    def cinder_list_availability_zones_with_http_info(self, request):
        """查询所有的可用分区信息

        查询所有的可用分区信息。

        :param CinderListAvailabilityZonesRequest request
        :return: tuple(CinderListAvailabilityZonesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/os-availability-zone', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CinderListAvailabilityZonesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def cinder_list_quotas(self, request):
        """查询租户的详细配额

        查询租户的详细配额。

        :param CinderListQuotasRequest request
        :return: CinderListQuotasResponse
        """
        return self.cinder_list_quotas_with_http_info(request)

    def cinder_list_quotas_with_http_info(self, request):
        """查询租户的详细配额

        查询租户的详细配额。

        :param CinderListQuotasRequest request
        :return: tuple(CinderListQuotasResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['target_project_id', 'usage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'target_project_id' in local_var_params:
            path_params['target_project_id'] = local_var_params['target_project_id']

        query_params = []
        if 'usage' in local_var_params:
            query_params.append(('usage', local_var_params['usage']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/os-quota-sets/{target_project_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CinderListQuotasResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def cinder_list_volume_types(self, request):
        """查询云硬盘类型列表

        查询云硬盘类型列表。

        :param CinderListVolumeTypesRequest request
        :return: CinderListVolumeTypesResponse
        """
        return self.cinder_list_volume_types_with_http_info(request)

    def cinder_list_volume_types_with_http_info(self, request):
        """查询云硬盘类型列表

        查询云硬盘类型列表。

        :param CinderListVolumeTypesRequest request
        :return: tuple(CinderListVolumeTypesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CinderListVolumeTypesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_snapshot(self, request):
        """创建云硬盘快照

        创建云硬盘快照。

        :param CreateSnapshotRequest request
        :return: CreateSnapshotResponse
        """
        return self.create_snapshot_with_http_info(request)

    def create_snapshot_with_http_info(self, request):
        """创建云硬盘快照

        创建云硬盘快照。

        :param CreateSnapshotRequest request
        :return: tuple(CreateSnapshotResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_snapshot_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudsnapshots', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSnapshotResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_volume(self, request):
        """创建云硬盘

        创建按需或包周期云硬盘。 在创建包周期云硬盘的场景下： - 如果您需要查看订单可用的优惠券，请参考\"[查询订单可用优惠券](https://support.huaweicloud.com/api-oce/zh-cn_topic_0092953630.html)\"。 - 如果您需要支付订单，请参考\"[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\"。 - 如果您需要查询订单的资源开通详情，请参考\"[查询订单的资源开通详情](https://support.huaweicloud.com/api-oce/api_order_00001.html)\"。 - 如果您需要退订该包周期资源，请参考“[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html)”。

        :param CreateVolumeRequest request
        :return: CreateVolumeResponse
        """
        return self.create_volume_with_http_info(request)

    def create_volume_with_http_info(self, request):
        """创建云硬盘

        创建按需或包周期云硬盘。 在创建包周期云硬盘的场景下： - 如果您需要查看订单可用的优惠券，请参考\"[查询订单可用优惠券](https://support.huaweicloud.com/api-oce/zh-cn_topic_0092953630.html)\"。 - 如果您需要支付订单，请参考\"[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\"。 - 如果您需要查询订单的资源开通详情，请参考\"[查询订单的资源开通详情](https://support.huaweicloud.com/api-oce/api_order_00001.html)\"。 - 如果您需要退订该包周期资源，请参考“[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html)”。

        :param CreateVolumeRequest request
        :return: tuple(CreateVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_volume_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json', 'application/json-1'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/cloudvolumes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_snapshot(self, request):
        """删除云硬盘快照

        删除云硬盘快照。

        :param DeleteSnapshotRequest request
        :return: None
        """
        return self.delete_snapshot_with_http_info(request)

    def delete_snapshot_with_http_info(self, request):
        """删除云硬盘快照

        删除云硬盘快照。

        :param DeleteSnapshotRequest request
        :return: None
        """

        all_params = ['snapshot_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudsnapshots/{snapshot_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_volume(self, request):
        """删除云硬盘

        删除一个云硬盘。

        :param DeleteVolumeRequest request
        :return: DeleteVolumeResponse
        """
        return self.delete_volume_with_http_info(request)

    def delete_volume_with_http_info(self, request):
        """删除云硬盘

        删除一个云硬盘。

        :param DeleteVolumeRequest request
        :return: tuple(DeleteVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['volume_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/{volume_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_snapshots_details(self, request):
        """查询云硬盘快照详细列表信息

        查询云硬盘快照详细列表信息。

        :param ListSnapshotsDetailsRequest request
        :return: ListSnapshotsDetailsResponse
        """
        return self.list_snapshots_details_with_http_info(request)

    def list_snapshots_details_with_http_info(self, request):
        """查询云硬盘快照详细列表信息

        查询云硬盘快照详细列表信息。

        :param ListSnapshotsDetailsRequest request
        :return: tuple(ListSnapshotsDetailsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['offset', 'limit', 'name', 'status', 'volume_id', 'availability_zone', 'id', 'dedicated_storage_name', 'dedicated_storage_id', 'service_type', 'enterprise_project_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'volume_id' in local_var_params:
            query_params.append(('volume_id', local_var_params['volume_id']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'dedicated_storage_name' in local_var_params:
            query_params.append(('dedicated_storage_name', local_var_params['dedicated_storage_name']))
        if 'dedicated_storage_id' in local_var_params:
            query_params.append(('dedicated_storage_id', local_var_params['dedicated_storage_id']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudsnapshots/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSnapshotsDetailsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_volume_tags(self, request):
        """获取云硬盘资源的所有标签

        获取某个租户的所有云硬盘资源的标签信息。

        :param ListVolumeTagsRequest request
        :return: ListVolumeTagsResponse
        """
        return self.list_volume_tags_with_http_info(request)

    def list_volume_tags_with_http_info(self, request):
        """获取云硬盘资源的所有标签

        获取某个租户的所有云硬盘资源的标签信息。

        :param ListVolumeTagsRequest request
        :return: tuple(ListVolumeTagsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVolumeTagsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_volumes_by_tags(self, request):
        """通过标签查询云硬盘资源实例详情

        通过标签查询云硬盘资源实例详情。

        :param ListVolumesByTagsRequest request
        :return: ListVolumesByTagsResponse
        """
        return self.list_volumes_by_tags_with_http_info(request)

    def list_volumes_by_tags_with_http_info(self, request):
        """通过标签查询云硬盘资源实例详情

        通过标签查询云硬盘资源实例详情。

        :param ListVolumesByTagsRequest request
        :return: tuple(ListVolumesByTagsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['list_volumes_by_tags_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/resource_instances/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVolumesByTagsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_volumes_details(self, request):
        """查询所有云硬盘详情

        查询所有云硬盘的详细信息。

        :param ListVolumesDetailsRequest request
        :return: ListVolumesDetailsResponse
        """
        return self.list_volumes_details_with_http_info(request)

    def list_volumes_details_with_http_info(self, request):
        """查询所有云硬盘详情

        查询所有云硬盘的详细信息。

        :param ListVolumesDetailsRequest request
        :return: tuple(ListVolumesDetailsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['marker', 'name', 'limit', 'sort_key', 'offset', 'sort_dir', 'status', 'metadata', 'availability_zone', 'multiattach', 'service_type', 'dedicated_storage_id', 'dedicated_storage_name', 'volume_type_id', 'id', 'ids', 'enterprise_project_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'metadata' in local_var_params:
            query_params.append(('metadata', local_var_params['metadata']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'multiattach' in local_var_params:
            query_params.append(('multiattach', local_var_params['multiattach']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'dedicated_storage_id' in local_var_params:
            query_params.append(('dedicated_storage_id', local_var_params['dedicated_storage_id']))
        if 'dedicated_storage_name' in local_var_params:
            query_params.append(('dedicated_storage_name', local_var_params['dedicated_storage_name']))
        if 'volume_type_id' in local_var_params:
            query_params.append(('volume_type_id', local_var_params['volume_type_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVolumesDetailsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def resize_volume(self, request):
        """扩容云硬盘

        对按需或者包周期云硬盘进行扩容。 在扩容包周期云硬盘的场景下： - 如果您需要查看订单可用的优惠券，请参考\"[查询订单可用优惠券](https://support.huaweicloud.com/api-oce/zh-cn_topic_0092953630.html)\"。 - 如果您需要支付订单，请参考\"[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\"。 - 如果您需要查询订单的资源开通详情，请参考\"[查询订单的资源开通详情](https://support.huaweicloud.com/api-oce/api_order_00001.html)\"。 - 如果您需要退订该包周期资源，请参考“[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html)”。

        :param ResizeVolumeRequest request
        :return: ResizeVolumeResponse
        """
        return self.resize_volume_with_http_info(request)

    def resize_volume_with_http_info(self, request):
        """扩容云硬盘

        对按需或者包周期云硬盘进行扩容。 在扩容包周期云硬盘的场景下： - 如果您需要查看订单可用的优惠券，请参考\"[查询订单可用优惠券](https://support.huaweicloud.com/api-oce/zh-cn_topic_0092953630.html)\"。 - 如果您需要支付订单，请参考\"[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\"。 - 如果您需要查询订单的资源开通详情，请参考\"[查询订单的资源开通详情](https://support.huaweicloud.com/api-oce/api_order_00001.html)\"。 - 如果您需要退订该包周期资源，请参考“[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html)”。

        :param ResizeVolumeRequest request
        :return: tuple(ResizeVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['volume_id', 'resize_volume_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json', 'application/json-1'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/cloudvolumes/{volume_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResizeVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def rollback_snapshot(self, request):
        """回滚快照到云硬盘

        将快照数据回滚到云硬盘。

        :param RollbackSnapshotRequest request
        :return: RollbackSnapshotResponse
        """
        return self.rollback_snapshot_with_http_info(request)

    def rollback_snapshot_with_http_info(self, request):
        """回滚快照到云硬盘

        将快照数据回滚到云硬盘。

        :param RollbackSnapshotRequest request
        :return: tuple(RollbackSnapshotResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['snapshot_id', 'rollback_snapshot_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudsnapshots/{snapshot_id}/rollback', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RollbackSnapshotResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_job(self, request):
        """查询job的状态

        查询Job的执行状态。 可用于查询创建云硬盘，扩容云硬盘，删除云硬盘等API的执行状态。

        :param ShowJobRequest request
        :return: ShowJobResponse
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        """查询job的状态

        查询Job的执行状态。 可用于查询创建云硬盘，扩容云硬盘，删除云硬盘等API的执行状态。

        :param ShowJobRequest request
        :return: tuple(ShowJobResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['job_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/jobs/{job_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_snapshot(self, request):
        """查询单个云硬盘快照详细信息

        查询单个云硬盘快照信息。

        :param ShowSnapshotRequest request
        :return: ShowSnapshotResponse
        """
        return self.show_snapshot_with_http_info(request)

    def show_snapshot_with_http_info(self, request):
        """查询单个云硬盘快照详细信息

        查询单个云硬盘快照信息。

        :param ShowSnapshotRequest request
        :return: tuple(ShowSnapshotResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['snapshot_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudsnapshots/{snapshot_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSnapshotResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_volume(self, request):
        """查询单个云硬盘详情

        查询单个云硬盘的详细信息。

        :param ShowVolumeRequest request
        :return: ShowVolumeResponse
        """
        return self.show_volume_with_http_info(request)

    def show_volume_with_http_info(self, request):
        """查询单个云硬盘详情

        查询单个云硬盘的详细信息。

        :param ShowVolumeRequest request
        :return: tuple(ShowVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['volume_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/{volume_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_volume_tags(self, request):
        """查询云硬盘标签

        查询指定云硬盘的标签信息。

        :param ShowVolumeTagsRequest request
        :return: ShowVolumeTagsResponse
        """
        return self.show_volume_tags_with_http_info(request)

    def show_volume_tags_with_http_info(self, request):
        """查询云硬盘标签

        查询指定云硬盘的标签信息。

        :param ShowVolumeTagsRequest request
        :return: tuple(ShowVolumeTagsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['volume_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/{volume_id}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVolumeTagsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_snapshot(self, request):
        """更新云硬盘快照

        更新云硬盘快照。

        :param UpdateSnapshotRequest request
        :return: UpdateSnapshotResponse
        """
        return self.update_snapshot_with_http_info(request)

    def update_snapshot_with_http_info(self, request):
        """更新云硬盘快照

        更新云硬盘快照。

        :param UpdateSnapshotRequest request
        :return: tuple(UpdateSnapshotResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['snapshot_id', 'update_snapshot_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudsnapshots/{snapshot_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSnapshotResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_volume(self, request):
        """更新云硬盘

        更新一个云硬盘的名称和描述。支持企业项目授权功能。

        :param UpdateVolumeRequest request
        :return: UpdateVolumeResponse
        """
        return self.update_volume_with_http_info(request)

    def update_volume_with_http_info(self, request):
        """更新云硬盘

        更新一个云硬盘的名称和描述。支持企业项目授权功能。

        :param UpdateVolumeRequest request
        :return: tuple(UpdateVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['volume_id', 'update_volume_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudvolumes/{volume_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None,
                 response_type=None, auth_settings=None,  collection_formats=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats)
