# coding: utf-8

from __future__ import absolute_import

# import WorkspaceClient
from huaweicloudsdkworkspace.v2.workspace_client import WorkspaceClient
from huaweicloudsdkworkspace.v2.workspace_async_client import WorkspaceAsyncClient
# import models into sdk package
from huaweicloudsdkworkspace.v2.model.ad_domain import AdDomain
from huaweicloudsdkworkspace.v2.model.ad_domain_info import AdDomainInfo
from huaweicloudsdkworkspace.v2.model.ad_info import AdInfo
from huaweicloudsdkworkspace.v2.model.add_desktop_volumes_req import AddDesktopVolumesReq
from huaweicloudsdkworkspace.v2.model.add_desktops_volumes_req import AddDesktopsVolumesReq
from huaweicloudsdkworkspace.v2.model.add_volumes_request import AddVolumesRequest
from huaweicloudsdkworkspace.v2.model.add_volumes_response import AddVolumesResponse
from huaweicloudsdkworkspace.v2.model.address_info import AddressInfo
from huaweicloudsdkworkspace.v2.model.apply_workspace_req import ApplyWorkspaceReq
from huaweicloudsdkworkspace.v2.model.apply_workspace_request import ApplyWorkspaceRequest
from huaweicloudsdkworkspace.v2.model.apply_workspace_response import ApplyWorkspaceResponse
from huaweicloudsdkworkspace.v2.model.availability_zone import AvailabilityZone
from huaweicloudsdkworkspace.v2.model.batch_action_desktops_req import BatchActionDesktopsReq
from huaweicloudsdkworkspace.v2.model.batch_delete_desktops_request import BatchDeleteDesktopsRequest
from huaweicloudsdkworkspace.v2.model.batch_delete_desktops_response import BatchDeleteDesktopsResponse
from huaweicloudsdkworkspace.v2.model.batch_run_desktops_request import BatchRunDesktopsRequest
from huaweicloudsdkworkspace.v2.model.batch_run_desktops_response import BatchRunDesktopsResponse
from huaweicloudsdkworkspace.v2.model.cancel_workspace_request import CancelWorkspaceRequest
from huaweicloudsdkworkspace.v2.model.cancel_workspace_response import CancelWorkspaceResponse
from huaweicloudsdkworkspace.v2.model.create_desktop_req import CreateDesktopReq
from huaweicloudsdkworkspace.v2.model.create_desktop_request import CreateDesktopRequest
from huaweicloudsdkworkspace.v2.model.create_desktop_response import CreateDesktopResponse
from huaweicloudsdkworkspace.v2.model.create_desktop_user_request import CreateDesktopUserRequest
from huaweicloudsdkworkspace.v2.model.create_desktop_user_response import CreateDesktopUserResponse
from huaweicloudsdkworkspace.v2.model.create_user_req import CreateUserReq
from huaweicloudsdkworkspace.v2.model.delete_desktop_request import DeleteDesktopRequest
from huaweicloudsdkworkspace.v2.model.delete_desktop_response import DeleteDesktopResponse
from huaweicloudsdkworkspace.v2.model.delete_desktops_req import DeleteDesktopsReq
from huaweicloudsdkworkspace.v2.model.delete_user_request import DeleteUserRequest
from huaweicloudsdkworkspace.v2.model.delete_user_response import DeleteUserResponse
from huaweicloudsdkworkspace.v2.model.desktop import Desktop
from huaweicloudsdkworkspace.v2.model.desktop_detail_info import DesktopDetailInfo
from huaweicloudsdkworkspace.v2.model.edit_user_req import EditUserReq
from huaweicloudsdkworkspace.v2.model.expand_desktops_volumes_req import ExpandDesktopsVolumesReq
from huaweicloudsdkworkspace.v2.model.expand_volumes_req import ExpandVolumesReq
from huaweicloudsdkworkspace.v2.model.expand_volumes_request import ExpandVolumesRequest
from huaweicloudsdkworkspace.v2.model.expand_volumes_response import ExpandVolumesResponse
from huaweicloudsdkworkspace.v2.model.export_user_login_info_new_request import ExportUserLoginInfoNewRequest
from huaweicloudsdkworkspace.v2.model.export_user_login_info_new_response import ExportUserLoginInfoNewResponse
from huaweicloudsdkworkspace.v2.model.flavor_info import FlavorInfo
from huaweicloudsdkworkspace.v2.model.flavor_link_info import FlavorLinkInfo
from huaweicloudsdkworkspace.v2.model.image_info import ImageInfo
from huaweicloudsdkworkspace.v2.model.job_detail_info import JobDetailInfo
from huaweicloudsdkworkspace.v2.model.job_entities import JobEntities
from huaweicloudsdkworkspace.v2.model.list_availability_zones_request import ListAvailabilityZonesRequest
from huaweicloudsdkworkspace.v2.model.list_availability_zones_response import ListAvailabilityZonesResponse
from huaweicloudsdkworkspace.v2.model.list_desktops_detail_request import ListDesktopsDetailRequest
from huaweicloudsdkworkspace.v2.model.list_desktops_detail_response import ListDesktopsDetailResponse
from huaweicloudsdkworkspace.v2.model.list_desktops_request import ListDesktopsRequest
from huaweicloudsdkworkspace.v2.model.list_desktops_response import ListDesktopsResponse
from huaweicloudsdkworkspace.v2.model.list_history_online_info_new_request import ListHistoryOnlineInfoNewRequest
from huaweicloudsdkworkspace.v2.model.list_history_online_info_new_response import ListHistoryOnlineInfoNewResponse
from huaweicloudsdkworkspace.v2.model.list_images_request import ListImagesRequest
from huaweicloudsdkworkspace.v2.model.list_images_response import ListImagesResponse
from huaweicloudsdkworkspace.v2.model.list_ita_sub_jobs_request import ListItaSubJobsRequest
from huaweicloudsdkworkspace.v2.model.list_ita_sub_jobs_response import ListItaSubJobsResponse
from huaweicloudsdkworkspace.v2.model.list_login_records_new_request import ListLoginRecordsNewRequest
from huaweicloudsdkworkspace.v2.model.list_login_records_new_response import ListLoginRecordsNewResponse
from huaweicloudsdkworkspace.v2.model.list_products_request import ListProductsRequest
from huaweicloudsdkworkspace.v2.model.list_products_response import ListProductsResponse
from huaweicloudsdkworkspace.v2.model.list_user_detail_request import ListUserDetailRequest
from huaweicloudsdkworkspace.v2.model.list_user_detail_response import ListUserDetailResponse
from huaweicloudsdkworkspace.v2.model.list_users_request import ListUsersRequest
from huaweicloudsdkworkspace.v2.model.list_users_response import ListUsersResponse
from huaweicloudsdkworkspace.v2.model.list_workspaces_request import ListWorkspacesRequest
from huaweicloudsdkworkspace.v2.model.list_workspaces_response import ListWorkspacesResponse
from huaweicloudsdkworkspace.v2.model.modify_workspace_attributes_req import ModifyWorkspaceAttributesReq
from huaweicloudsdkworkspace.v2.model.nic import Nic
from huaweicloudsdkworkspace.v2.model.product_detail_info import ProductDetailInfo
from huaweicloudsdkworkspace.v2.model.product_info import ProductInfo
from huaweicloudsdkworkspace.v2.model.record import Record
from huaweicloudsdkworkspace.v2.model.resize_desktop_data import ResizeDesktopData
from huaweicloudsdkworkspace.v2.model.resize_desktop_job_result import ResizeDesktopJobResult
from huaweicloudsdkworkspace.v2.model.resize_desktop_req import ResizeDesktopReq
from huaweicloudsdkworkspace.v2.model.resize_desktop_request import ResizeDesktopRequest
from huaweicloudsdkworkspace.v2.model.resize_desktop_response import ResizeDesktopResponse
from huaweicloudsdkworkspace.v2.model.security_group import SecurityGroup
from huaweicloudsdkworkspace.v2.model.security_group_info import SecurityGroupInfo
from huaweicloudsdkworkspace.v2.model.show_desktop_detail_request import ShowDesktopDetailRequest
from huaweicloudsdkworkspace.v2.model.show_desktop_detail_response import ShowDesktopDetailResponse
from huaweicloudsdkworkspace.v2.model.simple_desktop_info import SimpleDesktopInfo
from huaweicloudsdkworkspace.v2.model.simple_product import SimpleProduct
from huaweicloudsdkworkspace.v2.model.sold_out_info import SoldOutInfo
from huaweicloudsdkworkspace.v2.model.subnet import Subnet
from huaweicloudsdkworkspace.v2.model.subnet_info import SubnetInfo
from huaweicloudsdkworkspace.v2.model.tag import Tag
from huaweicloudsdkworkspace.v2.model.tls_config import TlsConfig
from huaweicloudsdkworkspace.v2.model.update_user_info_request import UpdateUserInfoRequest
from huaweicloudsdkworkspace.v2.model.update_user_info_response import UpdateUserInfoResponse
from huaweicloudsdkworkspace.v2.model.update_workspace_request import UpdateWorkspaceRequest
from huaweicloudsdkworkspace.v2.model.update_workspace_response import UpdateWorkspaceResponse
from huaweicloudsdkworkspace.v2.model.user import User
from huaweicloudsdkworkspace.v2.model.user_detail import UserDetail
from huaweicloudsdkworkspace.v2.model.vm_operate_result import VmOperateResult
from huaweicloudsdkworkspace.v2.model.volume import Volume
from huaweicloudsdkworkspace.v2.model.volume_detail import VolumeDetail

