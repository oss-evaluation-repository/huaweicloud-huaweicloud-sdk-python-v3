# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkdcs.v2.model.acl_account_modify_password_body import AclAccountModifyPasswordBody
from huaweicloudsdkdcs.v2.model.acl_account_reset_password_body import AclAccountResetPasswordBody
from huaweicloudsdkdcs.v2.model.acl_account_resp import AclAccountResp
from huaweicloudsdkdcs.v2.model.acl_account_role_modify_body import AclAccountRoleModifyBody
from huaweicloudsdkdcs.v2.model.attrs_object import AttrsObject
from huaweicloudsdkdcs.v2.model.autoscan_config_request import AutoscanConfigRequest
from huaweicloudsdkdcs.v2.model.available_zones import AvailableZones
from huaweicloudsdkdcs.v2.model.backup_files_body import BackupFilesBody
from huaweicloudsdkdcs.v2.model.backup_instance_body import BackupInstanceBody
from huaweicloudsdkdcs.v2.model.backup_plan import BackupPlan
from huaweicloudsdkdcs.v2.model.backup_policy import BackupPolicy
from huaweicloudsdkdcs.v2.model.backup_record_response import BackupRecordResponse
from huaweicloudsdkdcs.v2.model.bandwidth_info import BandwidthInfo
from huaweicloudsdkdcs.v2.model.batch_create_or_delete_tags_request import BatchCreateOrDeleteTagsRequest
from huaweicloudsdkdcs.v2.model.batch_create_or_delete_tags_response import BatchCreateOrDeleteTagsResponse
from huaweicloudsdkdcs.v2.model.batch_delete_body import BatchDeleteBody
from huaweicloudsdkdcs.v2.model.batch_delete_instances_request import BatchDeleteInstancesRequest
from huaweicloudsdkdcs.v2.model.batch_delete_instances_response import BatchDeleteInstancesResponse
from huaweicloudsdkdcs.v2.model.batch_ops_result import BatchOpsResult
from huaweicloudsdkdcs.v2.model.batch_show_nodes_information_request import BatchShowNodesInformationRequest
from huaweicloudsdkdcs.v2.model.batch_show_nodes_information_response import BatchShowNodesInformationResponse
from huaweicloudsdkdcs.v2.model.batch_stop_migration_tasks_body import BatchStopMigrationTasksBody
from huaweicloudsdkdcs.v2.model.batch_stop_migration_tasks_request import BatchStopMigrationTasksRequest
from huaweicloudsdkdcs.v2.model.batch_stop_migration_tasks_response import BatchStopMigrationTasksResponse
from huaweicloudsdkdcs.v2.model.bigkeys_body import BigkeysBody
from huaweicloudsdkdcs.v2.model.bss_param import BssParam
from huaweicloudsdkdcs.v2.model.bss_param_entity import BssParamEntity
from huaweicloudsdkdcs.v2.model.change_instance_status_body import ChangeInstanceStatusBody
from huaweicloudsdkdcs.v2.model.change_master_standby_async_request import ChangeMasterStandbyAsyncRequest
from huaweicloudsdkdcs.v2.model.change_master_standby_async_response import ChangeMasterStandbyAsyncResponse
from huaweicloudsdkdcs.v2.model.change_master_standby_request import ChangeMasterStandbyRequest
from huaweicloudsdkdcs.v2.model.change_master_standby_response import ChangeMasterStandbyResponse
from huaweicloudsdkdcs.v2.model.cluster_redis_node_monitored_object import ClusterRedisNodeMonitoredObject
from huaweicloudsdkdcs.v2.model.command_time_taken import CommandTimeTaken
from huaweicloudsdkdcs.v2.model.command_time_taken_list import CommandTimeTakenList
from huaweicloudsdkdcs.v2.model.conclusion_item import ConclusionItem
from huaweicloudsdkdcs.v2.model.config_migration_instance_body import ConfigMigrationInstanceBody
from huaweicloudsdkdcs.v2.model.config_templates_list_info import ConfigTemplatesListInfo
from huaweicloudsdkdcs.v2.model.copy_instance_request import CopyInstanceRequest
from huaweicloudsdkdcs.v2.model.copy_instance_response import CopyInstanceResponse
from huaweicloudsdkdcs.v2.model.create_acl_account_request import CreateAclAccountRequest
from huaweicloudsdkdcs.v2.model.create_acl_account_request_body import CreateAclAccountRequestBody
from huaweicloudsdkdcs.v2.model.create_acl_account_response import CreateAclAccountResponse
from huaweicloudsdkdcs.v2.model.create_auto_expire_scan_task_request import CreateAutoExpireScanTaskRequest
from huaweicloudsdkdcs.v2.model.create_auto_expire_scan_task_response import CreateAutoExpireScanTaskResponse
from huaweicloudsdkdcs.v2.model.create_bigkey_scan_task_request import CreateBigkeyScanTaskRequest
from huaweicloudsdkdcs.v2.model.create_bigkey_scan_task_response import CreateBigkeyScanTaskResponse
from huaweicloudsdkdcs.v2.model.create_custom_template_body import CreateCustomTemplateBody
from huaweicloudsdkdcs.v2.model.create_custom_template_request import CreateCustomTemplateRequest
from huaweicloudsdkdcs.v2.model.create_custom_template_response import CreateCustomTemplateResponse
from huaweicloudsdkdcs.v2.model.create_diagnosis_task_body import CreateDiagnosisTaskBody
from huaweicloudsdkdcs.v2.model.create_diagnosis_task_request import CreateDiagnosisTaskRequest
from huaweicloudsdkdcs.v2.model.create_diagnosis_task_response import CreateDiagnosisTaskResponse
from huaweicloudsdkdcs.v2.model.create_hotkey_scan_task_request import CreateHotkeyScanTaskRequest
from huaweicloudsdkdcs.v2.model.create_hotkey_scan_task_response import CreateHotkeyScanTaskResponse
from huaweicloudsdkdcs.v2.model.create_instance_body import CreateInstanceBody
from huaweicloudsdkdcs.v2.model.create_instance_request import CreateInstanceRequest
from huaweicloudsdkdcs.v2.model.create_instance_response import CreateInstanceResponse
from huaweicloudsdkdcs.v2.model.create_migration_task_body import CreateMigrationTaskBody
from huaweicloudsdkdcs.v2.model.create_migration_task_request import CreateMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.create_migration_task_response import CreateMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.create_online_migration_task_body import CreateOnlineMigrationTaskBody
from huaweicloudsdkdcs.v2.model.create_online_migration_task_request import CreateOnlineMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.create_online_migration_task_response import CreateOnlineMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.create_or_delete_instance_tags import CreateOrDeleteInstanceTags
from huaweicloudsdkdcs.v2.model.create_redislog_download_link_request import CreateRedislogDownloadLinkRequest
from huaweicloudsdkdcs.v2.model.create_redislog_download_link_response import CreateRedislogDownloadLinkResponse
from huaweicloudsdkdcs.v2.model.create_redislog_request import CreateRedislogRequest
from huaweicloudsdkdcs.v2.model.create_redislog_response import CreateRedislogResponse
from huaweicloudsdkdcs.v2.model.create_resize_order_request import CreateResizeOrderRequest
from huaweicloudsdkdcs.v2.model.create_resize_order_request_body import CreateResizeOrderRequestBody
from huaweicloudsdkdcs.v2.model.create_resize_order_response import CreateResizeOrderResponse
from huaweicloudsdkdcs.v2.model.delete_acl_account_request import DeleteAclAccountRequest
from huaweicloudsdkdcs.v2.model.delete_acl_account_response import DeleteAclAccountResponse
from huaweicloudsdkdcs.v2.model.delete_background_task_request import DeleteBackgroundTaskRequest
from huaweicloudsdkdcs.v2.model.delete_background_task_response import DeleteBackgroundTaskResponse
from huaweicloudsdkdcs.v2.model.delete_backup_file_request import DeleteBackupFileRequest
from huaweicloudsdkdcs.v2.model.delete_backup_file_response import DeleteBackupFileResponse
from huaweicloudsdkdcs.v2.model.delete_bigkey_scan_task_request import DeleteBigkeyScanTaskRequest
from huaweicloudsdkdcs.v2.model.delete_bigkey_scan_task_response import DeleteBigkeyScanTaskResponse
from huaweicloudsdkdcs.v2.model.delete_center_task_request import DeleteCenterTaskRequest
from huaweicloudsdkdcs.v2.model.delete_center_task_request_body import DeleteCenterTaskRequestBody
from huaweicloudsdkdcs.v2.model.delete_center_task_response import DeleteCenterTaskResponse
from huaweicloudsdkdcs.v2.model.delete_config_template_request import DeleteConfigTemplateRequest
from huaweicloudsdkdcs.v2.model.delete_config_template_response import DeleteConfigTemplateResponse
from huaweicloudsdkdcs.v2.model.delete_diagnosis_report_request import DeleteDiagnosisReportRequest
from huaweicloudsdkdcs.v2.model.delete_diagnosis_task_request import DeleteDiagnosisTaskRequest
from huaweicloudsdkdcs.v2.model.delete_diagnosis_task_response import DeleteDiagnosisTaskResponse
from huaweicloudsdkdcs.v2.model.delete_hotkey_scan_task_request import DeleteHotkeyScanTaskRequest
from huaweicloudsdkdcs.v2.model.delete_hotkey_scan_task_response import DeleteHotkeyScanTaskResponse
from huaweicloudsdkdcs.v2.model.delete_ip_from_domain_name_request import DeleteIpFromDomainNameRequest
from huaweicloudsdkdcs.v2.model.delete_ip_from_domain_name_response import DeleteIpFromDomainNameResponse
from huaweicloudsdkdcs.v2.model.delete_migrate_task_request import DeleteMigrateTaskRequest
from huaweicloudsdkdcs.v2.model.delete_migration_task_request import DeleteMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.delete_migration_task_response import DeleteMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.delete_single_instance_request import DeleteSingleInstanceRequest
from huaweicloudsdkdcs.v2.model.delete_single_instance_response import DeleteSingleInstanceResponse
from huaweicloudsdkdcs.v2.model.details_body import DetailsBody
from huaweicloudsdkdcs.v2.model.diagnosis_dimension import DiagnosisDimension
from huaweicloudsdkdcs.v2.model.diagnosis_item import DiagnosisItem
from huaweicloudsdkdcs.v2.model.diagnosis_node_report import DiagnosisNodeReport
from huaweicloudsdkdcs.v2.model.diagnosis_report_info import DiagnosisReportInfo
from huaweicloudsdkdcs.v2.model.dim_child import DimChild
from huaweicloudsdkdcs.v2.model.domain_name_entity import DomainNameEntity
from huaweicloudsdkdcs.v2.model.domain_name_info import DomainNameInfo
from huaweicloudsdkdcs.v2.model.download_backup_files_req import DownloadBackupFilesReq
from huaweicloudsdkdcs.v2.model.download_ssl_cert_request import DownloadSslCertRequest
from huaweicloudsdkdcs.v2.model.download_ssl_cert_response import DownloadSslCertResponse
from huaweicloudsdkdcs.v2.model.exchange_instance_ip_request import ExchangeInstanceIpRequest
from huaweicloudsdkdcs.v2.model.exchange_instance_ip_response import ExchangeInstanceIpResponse
from huaweicloudsdkdcs.v2.model.execute_cluster_switchover_request import ExecuteClusterSwitchoverRequest
from huaweicloudsdkdcs.v2.model.execute_cluster_switchover_response import ExecuteClusterSwitchoverResponse
from huaweicloudsdkdcs.v2.model.execute_command_mobilization_request import ExecuteCommandMobilizationRequest
from huaweicloudsdkdcs.v2.model.execute_command_mobilization_response import ExecuteCommandMobilizationResponse
from huaweicloudsdkdcs.v2.model.execute_command_request_body import ExecuteCommandRequestBody
from huaweicloudsdkdcs.v2.model.export_excel_job_request import ExportExcelJobRequest
from huaweicloudsdkdcs.v2.model.export_excel_job_response import ExportExcelJobResponse
from huaweicloudsdkdcs.v2.model.export_instances_task_body import ExportInstancesTaskBody
from huaweicloudsdkdcs.v2.model.export_instances_task_request import ExportInstancesTaskRequest
from huaweicloudsdkdcs.v2.model.export_instances_task_response import ExportInstancesTaskResponse
from huaweicloudsdkdcs.v2.model.features import Features
from huaweicloudsdkdcs.v2.model.files import Files
from huaweicloudsdkdcs.v2.model.flavor_az_object import FlavorAzObject
from huaweicloudsdkdcs.v2.model.flavors_items import FlavorsItems
from huaweicloudsdkdcs.v2.model.history_info import HistoryInfo
from huaweicloudsdkdcs.v2.model.hotkeys_body import HotkeysBody
from huaweicloudsdkdcs.v2.model.instance_backup_policy import InstanceBackupPolicy
from huaweicloudsdkdcs.v2.model.instance_group_list_info import InstanceGroupListInfo
from huaweicloudsdkdcs.v2.model.instance_list_info import InstanceListInfo
from huaweicloudsdkdcs.v2.model.instance_nodes_info_resp import InstanceNodesInfoResp
from huaweicloudsdkdcs.v2.model.instance_replication_dimensions_info import InstanceReplicationDimensionsInfo
from huaweicloudsdkdcs.v2.model.instance_replication_list_info import InstanceReplicationListInfo
from huaweicloudsdkdcs.v2.model.instance_restore_info import InstanceRestoreInfo
from huaweicloudsdkdcs.v2.model.instance_statistic import InstanceStatistic
from huaweicloudsdkdcs.v2.model.instances import Instances
from huaweicloudsdkdcs.v2.model.instances_monitored_object import InstancesMonitoredObject
from huaweicloudsdkdcs.v2.model.ip_exchange_request import IpExchangeRequest
from huaweicloudsdkdcs.v2.model.item import Item
from huaweicloudsdkdcs.v2.model.links_item import LinksItem
from huaweicloudsdkdcs.v2.model.list_acl_accounts_request import ListAclAccountsRequest
from huaweicloudsdkdcs.v2.model.list_acl_accounts_response import ListAclAccountsResponse
from huaweicloudsdkdcs.v2.model.list_available_zones_request import ListAvailableZonesRequest
from huaweicloudsdkdcs.v2.model.list_available_zones_response import ListAvailableZonesResponse
from huaweicloudsdkdcs.v2.model.list_background_task_request import ListBackgroundTaskRequest
from huaweicloudsdkdcs.v2.model.list_background_task_response import ListBackgroundTaskResponse
from huaweicloudsdkdcs.v2.model.list_backup_file_links_request import ListBackupFileLinksRequest
from huaweicloudsdkdcs.v2.model.list_backup_file_links_response import ListBackupFileLinksResponse
from huaweicloudsdkdcs.v2.model.list_backup_records_request import ListBackupRecordsRequest
from huaweicloudsdkdcs.v2.model.list_backup_records_response import ListBackupRecordsResponse
from huaweicloudsdkdcs.v2.model.list_bigkey_scan_tasks_request import ListBigkeyScanTasksRequest
from huaweicloudsdkdcs.v2.model.list_bigkey_scan_tasks_response import ListBigkeyScanTasksResponse
from huaweicloudsdkdcs.v2.model.list_center_task_request import ListCenterTaskRequest
from huaweicloudsdkdcs.v2.model.list_center_task_response import ListCenterTaskResponse
from huaweicloudsdkdcs.v2.model.list_center_tasks_resp import ListCenterTasksResp
from huaweicloudsdkdcs.v2.model.list_config_histories_request import ListConfigHistoriesRequest
from huaweicloudsdkdcs.v2.model.list_config_histories_response import ListConfigHistoriesResponse
from huaweicloudsdkdcs.v2.model.list_config_templates_request import ListConfigTemplatesRequest
from huaweicloudsdkdcs.v2.model.list_config_templates_response import ListConfigTemplatesResponse
from huaweicloudsdkdcs.v2.model.list_configurations_request import ListConfigurationsRequest
from huaweicloudsdkdcs.v2.model.list_configurations_response import ListConfigurationsResponse
from huaweicloudsdkdcs.v2.model.list_diagnosis_tasks_request import ListDiagnosisTasksRequest
from huaweicloudsdkdcs.v2.model.list_diagnosis_tasks_response import ListDiagnosisTasksResponse
from huaweicloudsdkdcs.v2.model.list_flavors_request import ListFlavorsRequest
from huaweicloudsdkdcs.v2.model.list_flavors_response import ListFlavorsResponse
from huaweicloudsdkdcs.v2.model.list_group_replication_info_request import ListGroupReplicationInfoRequest
from huaweicloudsdkdcs.v2.model.list_group_replication_info_response import ListGroupReplicationInfoResponse
from huaweicloudsdkdcs.v2.model.list_hot_key_scan_tasks_request import ListHotKeyScanTasksRequest
from huaweicloudsdkdcs.v2.model.list_hot_key_scan_tasks_response import ListHotKeyScanTasksResponse
from huaweicloudsdkdcs.v2.model.list_instance_operations_request import ListInstanceOperationsRequest
from huaweicloudsdkdcs.v2.model.list_instance_operations_response import ListInstanceOperationsResponse
from huaweicloudsdkdcs.v2.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkdcs.v2.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkdcs.v2.model.list_maintenance_windows_request import ListMaintenanceWindowsRequest
from huaweicloudsdkdcs.v2.model.list_maintenance_windows_response import ListMaintenanceWindowsResponse
from huaweicloudsdkdcs.v2.model.list_migration_task_logs_request import ListMigrationTaskLogsRequest
from huaweicloudsdkdcs.v2.model.list_migration_task_logs_response import ListMigrationTaskLogsResponse
from huaweicloudsdkdcs.v2.model.list_migration_task_request import ListMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.list_migration_task_response import ListMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.list_monitored_objects_of_instance_request import ListMonitoredObjectsOfInstanceRequest
from huaweicloudsdkdcs.v2.model.list_monitored_objects_of_instance_response import ListMonitoredObjectsOfInstanceResponse
from huaweicloudsdkdcs.v2.model.list_monitored_objects_request import ListMonitoredObjectsRequest
from huaweicloudsdkdcs.v2.model.list_monitored_objects_response import ListMonitoredObjectsResponse
from huaweicloudsdkdcs.v2.model.list_number_of_instances_in_different_status_request import ListNumberOfInstancesInDifferentStatusRequest
from huaweicloudsdkdcs.v2.model.list_number_of_instances_in_different_status_response import ListNumberOfInstancesInDifferentStatusResponse
from huaweicloudsdkdcs.v2.model.list_redislog_request import ListRedislogRequest
from huaweicloudsdkdcs.v2.model.list_redislog_response import ListRedislogResponse
from huaweicloudsdkdcs.v2.model.list_restore_records_request import ListRestoreRecordsRequest
from huaweicloudsdkdcs.v2.model.list_restore_records_response import ListRestoreRecordsResponse
from huaweicloudsdkdcs.v2.model.list_slowlog_request import ListSlowlogRequest
from huaweicloudsdkdcs.v2.model.list_slowlog_response import ListSlowlogResponse
from huaweicloudsdkdcs.v2.model.list_statistics_of_running_instances_request import ListStatisticsOfRunningInstancesRequest
from huaweicloudsdkdcs.v2.model.list_statistics_of_running_instances_response import ListStatisticsOfRunningInstancesResponse
from huaweicloudsdkdcs.v2.model.list_tags_of_tenant_request import ListTagsOfTenantRequest
from huaweicloudsdkdcs.v2.model.list_tags_of_tenant_response import ListTagsOfTenantResponse
from huaweicloudsdkdcs.v2.model.login_web_cli_body import LoginWebCliBody
from huaweicloudsdkdcs.v2.model.login_web_cli_request import LoginWebCliRequest
from huaweicloudsdkdcs.v2.model.login_web_cli_response import LoginWebCliResponse
from huaweicloudsdkdcs.v2.model.logoff_web_cli_request import LogoffWebCliRequest
from huaweicloudsdkdcs.v2.model.logoff_web_cli_response import LogoffWebCliResponse
from huaweicloudsdkdcs.v2.model.logout_web_cli_body import LogoutWebCliBody
from huaweicloudsdkdcs.v2.model.maintain_windows_entity import MaintainWindowsEntity
from huaweicloudsdkdcs.v2.model.migration_log import MigrationLog
from huaweicloudsdkdcs.v2.model.migration_task_list import MigrationTaskList
from huaweicloudsdkdcs.v2.model.migration_update_request_entity import MigrationUpdateRequestEntity
from huaweicloudsdkdcs.v2.model.modify_instance_body import ModifyInstanceBody
from huaweicloudsdkdcs.v2.model.modify_instance_password_body import ModifyInstancePasswordBody
from huaweicloudsdkdcs.v2.model.modify_ip_whitelist_body import ModifyIpWhitelistBody
from huaweicloudsdkdcs.v2.model.modify_redis_config_body import ModifyRedisConfigBody
from huaweicloudsdkdcs.v2.model.nodes_info_resp import NodesInfoResp
from huaweicloudsdkdcs.v2.model.operations import Operations
from huaweicloudsdkdcs.v2.model.priority_body import PriorityBody
from huaweicloudsdkdcs.v2.model.proxy2_node_monitored_object import Proxy2NodeMonitoredObject
from huaweicloudsdkdcs.v2.model.proxy_node_monitored_object import ProxyNodeMonitoredObject
from huaweicloudsdkdcs.v2.model.query_redis_config import QueryRedisConfig
from huaweicloudsdkdcs.v2.model.query_tenant_quota_resp_quotas import QueryTenantQuotaRespQuotas
from huaweicloudsdkdcs.v2.model.records_response import RecordsResponse
from huaweicloudsdkdcs.v2.model.redis_config import RedisConfig
from huaweicloudsdkdcs.v2.model.rename_command_resp import RenameCommandResp
from huaweicloudsdkdcs.v2.model.replication_info import ReplicationInfo
from huaweicloudsdkdcs.v2.model.reset_acl_account_pass_word_request import ResetAclAccountPassWordRequest
from huaweicloudsdkdcs.v2.model.reset_acl_account_pass_word_response import ResetAclAccountPassWordResponse
from huaweicloudsdkdcs.v2.model.reset_instance_password_body import ResetInstancePasswordBody
from huaweicloudsdkdcs.v2.model.reset_password_request import ResetPasswordRequest
from huaweicloudsdkdcs.v2.model.reset_password_response import ResetPasswordResponse
from huaweicloudsdkdcs.v2.model.resize_instance_body import ResizeInstanceBody
from huaweicloudsdkdcs.v2.model.resize_instance_request import ResizeInstanceRequest
from huaweicloudsdkdcs.v2.model.resize_instance_response import ResizeInstanceResponse
from huaweicloudsdkdcs.v2.model.resource_tag import ResourceTag
from huaweicloudsdkdcs.v2.model.resources import Resources
from huaweicloudsdkdcs.v2.model.restart_or_flush_instances_request import RestartOrFlushInstancesRequest
from huaweicloudsdkdcs.v2.model.restart_or_flush_instances_response import RestartOrFlushInstancesResponse
from huaweicloudsdkdcs.v2.model.restore_instance_body import RestoreInstanceBody
from huaweicloudsdkdcs.v2.model.restore_instance_request import RestoreInstanceRequest
from huaweicloudsdkdcs.v2.model.restore_instance_response import RestoreInstanceResponse
from huaweicloudsdkdcs.v2.model.runlog_item import RunlogItem
from huaweicloudsdkdcs.v2.model.scan_expire_key_request import ScanExpireKeyRequest
from huaweicloudsdkdcs.v2.model.scan_expire_key_response import ScanExpireKeyResponse
from huaweicloudsdkdcs.v2.model.set_online_migration_task_body import SetOnlineMigrationTaskBody
from huaweicloudsdkdcs.v2.model.set_online_migration_task_request import SetOnlineMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.set_online_migration_task_response import SetOnlineMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.show_background_task_progress_request import ShowBackgroundTaskProgressRequest
from huaweicloudsdkdcs.v2.model.show_background_task_progress_response import ShowBackgroundTaskProgressResponse
from huaweicloudsdkdcs.v2.model.show_bigkey_autoscan_config_request import ShowBigkeyAutoscanConfigRequest
from huaweicloudsdkdcs.v2.model.show_bigkey_autoscan_config_response import ShowBigkeyAutoscanConfigResponse
from huaweicloudsdkdcs.v2.model.show_bigkey_scan_task_details_request import ShowBigkeyScanTaskDetailsRequest
from huaweicloudsdkdcs.v2.model.show_bigkey_scan_task_details_response import ShowBigkeyScanTaskDetailsResponse
from huaweicloudsdkdcs.v2.model.show_config_history_detail_request import ShowConfigHistoryDetailRequest
from huaweicloudsdkdcs.v2.model.show_config_history_detail_response import ShowConfigHistoryDetailResponse
from huaweicloudsdkdcs.v2.model.show_config_template_request import ShowConfigTemplateRequest
from huaweicloudsdkdcs.v2.model.show_config_template_response import ShowConfigTemplateResponse
from huaweicloudsdkdcs.v2.model.show_diagnosis_task_details_request import ShowDiagnosisTaskDetailsRequest
from huaweicloudsdkdcs.v2.model.show_diagnosis_task_details_response import ShowDiagnosisTaskDetailsResponse
from huaweicloudsdkdcs.v2.model.show_expire_auto_scan_config_request import ShowExpireAutoScanConfigRequest
from huaweicloudsdkdcs.v2.model.show_expire_auto_scan_config_response import ShowExpireAutoScanConfigResponse
from huaweicloudsdkdcs.v2.model.show_expire_key_scan_info_request import ShowExpireKeyScanInfoRequest
from huaweicloudsdkdcs.v2.model.show_expire_key_scan_info_response import ShowExpireKeyScanInfoResponse
from huaweicloudsdkdcs.v2.model.show_hotkey_autoscan_config_request import ShowHotkeyAutoscanConfigRequest
from huaweicloudsdkdcs.v2.model.show_hotkey_autoscan_config_response import ShowHotkeyAutoscanConfigResponse
from huaweicloudsdkdcs.v2.model.show_hotkey_task_details_request import ShowHotkeyTaskDetailsRequest
from huaweicloudsdkdcs.v2.model.show_hotkey_task_details_response import ShowHotkeyTaskDetailsResponse
from huaweicloudsdkdcs.v2.model.show_instance_request import ShowInstanceRequest
from huaweicloudsdkdcs.v2.model.show_instance_response import ShowInstanceResponse
from huaweicloudsdkdcs.v2.model.show_instance_ssl_detail_request import ShowInstanceSslDetailRequest
from huaweicloudsdkdcs.v2.model.show_instance_ssl_detail_response import ShowInstanceSslDetailResponse
from huaweicloudsdkdcs.v2.model.show_ip_whitelist_request import ShowIpWhitelistRequest
from huaweicloudsdkdcs.v2.model.show_ip_whitelist_response import ShowIpWhitelistResponse
from huaweicloudsdkdcs.v2.model.show_job_info_request import ShowJobInfoRequest
from huaweicloudsdkdcs.v2.model.show_job_info_response import ShowJobInfoResponse
from huaweicloudsdkdcs.v2.model.show_migration_task_request import ShowMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.show_migration_task_response import ShowMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.show_migration_task_stats_request import ShowMigrationTaskStatsRequest
from huaweicloudsdkdcs.v2.model.show_migration_task_stats_response import ShowMigrationTaskStatsResponse
from huaweicloudsdkdcs.v2.model.show_nodes_information_request import ShowNodesInformationRequest
from huaweicloudsdkdcs.v2.model.show_nodes_information_response import ShowNodesInformationResponse
from huaweicloudsdkdcs.v2.model.show_quota_of_tenant_request import ShowQuotaOfTenantRequest
from huaweicloudsdkdcs.v2.model.show_quota_of_tenant_response import ShowQuotaOfTenantResponse
from huaweicloudsdkdcs.v2.model.show_replication_states_request import ShowReplicationStatesRequest
from huaweicloudsdkdcs.v2.model.show_replication_states_response import ShowReplicationStatesResponse
from huaweicloudsdkdcs.v2.model.show_tags_request import ShowTagsRequest
from huaweicloudsdkdcs.v2.model.show_tags_response import ShowTagsResponse
from huaweicloudsdkdcs.v2.model.simple_key_scan_record import SimpleKeyScanRecord
from huaweicloudsdkdcs.v2.model.single_background_task import SingleBackgroundTask
from huaweicloudsdkdcs.v2.model.slowlog_item import SlowlogItem
from huaweicloudsdkdcs.v2.model.source_instance_body import SourceInstanceBody
from huaweicloudsdkdcs.v2.model.start_instance_resize_check_job_request import StartInstanceResizeCheckJobRequest
from huaweicloudsdkdcs.v2.model.start_instance_resize_check_job_request_body import StartInstanceResizeCheckJobRequestBody
from huaweicloudsdkdcs.v2.model.start_instance_resize_check_job_response import StartInstanceResizeCheckJobResponse
from huaweicloudsdkdcs.v2.model.status_statistic import StatusStatistic
from huaweicloudsdkdcs.v2.model.step_detail import StepDetail
from huaweicloudsdkdcs.v2.model.stop_migration_task_request import StopMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.stop_migration_task_response import StopMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.stop_migration_task_result import StopMigrationTaskResult
from huaweicloudsdkdcs.v2.model.stop_migration_task_sync_request import StopMigrationTaskSyncRequest
from huaweicloudsdkdcs.v2.model.stop_migration_task_sync_response import StopMigrationTaskSyncResponse
from huaweicloudsdkdcs.v2.model.sub_step_detail import SubStepDetail
from huaweicloudsdkdcs.v2.model.tag import Tag
from huaweicloudsdkdcs.v2.model.target_instance_body import TargetInstanceBody
from huaweicloudsdkdcs.v2.model.update_acl_account_pass_word_request import UpdateAclAccountPassWordRequest
from huaweicloudsdkdcs.v2.model.update_acl_account_pass_word_response import UpdateAclAccountPassWordResponse
from huaweicloudsdkdcs.v2.model.update_acl_account_remark_request import UpdateAclAccountRemarkRequest
from huaweicloudsdkdcs.v2.model.update_acl_account_remark_request_body import UpdateAclAccountRemarkRequestBody
from huaweicloudsdkdcs.v2.model.update_acl_account_remark_response import UpdateAclAccountRemarkResponse
from huaweicloudsdkdcs.v2.model.update_acl_account_request import UpdateAclAccountRequest
from huaweicloudsdkdcs.v2.model.update_acl_account_response import UpdateAclAccountResponse
from huaweicloudsdkdcs.v2.model.update_auto_scan_config_request_body import UpdateAutoScanConfigRequestBody
from huaweicloudsdkdcs.v2.model.update_bigkey_autoscan_config_request import UpdateBigkeyAutoscanConfigRequest
from huaweicloudsdkdcs.v2.model.update_bigkey_autoscan_config_response import UpdateBigkeyAutoscanConfigResponse
from huaweicloudsdkdcs.v2.model.update_client_ip_transparent_transmission_request import UpdateClientIpTransparentTransmissionRequest
from huaweicloudsdkdcs.v2.model.update_client_ip_transparent_transmission_request_body import UpdateClientIpTransparentTransmissionRequestBody
from huaweicloudsdkdcs.v2.model.update_client_ip_transparent_transmission_response import UpdateClientIpTransparentTransmissionResponse
from huaweicloudsdkdcs.v2.model.update_config_template_request import UpdateConfigTemplateRequest
from huaweicloudsdkdcs.v2.model.update_config_template_response import UpdateConfigTemplateResponse
from huaweicloudsdkdcs.v2.model.update_configurations_request import UpdateConfigurationsRequest
from huaweicloudsdkdcs.v2.model.update_configurations_response import UpdateConfigurationsResponse
from huaweicloudsdkdcs.v2.model.update_custom_template_body import UpdateCustomTemplateBody
from huaweicloudsdkdcs.v2.model.update_expire_auto_scan_config_request import UpdateExpireAutoScanConfigRequest
from huaweicloudsdkdcs.v2.model.update_expire_auto_scan_config_response import UpdateExpireAutoScanConfigResponse
from huaweicloudsdkdcs.v2.model.update_hotkey_auto_scan_config_request import UpdateHotkeyAutoScanConfigRequest
from huaweicloudsdkdcs.v2.model.update_hotkey_auto_scan_config_response import UpdateHotkeyAutoScanConfigResponse
from huaweicloudsdkdcs.v2.model.update_instance_bandwidth_request import UpdateInstanceBandwidthRequest
from huaweicloudsdkdcs.v2.model.update_instance_bandwidth_response import UpdateInstanceBandwidthResponse
from huaweicloudsdkdcs.v2.model.update_instance_config_request import UpdateInstanceConfigRequest
from huaweicloudsdkdcs.v2.model.update_instance_config_response import UpdateInstanceConfigResponse
from huaweicloudsdkdcs.v2.model.update_instance_request import UpdateInstanceRequest
from huaweicloudsdkdcs.v2.model.update_instance_response import UpdateInstanceResponse
from huaweicloudsdkdcs.v2.model.update_ip_whitelist_request import UpdateIpWhitelistRequest
from huaweicloudsdkdcs.v2.model.update_ip_whitelist_response import UpdateIpWhitelistResponse
from huaweicloudsdkdcs.v2.model.update_migration_task_request import UpdateMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.update_migration_task_response import UpdateMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.update_password_request import UpdatePasswordRequest
from huaweicloudsdkdcs.v2.model.update_password_response import UpdatePasswordResponse
from huaweicloudsdkdcs.v2.model.update_ssl_switch_request_body import UpdateSSLSwitchRequestBody
from huaweicloudsdkdcs.v2.model.update_slave_priority_request import UpdateSlavePriorityRequest
from huaweicloudsdkdcs.v2.model.update_slave_priority_response import UpdateSlavePriorityResponse
from huaweicloudsdkdcs.v2.model.update_ssl_switch_request import UpdateSslSwitchRequest
from huaweicloudsdkdcs.v2.model.update_ssl_switch_response import UpdateSslSwitchResponse
from huaweicloudsdkdcs.v2.model.validate_deletable_replica_request import ValidateDeletableReplicaRequest
from huaweicloudsdkdcs.v2.model.validate_deletable_replica_response import ValidateDeletableReplicaResponse
from huaweicloudsdkdcs.v2.model.whitelist import Whitelist
