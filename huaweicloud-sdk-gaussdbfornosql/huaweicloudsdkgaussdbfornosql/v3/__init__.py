# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkgaussdbfornosql.v3.gaussdbfornosql_client import GaussDBforNoSQLClient
from huaweicloudsdkgaussdbfornosql.v3.gaussdbfornosql_async_client import GaussDBforNoSQLAsyncClient

from huaweicloudsdkgaussdbfornosql.v3.model.action_body import ActionBody
from huaweicloudsdkgaussdbfornosql.v3.model.api_version_response import ApiVersionResponse
from huaweicloudsdkgaussdbfornosql.v3.model.applicable_instance_rsp import ApplicableInstanceRsp
from huaweicloudsdkgaussdbfornosql.v3.model.apply_configuration_request import ApplyConfigurationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.apply_configuration_request_body import ApplyConfigurationRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.apply_configuration_response import ApplyConfigurationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.apply_history_rsp import ApplyHistoryRsp
from huaweicloudsdkgaussdbfornosql.v3.model.availability_zone_detail import AvailabilityZoneDetail
from huaweicloudsdkgaussdbfornosql.v3.model.backup import Backup
from huaweicloudsdkgaussdbfornosql.v3.model.backup_policy import BackupPolicy
from huaweicloudsdkgaussdbfornosql.v3.model.backup_strategy_option import BackupStrategyOption
from huaweicloudsdkgaussdbfornosql.v3.model.backup_strategy_result import BackupStrategyResult
from huaweicloudsdkgaussdbfornosql.v3.model.batch_tag_action_request import BatchTagActionRequest
from huaweicloudsdkgaussdbfornosql.v3.model.batch_tag_action_request_body import BatchTagActionRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.batch_tag_action_response import BatchTagActionResponse
from huaweicloudsdkgaussdbfornosql.v3.model.batch_tag_action_tag_option import BatchTagActionTagOption
from huaweicloudsdkgaussdbfornosql.v3.model.cassandra_slow_log_detail import CassandraSlowLogDetail
from huaweicloudsdkgaussdbfornosql.v3.model.charge_info_option import ChargeInfoOption
from huaweicloudsdkgaussdbfornosql.v3.model.charge_info_result import ChargeInfoResult
from huaweicloudsdkgaussdbfornosql.v3.model.check_disaster_recovery_operation_request import CheckDisasterRecoveryOperationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.check_disaster_recovery_operation_response import CheckDisasterRecoveryOperationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.check_week_password_request import CheckWeekPasswordRequest
from huaweicloudsdkgaussdbfornosql.v3.model.check_week_password_request_body import CheckWeekPasswordRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.check_week_password_response import CheckWeekPasswordResponse
from huaweicloudsdkgaussdbfornosql.v3.model.command_info import CommandInfo
from huaweicloudsdkgaussdbfornosql.v3.model.compare_configuration_request import CompareConfigurationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.compare_configuration_request_body import CompareConfigurationRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.compare_configuration_response import CompareConfigurationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.compute_flavor import ComputeFlavor
from huaweicloudsdkgaussdbfornosql.v3.model.configuration_history_rsp import ConfigurationHistoryRsp
from huaweicloudsdkgaussdbfornosql.v3.model.configuration_parameter_result import ConfigurationParameterResult
from huaweicloudsdkgaussdbfornosql.v3.model.construct_disaster_recovery_body import ConstructDisasterRecoveryBody
from huaweicloudsdkgaussdbfornosql.v3.model.construct_disaster_recovery_instance import ConstructDisasterRecoveryInstance
from huaweicloudsdkgaussdbfornosql.v3.model.copy_configuration_request import CopyConfigurationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.copy_configuration_request_body import CopyConfigurationRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.copy_configuration_response import CopyConfigurationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.create_back_request import CreateBackRequest
from huaweicloudsdkgaussdbfornosql.v3.model.create_back_response import CreateBackResponse
from huaweicloudsdkgaussdbfornosql.v3.model.create_cold_volume_request import CreateColdVolumeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.create_cold_volume_request_body import CreateColdVolumeRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.create_cold_volume_response import CreateColdVolumeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.create_configuration_datastore_option import CreateConfigurationDatastoreOption
from huaweicloudsdkgaussdbfornosql.v3.model.create_configuration_request import CreateConfigurationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.create_configuration_request_body import CreateConfigurationRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.create_configuration_response import CreateConfigurationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.create_configuration_result import CreateConfigurationResult
from huaweicloudsdkgaussdbfornosql.v3.model.create_db_user_request import CreateDbUserRequest
from huaweicloudsdkgaussdbfornosql.v3.model.create_db_user_response import CreateDbUserResponse
from huaweicloudsdkgaussdbfornosql.v3.model.create_disaster_recovery_request import CreateDisasterRecoveryRequest
from huaweicloudsdkgaussdbfornosql.v3.model.create_disaster_recovery_response import CreateDisasterRecoveryResponse
from huaweicloudsdkgaussdbfornosql.v3.model.create_instance_flavor_option import CreateInstanceFlavorOption
from huaweicloudsdkgaussdbfornosql.v3.model.create_instance_flavor_result import CreateInstanceFlavorResult
from huaweicloudsdkgaussdbfornosql.v3.model.create_instance_request import CreateInstanceRequest
from huaweicloudsdkgaussdbfornosql.v3.model.create_instance_request_body import CreateInstanceRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.create_instance_response import CreateInstanceResponse
from huaweicloudsdkgaussdbfornosql.v3.model.data_store_list import DataStoreList
from huaweicloudsdkgaussdbfornosql.v3.model.datastore import Datastore
from huaweicloudsdkgaussdbfornosql.v3.model.datastore_option import DatastoreOption
from huaweicloudsdkgaussdbfornosql.v3.model.datastore_result import DatastoreResult
from huaweicloudsdkgaussdbfornosql.v3.model.dedicated_resource_capacity import DedicatedResourceCapacity
from huaweicloudsdkgaussdbfornosql.v3.model.delete_backup_request import DeleteBackupRequest
from huaweicloudsdkgaussdbfornosql.v3.model.delete_backup_response import DeleteBackupResponse
from huaweicloudsdkgaussdbfornosql.v3.model.delete_configuration_request import DeleteConfigurationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.delete_configuration_response import DeleteConfigurationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.delete_db_user_request import DeleteDbUserRequest
from huaweicloudsdkgaussdbfornosql.v3.model.delete_db_user_response import DeleteDbUserResponse
from huaweicloudsdkgaussdbfornosql.v3.model.delete_disaster_recovery_request import DeleteDisasterRecoveryRequest
from huaweicloudsdkgaussdbfornosql.v3.model.delete_disaster_recovery_response import DeleteDisasterRecoveryResponse
from huaweicloudsdkgaussdbfornosql.v3.model.delete_enlarge_fail_node_request import DeleteEnlargeFailNodeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.delete_enlarge_fail_node_request_body import DeleteEnlargeFailNodeRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.delete_enlarge_fail_node_response import DeleteEnlargeFailNodeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.delete_instance_request import DeleteInstanceRequest
from huaweicloudsdkgaussdbfornosql.v3.model.delete_instance_response import DeleteInstanceResponse
from huaweicloudsdkgaussdbfornosql.v3.model.delete_instances_session_request import DeleteInstancesSessionRequest
from huaweicloudsdkgaussdbfornosql.v3.model.delete_instances_session_request_body import DeleteInstancesSessionRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.delete_instances_session_response import DeleteInstancesSessionResponse
from huaweicloudsdkgaussdbfornosql.v3.model.delete_lts_configs_request import DeleteLtsConfigsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.delete_lts_configs_request_body import DeleteLtsConfigsRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.delete_lts_configs_response import DeleteLtsConfigsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.different_details import DifferentDetails
from huaweicloudsdkgaussdbfornosql.v3.model.disk_auto_expansion_policy import DiskAutoExpansionPolicy
from huaweicloudsdkgaussdbfornosql.v3.model.error_log_list import ErrorLogList
from huaweicloudsdkgaussdbfornosql.v3.model.error_response_body import ErrorResponseBody
from huaweicloudsdkgaussdbfornosql.v3.model.expand_instance_node_request import ExpandInstanceNodeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.expand_instance_node_request_body import ExpandInstanceNodeRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.expand_instance_node_response import ExpandInstanceNodeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.influxdb_slow_log_detail import InfluxdbSlowLogDetail
from huaweicloudsdkgaussdbfornosql.v3.model.instance_log_config import InstanceLogConfig
from huaweicloudsdkgaussdbfornosql.v3.model.instance_log_config_detail import InstanceLogConfigDetail
from huaweicloudsdkgaussdbfornosql.v3.model.instance_result import InstanceResult
from huaweicloudsdkgaussdbfornosql.v3.model.instance_tag_result import InstanceTagResult
from huaweicloudsdkgaussdbfornosql.v3.model.instances_datastore_result import InstancesDatastoreResult
from huaweicloudsdkgaussdbfornosql.v3.model.job_detail import JobDetail
from huaweicloudsdkgaussdbfornosql.v3.model.job_instance_info import JobInstanceInfo
from huaweicloudsdkgaussdbfornosql.v3.model.links import Links
from huaweicloudsdkgaussdbfornosql.v3.model.list_api_version_request import ListApiVersionRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_api_version_response import ListApiVersionResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_available_flavor_infos_request import ListAvailableFlavorInfosRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_available_flavor_infos_response import ListAvailableFlavorInfosResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_cassandra_slow_logs_request import ListCassandraSlowLogsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_cassandra_slow_logs_request_body import ListCassandraSlowLogsRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.list_cassandra_slow_logs_response import ListCassandraSlowLogsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_configuration_datastores_request import ListConfigurationDatastoresRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_configuration_datastores_response import ListConfigurationDatastoresResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_configuration_templates_request import ListConfigurationTemplatesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_configuration_templates_response import ListConfigurationTemplatesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_configurations_request import ListConfigurationsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_configurations_response import ListConfigurationsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_configurations_result import ListConfigurationsResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_datastores_request import ListDatastoresRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_datastores_response import ListDatastoresResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_db_users_request import ListDbUsersRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_db_users_response import ListDbUsersResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_dedicated_resource_result import ListDedicatedResourceResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_dedicated_resources_request import ListDedicatedResourcesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_dedicated_resources_response import ListDedicatedResourcesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_eps_quotas_request import ListEpsQuotasRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_eps_quotas_response import ListEpsQuotasResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_flavor_infos_request import ListFlavorInfosRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_flavor_infos_response import ListFlavorInfosResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_flavors_request import ListFlavorsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_flavors_response import ListFlavorsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_flavors_result import ListFlavorsResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_influxdb_slow_logs_request import ListInfluxdbSlowLogsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_influxdb_slow_logs_request_body import ListInfluxdbSlowLogsRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.list_influxdb_slow_logs_response import ListInfluxdbSlowLogsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_instance_databases_request import ListInstanceDatabasesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_instance_databases_response import ListInstanceDatabasesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_instance_tags_request import ListInstanceTagsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_instance_tags_response import ListInstanceTagsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_instance_tags_result import ListInstanceTagsResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_backup_strategy_result import ListInstancesBackupStrategyResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_by_resource_tags_request import ListInstancesByResourceTagsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_by_resource_tags_response import ListInstancesByResourceTagsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_by_tags_request import ListInstancesByTagsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_by_tags_request_body import ListInstancesByTagsRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_by_tags_response import ListInstancesByTagsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_datastore_result import ListInstancesDatastoreResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_group_result import ListInstancesGroupResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_node_result import ListInstancesNodeResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_result import ListInstancesResult
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_session_request import ListInstancesSessionRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_session_respond_body_sessions import ListInstancesSessionRespondBodySessions
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_session_response import ListInstancesSessionResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_session_statistics_request import ListInstancesSessionStatisticsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_session_statistics_respond_body_top_source_ips import ListInstancesSessionStatisticsRespondBodyTopSourceIps
from huaweicloudsdkgaussdbfornosql.v3.model.list_instances_session_statistics_response import ListInstancesSessionStatisticsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_jobs_request import ListJobsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_jobs_response import ListJobsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_lts_configs_request import ListLtsConfigsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_lts_configs_response import ListLtsConfigsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_mongodb_error_logs_request import ListMongodbErrorLogsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_mongodb_error_logs_request_body import ListMongodbErrorLogsRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.list_mongodb_error_logs_response import ListMongodbErrorLogsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_mongodb_slow_logs_request import ListMongodbSlowLogsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_mongodb_slow_logs_request_body import ListMongodbSlowLogsRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.list_mongodb_slow_logs_response import ListMongodbSlowLogsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_recycle_instances_request import ListRecycleInstancesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_recycle_instances_response import ListRecycleInstancesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_redis_slow_logs_request import ListRedisSlowLogsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_redis_slow_logs_request_body import ListRedisSlowLogsRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.list_redis_slow_logs_response import ListRedisSlowLogsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_restore_databases_request import ListRestoreDatabasesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_restore_databases_response import ListRestoreDatabasesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_restore_tables_request import ListRestoreTablesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_restore_tables_response import ListRestoreTablesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_restore_time_request import ListRestoreTimeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_restore_time_response import ListRestoreTimeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.list_slow_logs_request import ListSlowLogsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.list_slow_logs_response import ListSlowLogsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.log_instance_info import LogInstanceInfo
from huaweicloudsdkgaussdbfornosql.v3.model.match_option import MatchOption
from huaweicloudsdkgaussdbfornosql.v3.model.modify_db_user_privilege_request import ModifyDbUserPrivilegeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.modify_db_user_privilege_response import ModifyDbUserPrivilegeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.modify_eps_quotas_request import ModifyEpsQuotasRequest
from huaweicloudsdkgaussdbfornosql.v3.model.modify_eps_quotas_response import ModifyEpsQuotasResponse
from huaweicloudsdkgaussdbfornosql.v3.model.modify_port_request import ModifyPortRequest
from huaweicloudsdkgaussdbfornosql.v3.model.modify_port_request_body import ModifyPortRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.modify_port_response import ModifyPortResponse
from huaweicloudsdkgaussdbfornosql.v3.model.modify_public_ip_request import ModifyPublicIpRequest
from huaweicloudsdkgaussdbfornosql.v3.model.modify_public_ip_request_body import ModifyPublicIpRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.modify_public_ip_response import ModifyPublicIpResponse
from huaweicloudsdkgaussdbfornosql.v3.model.modify_volume_request import ModifyVolumeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.modify_volume_request_body import ModifyVolumeRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.modify_volume_response import ModifyVolumeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.mongodb_error_log_detail import MongodbErrorLogDetail
from huaweicloudsdkgaussdbfornosql.v3.model.mongodb_slow_log_detail import MongodbSlowLogDetail
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_dr_date_sync_indicators import NoSQLDrDateSyncIndicators
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_dr_rpo_and_rto import NoSQLDrRpoAndRto
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_create_backup_request_body import NoSqlCreateBackupRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_eps_quota_request_info import NoSqlEpsQuotaRequestInfo
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_eps_quota_total import NoSqlEpsQuotaTotal
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_eps_quota_used import NoSqlEpsQuotaUsed
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_modifly_eps_quotas_request_body import NoSqlModiflyEpsQuotasRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_query_eps_quota_info import NoSqlQueryEpsQuotaInfo
from huaweicloudsdkgaussdbfornosql.v3.model.no_sql_request_eps_quota import NoSqlRequestEpsQuota
from huaweicloudsdkgaussdbfornosql.v3.model.offline_nodes_request import OfflineNodesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.offline_nodes_request_body import OfflineNodesRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.offline_nodes_response import OfflineNodesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.optional_flavors_info import OptionalFlavorsInfo
from huaweicloudsdkgaussdbfornosql.v3.model.pause_resume_data_synchronization_request import PauseResumeDataSynchronizationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.pause_resume_data_synchronization_response import PauseResumeDataSynchronizationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.precheck_disaster_recovery_instance import PrecheckDisasterRecoveryInstance
from huaweicloudsdkgaussdbfornosql.v3.model.precheck_disaster_recovery_operation_body import PrecheckDisasterRecoveryOperationBody
from huaweicloudsdkgaussdbfornosql.v3.model.query_database_table_info import QueryDatabaseTableInfo
from huaweicloudsdkgaussdbfornosql.v3.model.query_instance_backup_response_body_backups import QueryInstanceBackupResponseBodyBackups
from huaweicloudsdkgaussdbfornosql.v3.model.query_instance_backup_response_body_datastore import QueryInstanceBackupResponseBodyDatastore
from huaweicloudsdkgaussdbfornosql.v3.model.query_restore_list import QueryRestoreList
from huaweicloudsdkgaussdbfornosql.v3.model.recycle_datastore import RecycleDatastore
from huaweicloudsdkgaussdbfornosql.v3.model.recycle_instance import RecycleInstance
from huaweicloudsdkgaussdbfornosql.v3.model.recycle_policy import RecyclePolicy
from huaweicloudsdkgaussdbfornosql.v3.model.recycle_policy_request_body import RecyclePolicyRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.redis_create_db_user_request import RedisCreateDbUserRequest
from huaweicloudsdkgaussdbfornosql.v3.model.redis_db_user_info import RedisDbUserInfo
from huaweicloudsdkgaussdbfornosql.v3.model.redis_delete_db_user_request import RedisDeleteDbUserRequest
from huaweicloudsdkgaussdbfornosql.v3.model.redis_modify_db_user_privilege_request import RedisModifyDBUserPrivilegeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.redis_modify_db_user_privilege_request_body import RedisModifyDbUserPrivilegeRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.redis_reset_db_user_password_request_body import RedisResetDbUserPasswordRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.redis_slow_log_detail import RedisSlowLogDetail
from huaweicloudsdkgaussdbfornosql.v3.model.redis_user_for_creation import RedisUserForCreation
from huaweicloudsdkgaussdbfornosql.v3.model.rename_high_risk_commands_request import RenameHighRiskCommandsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.reset_db_user_password_request import ResetDbUserPasswordRequest
from huaweicloudsdkgaussdbfornosql.v3.model.reset_db_user_password_response import ResetDbUserPasswordResponse
from huaweicloudsdkgaussdbfornosql.v3.model.reset_param_group_template_request import ResetParamGroupTemplateRequest
from huaweicloudsdkgaussdbfornosql.v3.model.reset_param_group_template_response import ResetParamGroupTemplateResponse
from huaweicloudsdkgaussdbfornosql.v3.model.reset_password_request import ResetPasswordRequest
from huaweicloudsdkgaussdbfornosql.v3.model.reset_password_request_body import ResetPasswordRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.reset_password_response import ResetPasswordResponse
from huaweicloudsdkgaussdbfornosql.v3.model.resize_cold_volume_request import ResizeColdVolumeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.resize_cold_volume_request_body import ResizeColdVolumeRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.resize_cold_volume_response import ResizeColdVolumeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.resize_instance_option import ResizeInstanceOption
from huaweicloudsdkgaussdbfornosql.v3.model.resize_instance_request import ResizeInstanceRequest
from huaweicloudsdkgaussdbfornosql.v3.model.resize_instance_request_body import ResizeInstanceRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.resize_instance_response import ResizeInstanceResponse
from huaweicloudsdkgaussdbfornosql.v3.model.resize_instance_volume_request import ResizeInstanceVolumeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.resize_instance_volume_request_body import ResizeInstanceVolumeRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.resize_instance_volume_response import ResizeInstanceVolumeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.restart_instance_request import RestartInstanceRequest
from huaweicloudsdkgaussdbfornosql.v3.model.restart_instance_response import RestartInstanceResponse
from huaweicloudsdkgaussdbfornosql.v3.model.restorable_time import RestorableTime
from huaweicloudsdkgaussdbfornosql.v3.model.restore_existing_instance_request import RestoreExistingInstanceRequest
from huaweicloudsdkgaussdbfornosql.v3.model.restore_existing_instance_response import RestoreExistingInstanceResponse
from huaweicloudsdkgaussdbfornosql.v3.model.restore_info import RestoreInfo
from huaweicloudsdkgaussdbfornosql.v3.model.restore_request_body import RestoreRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.save_lts_configs_request import SaveLtsConfigsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.save_lts_configs_request_body import SaveLtsConfigsRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.save_lts_configs_response import SaveLtsConfigsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.set_auto_enlarge_policy_request import SetAutoEnlargePolicyRequest
from huaweicloudsdkgaussdbfornosql.v3.model.set_auto_enlarge_policy_response import SetAutoEnlargePolicyResponse
from huaweicloudsdkgaussdbfornosql.v3.model.set_auto_policy_request_body import SetAutoPolicyRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.set_backup_policy_request import SetBackupPolicyRequest
from huaweicloudsdkgaussdbfornosql.v3.model.set_backup_policy_request_body import SetBackupPolicyRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.set_backup_policy_response import SetBackupPolicyResponse
from huaweicloudsdkgaussdbfornosql.v3.model.set_recycle_policy_request import SetRecyclePolicyRequest
from huaweicloudsdkgaussdbfornosql.v3.model.set_recycle_policy_response import SetRecyclePolicyResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_all_instances_backups_new_request import ShowAllInstancesBackupsNewRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_all_instances_backups_new_response import ShowAllInstancesBackupsNewResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_all_instances_backups_request import ShowAllInstancesBackupsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_all_instances_backups_response import ShowAllInstancesBackupsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_api_version_request import ShowApiVersionRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_api_version_response import ShowApiVersionResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_applicable_instances_request import ShowApplicableInstancesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_applicable_instances_response import ShowApplicableInstancesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_apply_history_request import ShowApplyHistoryRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_apply_history_response import ShowApplyHistoryResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_auto_enlarge_policy_request import ShowAutoEnlargePolicyRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_auto_enlarge_policy_response import ShowAutoEnlargePolicyResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_backup_policy_request import ShowBackupPolicyRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_backup_policy_response import ShowBackupPolicyResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_backup_policy_result import ShowBackupPolicyResult
from huaweicloudsdkgaussdbfornosql.v3.model.show_configuration_detail_request import ShowConfigurationDetailRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_configuration_detail_response import ShowConfigurationDetailResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_elb_ip_group_request import ShowElbIpGroupRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_elb_ip_group_response import ShowElbIpGroupResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_error_log_request import ShowErrorLogRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_error_log_response import ShowErrorLogResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_high_risk_commands_request import ShowHighRiskCommandsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_high_risk_commands_response import ShowHighRiskCommandsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_instance_biactive_regions_request import ShowInstanceBiactiveRegionsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_instance_biactive_regions_response import ShowInstanceBiactiveRegionsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_instance_configuration_request import ShowInstanceConfigurationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_instance_configuration_response import ShowInstanceConfigurationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_instance_role_request import ShowInstanceRoleRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_instance_role_response import ShowInstanceRoleResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_ip_num_requirement_request import ShowIpNumRequirementRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_ip_num_requirement_response import ShowIpNumRequirementResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_modify_history_request import ShowModifyHistoryRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_modify_history_response import ShowModifyHistoryResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_pause_resume_stutus_request import ShowPauseResumeStutusRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_pause_resume_stutus_response import ShowPauseResumeStutusResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_quotas_request import ShowQuotasRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_quotas_response import ShowQuotasResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_recycle_policy_request import ShowRecyclePolicyRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_recycle_policy_response import ShowRecyclePolicyResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_resources_detail_response_body import ShowResourcesDetailResponseBody
from huaweicloudsdkgaussdbfornosql.v3.model.show_resources_list_response_body import ShowResourcesListResponseBody
from huaweicloudsdkgaussdbfornosql.v3.model.show_restorable_list_request import ShowRestorableListRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_restorable_list_response import ShowRestorableListResponse
from huaweicloudsdkgaussdbfornosql.v3.model.show_slow_log_desensitization_request import ShowSlowLogDesensitizationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.show_slow_log_desensitization_response import ShowSlowLogDesensitizationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.shrink_instance_node_request import ShrinkInstanceNodeRequest
from huaweicloudsdkgaussdbfornosql.v3.model.shrink_instance_node_request_body import ShrinkInstanceNodeRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.shrink_instance_node_response import ShrinkInstanceNodeResponse
from huaweicloudsdkgaussdbfornosql.v3.model.slowlog_result import SlowlogResult
from huaweicloudsdkgaussdbfornosql.v3.model.switch_ip_group_request import SwitchIpGroupRequest
from huaweicloudsdkgaussdbfornosql.v3.model.switch_ip_group_request_body import SwitchIpGroupRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.switch_ip_group_request_body_ip_groups import SwitchIpGroupRequestBodyIpGroups
from huaweicloudsdkgaussdbfornosql.v3.model.switch_ip_group_response import SwitchIpGroupResponse
from huaweicloudsdkgaussdbfornosql.v3.model.switch_slowlog_desensitization_request import SwitchSlowlogDesensitizationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.switch_slowlog_desensitization_request_body import SwitchSlowlogDesensitizationRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.switch_slowlog_desensitization_response import SwitchSlowlogDesensitizationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.switch_ssl_request import SwitchSslRequest
from huaweicloudsdkgaussdbfornosql.v3.model.switch_ssl_request_body import SwitchSslRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.switch_ssl_response import SwitchSslResponse
from huaweicloudsdkgaussdbfornosql.v3.model.switch_to_master_disaster_recovery_body import SwitchToMasterDisasterRecoveryBody
from huaweicloudsdkgaussdbfornosql.v3.model.switch_to_master_request import SwitchToMasterRequest
from huaweicloudsdkgaussdbfornosql.v3.model.switch_to_master_response import SwitchToMasterResponse
from huaweicloudsdkgaussdbfornosql.v3.model.switch_to_slave_request import SwitchToSlaveRequest
from huaweicloudsdkgaussdbfornosql.v3.model.switch_to_slave_response import SwitchToSlaveResponse
from huaweicloudsdkgaussdbfornosql.v3.model.tag import Tag
from huaweicloudsdkgaussdbfornosql.v3.model.tag_option import TagOption
from huaweicloudsdkgaussdbfornosql.v3.model.update_client_network_request import UpdateClientNetworkRequest
from huaweicloudsdkgaussdbfornosql.v3.model.update_client_network_request_body import UpdateClientNetworkRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.update_client_network_response import UpdateClientNetworkResponse
from huaweicloudsdkgaussdbfornosql.v3.model.update_configuration_request import UpdateConfigurationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.update_configuration_request_body import UpdateConfigurationRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.update_configuration_response import UpdateConfigurationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.update_databases_request import UpdateDatabasesRequest
from huaweicloudsdkgaussdbfornosql.v3.model.update_databases_request_body import UpdateDatabasesRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.update_databases_response import UpdateDatabasesResponse
from huaweicloudsdkgaussdbfornosql.v3.model.update_high_risk_commands_request import UpdateHighRiskCommandsRequest
from huaweicloudsdkgaussdbfornosql.v3.model.update_high_risk_commands_response import UpdateHighRiskCommandsResponse
from huaweicloudsdkgaussdbfornosql.v3.model.update_instance_configuration_request import UpdateInstanceConfigurationRequest
from huaweicloudsdkgaussdbfornosql.v3.model.update_instance_configuration_request_body import UpdateInstanceConfigurationRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.update_instance_configuration_response import UpdateInstanceConfigurationResponse
from huaweicloudsdkgaussdbfornosql.v3.model.update_instance_name_request import UpdateInstanceNameRequest
from huaweicloudsdkgaussdbfornosql.v3.model.update_instance_name_request_body import UpdateInstanceNameRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.update_instance_name_response import UpdateInstanceNameResponse
from huaweicloudsdkgaussdbfornosql.v3.model.update_security_group_request import UpdateSecurityGroupRequest
from huaweicloudsdkgaussdbfornosql.v3.model.update_security_group_request_body import UpdateSecurityGroupRequestBody
from huaweicloudsdkgaussdbfornosql.v3.model.update_security_group_response import UpdateSecurityGroupResponse
from huaweicloudsdkgaussdbfornosql.v3.model.upgrade_db_version_request import UpgradeDbVersionRequest
from huaweicloudsdkgaussdbfornosql.v3.model.upgrade_db_version_response import UpgradeDbVersionResponse
from huaweicloudsdkgaussdbfornosql.v3.model.volume import Volume

