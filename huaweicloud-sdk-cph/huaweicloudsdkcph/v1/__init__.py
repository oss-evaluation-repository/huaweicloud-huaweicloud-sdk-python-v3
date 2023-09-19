# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkcph.v1.cph_client import CphClient
from huaweicloudsdkcph.v1.cph_async_client import CphAsyncClient

from huaweicloudsdkcph.v1.model.address import Address
from huaweicloudsdkcph.v1.model.bandwidth import Bandwidth
from huaweicloudsdkcph.v1.model.batch_create_tags_request import BatchCreateTagsRequest
from huaweicloudsdkcph.v1.model.batch_create_tags_request_body import BatchCreateTagsRequestBody
from huaweicloudsdkcph.v1.model.batch_create_tags_response import BatchCreateTagsResponse
from huaweicloudsdkcph.v1.model.batch_delete_tags_request import BatchDeleteTagsRequest
from huaweicloudsdkcph.v1.model.batch_delete_tags_request_body import BatchDeleteTagsRequestBody
from huaweicloudsdkcph.v1.model.batch_delete_tags_response import BatchDeleteTagsResponse
from huaweicloudsdkcph.v1.model.batch_export_cloud_phone_data_request import BatchExportCloudPhoneDataRequest
from huaweicloudsdkcph.v1.model.batch_export_cloud_phone_data_request_body import BatchExportCloudPhoneDataRequestBody
from huaweicloudsdkcph.v1.model.batch_export_cloud_phone_data_response import BatchExportCloudPhoneDataResponse
from huaweicloudsdkcph.v1.model.batch_import_cloud_phone_data_request import BatchImportCloudPhoneDataRequest
from huaweicloudsdkcph.v1.model.batch_import_cloud_phone_data_request_body import BatchImportCloudPhoneDataRequestBody
from huaweicloudsdkcph.v1.model.batch_import_cloud_phone_data_response import BatchImportCloudPhoneDataResponse
from huaweicloudsdkcph.v1.model.change_cloud_phone_server_model_request import ChangeCloudPhoneServerModelRequest
from huaweicloudsdkcph.v1.model.change_cloud_phone_server_model_request_body import ChangeCloudPhoneServerModelRequestBody
from huaweicloudsdkcph.v1.model.change_cloud_phone_server_model_request_body_extend_param import ChangeCloudPhoneServerModelRequestBodyExtendParam
from huaweicloudsdkcph.v1.model.change_cloud_phone_server_model_response import ChangeCloudPhoneServerModelResponse
from huaweicloudsdkcph.v1.model.create_net2_cloud_phone_server_request import CreateNet2CloudPhoneServerRequest
from huaweicloudsdkcph.v1.model.create_net2_cloud_phone_server_request_body import CreateNet2CloudPhoneServerRequestBody
from huaweicloudsdkcph.v1.model.create_net2_cloud_phone_server_request_body_band_width import CreateNet2CloudPhoneServerRequestBodyBandWidth
from huaweicloudsdkcph.v1.model.create_net2_cloud_phone_server_request_body_extend_param import CreateNet2CloudPhoneServerRequestBodyExtendParam
from huaweicloudsdkcph.v1.model.create_net2_cloud_phone_server_request_body_public_ip import CreateNet2CloudPhoneServerRequestBodyPublicIp
from huaweicloudsdkcph.v1.model.create_net2_cloud_phone_server_request_body_public_ip_eip import CreateNet2CloudPhoneServerRequestBodyPublicIpEip
from huaweicloudsdkcph.v1.model.create_net2_cloud_phone_server_response import CreateNet2CloudPhoneServerResponse
from huaweicloudsdkcph.v1.model.delete_share_apps_request import DeleteShareAppsRequest
from huaweicloudsdkcph.v1.model.delete_share_apps_request_body import DeleteShareAppsRequestBody
from huaweicloudsdkcph.v1.model.delete_share_apps_response import DeleteShareAppsResponse
from huaweicloudsdkcph.v1.model.delete_share_files_request import DeleteShareFilesRequest
from huaweicloudsdkcph.v1.model.delete_share_files_request_body import DeleteShareFilesRequestBody
from huaweicloudsdkcph.v1.model.delete_share_files_response import DeleteShareFilesResponse
from huaweicloudsdkcph.v1.model.encode_server import EncodeServer
from huaweicloudsdkcph.v1.model.encode_server_access_info import EncodeServerAccessInfo
from huaweicloudsdkcph.v1.model.encode_server_job import EncodeServerJob
from huaweicloudsdkcph.v1.model.import_traffic_request import ImportTrafficRequest
from huaweicloudsdkcph.v1.model.import_traffic_request_body import ImportTrafficRequestBody
from huaweicloudsdkcph.v1.model.import_traffic_response import ImportTrafficResponse
from huaweicloudsdkcph.v1.model.install_apk_request import InstallApkRequest
from huaweicloudsdkcph.v1.model.install_apk_request_body import InstallApkRequestBody
from huaweicloudsdkcph.v1.model.install_apk_response import InstallApkResponse
from huaweicloudsdkcph.v1.model.job import Job
from huaweicloudsdkcph.v1.model.list_cloud_phone_images_request import ListCloudPhoneImagesRequest
from huaweicloudsdkcph.v1.model.list_cloud_phone_images_response import ListCloudPhoneImagesResponse
from huaweicloudsdkcph.v1.model.list_cloud_phone_models_request import ListCloudPhoneModelsRequest
from huaweicloudsdkcph.v1.model.list_cloud_phone_models_response import ListCloudPhoneModelsResponse
from huaweicloudsdkcph.v1.model.list_cloud_phone_server_models_request import ListCloudPhoneServerModelsRequest
from huaweicloudsdkcph.v1.model.list_cloud_phone_server_models_response import ListCloudPhoneServerModelsResponse
from huaweicloudsdkcph.v1.model.list_cloud_phone_servers_request import ListCloudPhoneServersRequest
from huaweicloudsdkcph.v1.model.list_cloud_phone_servers_response import ListCloudPhoneServersResponse
from huaweicloudsdkcph.v1.model.list_cloud_phones_request import ListCloudPhonesRequest
from huaweicloudsdkcph.v1.model.list_cloud_phones_response import ListCloudPhonesResponse
from huaweicloudsdkcph.v1.model.list_encode_servers_request import ListEncodeServersRequest
from huaweicloudsdkcph.v1.model.list_encode_servers_response import ListEncodeServersResponse
from huaweicloudsdkcph.v1.model.list_jobs_request import ListJobsRequest
from huaweicloudsdkcph.v1.model.list_jobs_response import ListJobsResponse
from huaweicloudsdkcph.v1.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkcph.v1.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkcph.v1.model.list_resource_instances_request import ListResourceInstancesRequest
from huaweicloudsdkcph.v1.model.list_resource_instances_request_body import ListResourceInstancesRequestBody
from huaweicloudsdkcph.v1.model.list_resource_instances_response import ListResourceInstancesResponse
from huaweicloudsdkcph.v1.model.list_resource_tags_request import ListResourceTagsRequest
from huaweicloudsdkcph.v1.model.list_resource_tags_response import ListResourceTagsResponse
from huaweicloudsdkcph.v1.model.list_share_files_request import ListShareFilesRequest
from huaweicloudsdkcph.v1.model.list_share_files_response import ListShareFilesResponse
from huaweicloudsdkcph.v1.model.match import Match
from huaweicloudsdkcph.v1.model.model_property import ModelProperty
from huaweicloudsdkcph.v1.model.nic import Nic
from huaweicloudsdkcph.v1.model.nic_ipv6_bandwidth import NicIpv6Bandwidth
from huaweicloudsdkcph.v1.model.phone import Phone
from huaweicloudsdkcph.v1.model.phone_access_info import PhoneAccessInfo
from huaweicloudsdkcph.v1.model.phone_image import PhoneImage
from huaweicloudsdkcph.v1.model.phone_job import PhoneJob
from huaweicloudsdkcph.v1.model.phone_metadata import PhoneMetadata
from huaweicloudsdkcph.v1.model.phone_model import PhoneModel
from huaweicloudsdkcph.v1.model.phone_property import PhoneProperty
from huaweicloudsdkcph.v1.model.port import Port
from huaweicloudsdkcph.v1.model.push_file_request import PushFileRequest
from huaweicloudsdkcph.v1.model.push_file_request_body import PushFileRequestBody
from huaweicloudsdkcph.v1.model.push_file_response import PushFileResponse
from huaweicloudsdkcph.v1.model.push_share_apps_request import PushShareAppsRequest
from huaweicloudsdkcph.v1.model.push_share_apps_request_body import PushShareAppsRequestBody
from huaweicloudsdkcph.v1.model.push_share_apps_response import PushShareAppsResponse
from huaweicloudsdkcph.v1.model.push_share_files_request import PushShareFilesRequest
from huaweicloudsdkcph.v1.model.push_share_files_request_body import PushShareFilesRequestBody
from huaweicloudsdkcph.v1.model.push_share_files_response import PushShareFilesResponse
from huaweicloudsdkcph.v1.model.reset_cloud_phone_request import ResetCloudPhoneRequest
from huaweicloudsdkcph.v1.model.reset_cloud_phone_request_body import ResetCloudPhoneRequestBody
from huaweicloudsdkcph.v1.model.reset_cloud_phone_response import ResetCloudPhoneResponse
from huaweicloudsdkcph.v1.model.resource import Resource
from huaweicloudsdkcph.v1.model.restart_cloud_phone_request import RestartCloudPhoneRequest
from huaweicloudsdkcph.v1.model.restart_cloud_phone_request_body import RestartCloudPhoneRequestBody
from huaweicloudsdkcph.v1.model.restart_cloud_phone_response import RestartCloudPhoneResponse
from huaweicloudsdkcph.v1.model.restart_cloud_phone_server_request import RestartCloudPhoneServerRequest
from huaweicloudsdkcph.v1.model.restart_cloud_phone_server_request_body import RestartCloudPhoneServerRequestBody
from huaweicloudsdkcph.v1.model.restart_cloud_phone_server_response import RestartCloudPhoneServerResponse
from huaweicloudsdkcph.v1.model.restart_encode_server_request import RestartEncodeServerRequest
from huaweicloudsdkcph.v1.model.restart_encode_server_request_body import RestartEncodeServerRequestBody
from huaweicloudsdkcph.v1.model.restart_encode_server_response import RestartEncodeServerResponse
from huaweicloudsdkcph.v1.model.restore_info import RestoreInfo
from huaweicloudsdkcph.v1.model.run_shell_command_request import RunShellCommandRequest
from huaweicloudsdkcph.v1.model.run_shell_command_request_body import RunShellCommandRequestBody
from huaweicloudsdkcph.v1.model.run_shell_command_response import RunShellCommandResponse
from huaweicloudsdkcph.v1.model.run_sync_command_job import RunSyncCommandJob
from huaweicloudsdkcph.v1.model.run_sync_command_request import RunSyncCommandRequest
from huaweicloudsdkcph.v1.model.run_sync_command_request_body import RunSyncCommandRequestBody
from huaweicloudsdkcph.v1.model.run_sync_command_response import RunSyncCommandResponse
from huaweicloudsdkcph.v1.model.server import Server
from huaweicloudsdkcph.v1.model.server_job import ServerJob
from huaweicloudsdkcph.v1.model.server_keypair import ServerKeypair
from huaweicloudsdkcph.v1.model.server_metadata import ServerMetadata
from huaweicloudsdkcph.v1.model.server_model import ServerModel
from huaweicloudsdkcph.v1.model.server_model_extend_spec import ServerModelExtendSpec
from huaweicloudsdkcph.v1.model.show_bandwidth_detail_request import ShowBandwidthDetailRequest
from huaweicloudsdkcph.v1.model.show_bandwidth_detail_response import ShowBandwidthDetailResponse
from huaweicloudsdkcph.v1.model.show_cloud_phone_detail_request import ShowCloudPhoneDetailRequest
from huaweicloudsdkcph.v1.model.show_cloud_phone_detail_response import ShowCloudPhoneDetailResponse
from huaweicloudsdkcph.v1.model.show_cloud_phone_detail_response_body_metadata import ShowCloudPhoneDetailResponseBodyMetadata
from huaweicloudsdkcph.v1.model.show_cloud_phone_server_detail_request import ShowCloudPhoneServerDetailRequest
from huaweicloudsdkcph.v1.model.show_cloud_phone_server_detail_response import ShowCloudPhoneServerDetailResponse
from huaweicloudsdkcph.v1.model.show_cloud_phone_server_detail_response_body_metadata import ShowCloudPhoneServerDetailResponseBodyMetadata
from huaweicloudsdkcph.v1.model.show_job_request import ShowJobRequest
from huaweicloudsdkcph.v1.model.show_job_response import ShowJobResponse
from huaweicloudsdkcph.v1.model.stop_cloud_phone_request import StopCloudPhoneRequest
from huaweicloudsdkcph.v1.model.stop_cloud_phone_request_body import StopCloudPhoneRequestBody
from huaweicloudsdkcph.v1.model.stop_cloud_phone_response import StopCloudPhoneResponse
from huaweicloudsdkcph.v1.model.storage_info import StorageInfo
from huaweicloudsdkcph.v1.model.tag import Tag
from huaweicloudsdkcph.v1.model.tags import Tags
from huaweicloudsdkcph.v1.model.uninstall_apk_request import UninstallApkRequest
from huaweicloudsdkcph.v1.model.uninstall_apk_request_body import UninstallApkRequestBody
from huaweicloudsdkcph.v1.model.uninstall_apk_response import UninstallApkResponse
from huaweicloudsdkcph.v1.model.update_bandwidth_request import UpdateBandwidthRequest
from huaweicloudsdkcph.v1.model.update_bandwidth_request_body import UpdateBandwidthRequestBody
from huaweicloudsdkcph.v1.model.update_bandwidth_response import UpdateBandwidthResponse
from huaweicloudsdkcph.v1.model.update_cloud_phone_property_request import UpdateCloudPhonePropertyRequest
from huaweicloudsdkcph.v1.model.update_cloud_phone_property_request_body import UpdateCloudPhonePropertyRequestBody
from huaweicloudsdkcph.v1.model.update_cloud_phone_property_response import UpdateCloudPhonePropertyResponse
from huaweicloudsdkcph.v1.model.update_keypair_request import UpdateKeypairRequest
from huaweicloudsdkcph.v1.model.update_keypair_request_body import UpdateKeypairRequestBody
from huaweicloudsdkcph.v1.model.update_keypair_response import UpdateKeypairResponse
from huaweicloudsdkcph.v1.model.update_phone_name_request import UpdatePhoneNameRequest
from huaweicloudsdkcph.v1.model.update_phone_name_request_body import UpdatePhoneNameRequestBody
from huaweicloudsdkcph.v1.model.update_phone_name_response import UpdatePhoneNameResponse
from huaweicloudsdkcph.v1.model.update_server_name_request import UpdateServerNameRequest
from huaweicloudsdkcph.v1.model.update_server_name_request_body import UpdateServerNameRequestBody
from huaweicloudsdkcph.v1.model.update_server_name_response import UpdateServerNameResponse
from huaweicloudsdkcph.v1.model.volume import Volume

