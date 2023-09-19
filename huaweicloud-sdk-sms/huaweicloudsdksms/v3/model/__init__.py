# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdksms.v3.model.btrfs_file_system import BtrfsFileSystem
from huaweicloudsdksms.v3.model.btrfs_subvolumn import BtrfsSubvolumn
from huaweicloudsdksms.v3.model.check_net_acl_request import CheckNetAclRequest
from huaweicloudsdksms.v3.model.check_net_acl_response import CheckNetAclResponse
from huaweicloudsdksms.v3.model.clone_server import CloneServer
from huaweicloudsdksms.v3.model.clone_server_brief import CloneServerBrief
from huaweicloudsdksms.v3.model.collect_log_request import CollectLogRequest
from huaweicloudsdksms.v3.model.collect_log_response import CollectLogResponse
from huaweicloudsdksms.v3.model.comand_param import ComandParam
from huaweicloudsdksms.v3.model.command_body import CommandBody
from huaweicloudsdksms.v3.model.config_body import ConfigBody
from huaweicloudsdksms.v3.model.configuration_request_body import ConfigurationRequestBody
from huaweicloudsdksms.v3.model.create_migproject_request import CreateMigprojectRequest
from huaweicloudsdksms.v3.model.create_migproject_response import CreateMigprojectResponse
from huaweicloudsdksms.v3.model.create_privacy_agreements_request import CreatePrivacyAgreementsRequest
from huaweicloudsdksms.v3.model.create_privacy_agreements_response import CreatePrivacyAgreementsResponse
from huaweicloudsdksms.v3.model.create_task_request import CreateTaskRequest
from huaweicloudsdksms.v3.model.create_task_response import CreateTaskResponse
from huaweicloudsdksms.v3.model.create_template_req import CreateTemplateReq
from huaweicloudsdksms.v3.model.create_template_request import CreateTemplateRequest
from huaweicloudsdksms.v3.model.create_template_response import CreateTemplateResponse
from huaweicloudsdksms.v3.model.delete_ids import DeleteIds
from huaweicloudsdksms.v3.model.delete_migproject_request import DeleteMigprojectRequest
from huaweicloudsdksms.v3.model.delete_migproject_response import DeleteMigprojectResponse
from huaweicloudsdksms.v3.model.delete_server_request import DeleteServerRequest
from huaweicloudsdksms.v3.model.delete_server_response import DeleteServerResponse
from huaweicloudsdksms.v3.model.delete_servers_request import DeleteServersRequest
from huaweicloudsdksms.v3.model.delete_servers_response import DeleteServersResponse
from huaweicloudsdksms.v3.model.delete_task_request import DeleteTaskRequest
from huaweicloudsdksms.v3.model.delete_task_response import DeleteTaskResponse
from huaweicloudsdksms.v3.model.delete_tasks_req import DeleteTasksReq
from huaweicloudsdksms.v3.model.delete_tasks_request import DeleteTasksRequest
from huaweicloudsdksms.v3.model.delete_tasks_response import DeleteTasksResponse
from huaweicloudsdksms.v3.model.delete_template_request import DeleteTemplateRequest
from huaweicloudsdksms.v3.model.delete_template_response import DeleteTemplateResponse
from huaweicloudsdksms.v3.model.delete_templates_request import DeleteTemplatesRequest
from huaweicloudsdksms.v3.model.delete_templates_response import DeleteTemplatesResponse
from huaweicloudsdksms.v3.model.deletetemplates_req import DeletetemplatesReq
from huaweicloudsdksms.v3.model.disk import Disk
from huaweicloudsdksms.v3.model.disk_intarget_server import DiskIntargetServer
from huaweicloudsdksms.v3.model.environment_check import EnvironmentCheck
from huaweicloudsdksms.v3.model.init_target_server import InitTargetServer
from huaweicloudsdksms.v3.model.link import Link
from huaweicloudsdksms.v3.model.list_api_version_request import ListApiVersionRequest
from huaweicloudsdksms.v3.model.list_api_version_response import ListApiVersionResponse
from huaweicloudsdksms.v3.model.list_error_servers_request import ListErrorServersRequest
from huaweicloudsdksms.v3.model.list_error_servers_response import ListErrorServersResponse
from huaweicloudsdksms.v3.model.list_migprojects_request import ListMigprojectsRequest
from huaweicloudsdksms.v3.model.list_migprojects_response import ListMigprojectsResponse
from huaweicloudsdksms.v3.model.list_servers_request import ListServersRequest
from huaweicloudsdksms.v3.model.list_servers_response import ListServersResponse
from huaweicloudsdksms.v3.model.list_tasks_request import ListTasksRequest
from huaweicloudsdksms.v3.model.list_tasks_response import ListTasksResponse
from huaweicloudsdksms.v3.model.list_templates_request import ListTemplatesRequest
from huaweicloudsdksms.v3.model.list_templates_response import ListTemplatesResponse
from huaweicloudsdksms.v3.model.logical_volumes import LogicalVolumes
from huaweicloudsdksms.v3.model.mig_project import MigProject
from huaweicloudsdksms.v3.model.migprojects_response_body import MigprojectsResponseBody
from huaweicloudsdksms.v3.model.migration_errors import MigrationErrors
from huaweicloudsdksms.v3.model.net_work import NetWork
from huaweicloudsdksms.v3.model.network_check_info_request_body import NetworkCheckInfoRequestBody
from huaweicloudsdksms.v3.model.nics import Nics
from huaweicloudsdksms.v3.model.physical_volume import PhysicalVolume
from huaweicloudsdksms.v3.model.physical_volumes import PhysicalVolumes
from huaweicloudsdksms.v3.model.post_mig_project_body import PostMigProjectBody
from huaweicloudsdksms.v3.model.post_source_server_body import PostSourceServerBody
from huaweicloudsdksms.v3.model.post_task import PostTask
from huaweicloudsdksms.v3.model.public_ip import PublicIp
from huaweicloudsdksms.v3.model.put_copy_state_req import PutCopyStateReq
from huaweicloudsdksms.v3.model.put_disk import PutDisk
from huaweicloudsdksms.v3.model.put_disk_info_req import PutDiskInfoReq
from huaweicloudsdksms.v3.model.put_logical_volume import PutLogicalVolume
from huaweicloudsdksms.v3.model.put_source_server_body import PutSourceServerBody
from huaweicloudsdksms.v3.model.put_task_req import PutTaskReq
from huaweicloudsdksms.v3.model.put_volume import PutVolume
from huaweicloudsdksms.v3.model.put_volume_groups import PutVolumeGroups
from huaweicloudsdksms.v3.model.register_server_request import RegisterServerRequest
from huaweicloudsdksms.v3.model.register_server_response import RegisterServerResponse
from huaweicloudsdksms.v3.model.server import Server
from huaweicloudsdksms.v3.model.server_disk import ServerDisk
from huaweicloudsdksms.v3.model.sg_object import SgObject
from huaweicloudsdksms.v3.model.show_api_version_request import ShowApiVersionRequest
from huaweicloudsdksms.v3.model.show_api_version_response import ShowApiVersionResponse
from huaweicloudsdksms.v3.model.show_cert_key_request import ShowCertKeyRequest
from huaweicloudsdksms.v3.model.show_cert_key_response import ShowCertKeyResponse
from huaweicloudsdksms.v3.model.show_command_request import ShowCommandRequest
from huaweicloudsdksms.v3.model.show_command_response import ShowCommandResponse
from huaweicloudsdksms.v3.model.show_config_request import ShowConfigRequest
from huaweicloudsdksms.v3.model.show_config_response import ShowConfigResponse
from huaweicloudsdksms.v3.model.show_config_setting_request import ShowConfigSettingRequest
from huaweicloudsdksms.v3.model.show_config_setting_response import ShowConfigSettingResponse
from huaweicloudsdksms.v3.model.show_migproject_request import ShowMigprojectRequest
from huaweicloudsdksms.v3.model.show_migproject_response import ShowMigprojectResponse
from huaweicloudsdksms.v3.model.show_overview_request import ShowOverviewRequest
from huaweicloudsdksms.v3.model.show_overview_response import ShowOverviewResponse
from huaweicloudsdksms.v3.model.show_passphrase_request import ShowPassphraseRequest
from huaweicloudsdksms.v3.model.show_passphrase_response import ShowPassphraseResponse
from huaweicloudsdksms.v3.model.show_privacy_agreements_request import ShowPrivacyAgreementsRequest
from huaweicloudsdksms.v3.model.show_privacy_agreements_response import ShowPrivacyAgreementsResponse
from huaweicloudsdksms.v3.model.show_server_request import ShowServerRequest
from huaweicloudsdksms.v3.model.show_server_response import ShowServerResponse
from huaweicloudsdksms.v3.model.show_sha256_request import ShowSha256Request
from huaweicloudsdksms.v3.model.show_sha256_response import ShowSha256Response
from huaweicloudsdksms.v3.model.show_target_password_request import ShowTargetPasswordRequest
from huaweicloudsdksms.v3.model.show_target_password_response import ShowTargetPasswordResponse
from huaweicloudsdksms.v3.model.show_task_request import ShowTaskRequest
from huaweicloudsdksms.v3.model.show_task_response import ShowTaskResponse
from huaweicloudsdksms.v3.model.show_template_request import ShowTemplateRequest
from huaweicloudsdksms.v3.model.show_template_response import ShowTemplateResponse
from huaweicloudsdksms.v3.model.shows_speed_limits_request import ShowsSpeedLimitsRequest
from huaweicloudsdksms.v3.model.shows_speed_limits_response import ShowsSpeedLimitsResponse
from huaweicloudsdksms.v3.model.source_server_associated_with_task import SourceServerAssociatedWithTask
from huaweicloudsdksms.v3.model.source_server_by_task import SourceServerByTask
from huaweicloudsdksms.v3.model.source_server_response import SourceServerResponse
from huaweicloudsdksms.v3.model.source_servers_response_body import SourceServersResponseBody
from huaweicloudsdksms.v3.model.speed_limit import SpeedLimit
from huaweicloudsdksms.v3.model.speed_limitl_json import SpeedLimitlJson
from huaweicloudsdksms.v3.model.sub_task import SubTask
from huaweicloudsdksms.v3.model.sub_task_associated_with_task import SubTaskAssociatedWithTask
from huaweicloudsdksms.v3.model.target_disk import TargetDisk
from huaweicloudsdksms.v3.model.target_disks import TargetDisks
from huaweicloudsdksms.v3.model.target_physical_volumes import TargetPhysicalVolumes
from huaweicloudsdksms.v3.model.target_server import TargetServer
from huaweicloudsdksms.v3.model.target_server_associated_with_task import TargetServerAssociatedWithTask
from huaweicloudsdksms.v3.model.target_server_by_id import TargetServerById
from huaweicloudsdksms.v3.model.target_server_by_task import TargetServerByTask
from huaweicloudsdksms.v3.model.task_by_server_source import TaskByServerSource
from huaweicloudsdksms.v3.model.task_by_server_sources import TaskByServerSources
from huaweicloudsdksms.v3.model.task_target_server import TaskTargetServer
from huaweicloudsdksms.v3.model.tasks_response_body import TasksResponseBody
from huaweicloudsdksms.v3.model.template_disk import TemplateDisk
from huaweicloudsdksms.v3.model.template_request import TemplateRequest
from huaweicloudsdksms.v3.model.template_response_body import TemplateResponseBody
from huaweicloudsdksms.v3.model.unlock_target_ecs_request import UnlockTargetEcsRequest
from huaweicloudsdksms.v3.model.unlock_target_ecs_response import UnlockTargetEcsResponse
from huaweicloudsdksms.v3.model.update_command_result_request import UpdateCommandResultRequest
from huaweicloudsdksms.v3.model.update_command_result_response import UpdateCommandResultResponse
from huaweicloudsdksms.v3.model.update_copy_state_request import UpdateCopyStateRequest
from huaweicloudsdksms.v3.model.update_copy_state_response import UpdateCopyStateResponse
from huaweicloudsdksms.v3.model.update_default_migproject_request import UpdateDefaultMigprojectRequest
from huaweicloudsdksms.v3.model.update_default_migproject_response import UpdateDefaultMigprojectResponse
from huaweicloudsdksms.v3.model.update_disk_info_request import UpdateDiskInfoRequest
from huaweicloudsdksms.v3.model.update_disk_info_response import UpdateDiskInfoResponse
from huaweicloudsdksms.v3.model.update_migproject_request import UpdateMigprojectRequest
from huaweicloudsdksms.v3.model.update_migproject_response import UpdateMigprojectResponse
from huaweicloudsdksms.v3.model.update_network_check_info_request import UpdateNetworkCheckInfoRequest
from huaweicloudsdksms.v3.model.update_network_check_info_response import UpdateNetworkCheckInfoResponse
from huaweicloudsdksms.v3.model.update_server_name_request import UpdateServerNameRequest
from huaweicloudsdksms.v3.model.update_server_name_response import UpdateServerNameResponse
from huaweicloudsdksms.v3.model.update_speed_request import UpdateSpeedRequest
from huaweicloudsdksms.v3.model.update_speed_response import UpdateSpeedResponse
from huaweicloudsdksms.v3.model.update_task_request import UpdateTaskRequest
from huaweicloudsdksms.v3.model.update_task_response import UpdateTaskResponse
from huaweicloudsdksms.v3.model.update_task_speed_req import UpdateTaskSpeedReq
from huaweicloudsdksms.v3.model.update_task_speed_request import UpdateTaskSpeedRequest
from huaweicloudsdksms.v3.model.update_task_speed_response import UpdateTaskSpeedResponse
from huaweicloudsdksms.v3.model.update_task_status_req import UpdateTaskStatusReq
from huaweicloudsdksms.v3.model.update_task_status_request import UpdateTaskStatusRequest
from huaweicloudsdksms.v3.model.update_task_status_response import UpdateTaskStatusResponse
from huaweicloudsdksms.v3.model.update_template_req import UpdateTemplateReq
from huaweicloudsdksms.v3.model.update_template_request import UpdateTemplateRequest
from huaweicloudsdksms.v3.model.update_template_response import UpdateTemplateResponse
from huaweicloudsdksms.v3.model.upload_log_request_body import UploadLogRequestBody
from huaweicloudsdksms.v3.model.upload_special_configuration_setting_request import UploadSpecialConfigurationSettingRequest
from huaweicloudsdksms.v3.model.upload_special_configuration_setting_response import UploadSpecialConfigurationSettingResponse
from huaweicloudsdksms.v3.model.version import Version
from huaweicloudsdksms.v3.model.volume_groups import VolumeGroups
from huaweicloudsdksms.v3.model.vpc_object import VpcObject
