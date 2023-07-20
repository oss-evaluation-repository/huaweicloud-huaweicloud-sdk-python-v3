# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkcloudrtc.v2.cloudrtc_client import CloudRTCClient
from huaweicloudsdkcloudrtc.v2.cloudrtc_async_client import CloudRTCAsyncClient

from huaweicloudsdkcloudrtc.v2.model.app import App
from huaweicloudsdkcloudrtc.v2.model.app_auth import AppAuth
from huaweicloudsdkcloudrtc.v2.model.app_auth_req import AppAuthReq
from huaweicloudsdkcloudrtc.v2.model.app_auto_record_mode import AppAutoRecordMode
from huaweicloudsdkcloudrtc.v2.model.app_callback_url import AppCallbackUrl
from huaweicloudsdkcloudrtc.v2.model.app_callback_url_req import AppCallbackUrlReq
from huaweicloudsdkcloudrtc.v2.model.app_callbacks import AppCallbacks
from huaweicloudsdkcloudrtc.v2.model.app_req import AppReq
from huaweicloudsdkcloudrtc.v2.model.app_state import AppState
from huaweicloudsdkcloudrtc.v2.model.auto_record_mode_req import AutoRecordModeReq
from huaweicloudsdkcloudrtc.v2.model.create_app_request import CreateAppRequest
from huaweicloudsdkcloudrtc.v2.model.create_app_response import CreateAppResponse
from huaweicloudsdkcloudrtc.v2.model.create_individual_stream_job_request import CreateIndividualStreamJobRequest
from huaweicloudsdkcloudrtc.v2.model.create_individual_stream_job_response import CreateIndividualStreamJobResponse
from huaweicloudsdkcloudrtc.v2.model.create_mix_job_request import CreateMixJobRequest
from huaweicloudsdkcloudrtc.v2.model.create_mix_job_response import CreateMixJobResponse
from huaweicloudsdkcloudrtc.v2.model.create_record_rule_request import CreateRecordRuleRequest
from huaweicloudsdkcloudrtc.v2.model.create_record_rule_response import CreateRecordRuleResponse
from huaweicloudsdkcloudrtc.v2.model.delete_app_request import DeleteAppRequest
from huaweicloudsdkcloudrtc.v2.model.delete_app_response import DeleteAppResponse
from huaweicloudsdkcloudrtc.v2.model.delete_record_rule_request import DeleteRecordRuleRequest
from huaweicloudsdkcloudrtc.v2.model.delete_record_rule_response import DeleteRecordRuleResponse
from huaweicloudsdkcloudrtc.v2.model.hls_record_config import HLSRecordConfig
from huaweicloudsdkcloudrtc.v2.model.individual_stream_job_req import IndividualStreamJobReq
from huaweicloudsdkcloudrtc.v2.model.list_apps_request import ListAppsRequest
from huaweicloudsdkcloudrtc.v2.model.list_apps_response import ListAppsResponse
from huaweicloudsdkcloudrtc.v2.model.list_record_rules_request import ListRecordRulesRequest
from huaweicloudsdkcloudrtc.v2.model.list_record_rules_response import ListRecordRulesResponse
from huaweicloudsdkcloudrtc.v2.model.mp4_record_config import MP4RecordConfig
from huaweicloudsdkcloudrtc.v2.model.mix_job_req import MixJobReq
from huaweicloudsdkcloudrtc.v2.model.mix_layout_pane import MixLayoutPane
from huaweicloudsdkcloudrtc.v2.model.mix_param import MixParam
from huaweicloudsdkcloudrtc.v2.model.mix_user_background_image import MixUserBackgroundImage
from huaweicloudsdkcloudrtc.v2.model.record_obs_file_addr import RecordObsFileAddr
from huaweicloudsdkcloudrtc.v2.model.record_param import RecordParam
from huaweicloudsdkcloudrtc.v2.model.record_rule import RecordRule
from huaweicloudsdkcloudrtc.v2.model.record_rule_req import RecordRuleReq
from huaweicloudsdkcloudrtc.v2.model.remove_room_request import RemoveRoomRequest
from huaweicloudsdkcloudrtc.v2.model.remove_room_response import RemoveRoomResponse
from huaweicloudsdkcloudrtc.v2.model.remove_users_req import RemoveUsersReq
from huaweicloudsdkcloudrtc.v2.model.remove_users_request import RemoveUsersRequest
from huaweicloudsdkcloudrtc.v2.model.remove_users_response import RemoveUsersResponse
from huaweicloudsdkcloudrtc.v2.model.show_app_request import ShowAppRequest
from huaweicloudsdkcloudrtc.v2.model.show_app_response import ShowAppResponse
from huaweicloudsdkcloudrtc.v2.model.show_auto_record_request import ShowAutoRecordRequest
from huaweicloudsdkcloudrtc.v2.model.show_auto_record_response import ShowAutoRecordResponse
from huaweicloudsdkcloudrtc.v2.model.show_individual_stream_job_request import ShowIndividualStreamJobRequest
from huaweicloudsdkcloudrtc.v2.model.show_individual_stream_job_response import ShowIndividualStreamJobResponse
from huaweicloudsdkcloudrtc.v2.model.show_mix_job_request import ShowMixJobRequest
from huaweicloudsdkcloudrtc.v2.model.show_mix_job_response import ShowMixJobResponse
from huaweicloudsdkcloudrtc.v2.model.show_record_callback_request import ShowRecordCallbackRequest
from huaweicloudsdkcloudrtc.v2.model.show_record_callback_response import ShowRecordCallbackResponse
from huaweicloudsdkcloudrtc.v2.model.show_record_rule_request import ShowRecordRuleRequest
from huaweicloudsdkcloudrtc.v2.model.show_record_rule_response import ShowRecordRuleResponse
from huaweicloudsdkcloudrtc.v2.model.show_url_auth_request import ShowUrlAuthRequest
from huaweicloudsdkcloudrtc.v2.model.show_url_auth_response import ShowUrlAuthResponse
from huaweicloudsdkcloudrtc.v2.model.start_app_request import StartAppRequest
from huaweicloudsdkcloudrtc.v2.model.start_app_response import StartAppResponse
from huaweicloudsdkcloudrtc.v2.model.stop_app_request import StopAppRequest
from huaweicloudsdkcloudrtc.v2.model.stop_app_response import StopAppResponse
from huaweicloudsdkcloudrtc.v2.model.stop_individual_stream_job_request import StopIndividualStreamJobRequest
from huaweicloudsdkcloudrtc.v2.model.stop_individual_stream_job_response import StopIndividualStreamJobResponse
from huaweicloudsdkcloudrtc.v2.model.stop_mix_job_request import StopMixJobRequest
from huaweicloudsdkcloudrtc.v2.model.stop_mix_job_response import StopMixJobResponse
from huaweicloudsdkcloudrtc.v2.model.update_auto_record_request import UpdateAutoRecordRequest
from huaweicloudsdkcloudrtc.v2.model.update_auto_record_response import UpdateAutoRecordResponse
from huaweicloudsdkcloudrtc.v2.model.update_individual_job_req import UpdateIndividualJobReq
from huaweicloudsdkcloudrtc.v2.model.update_individual_stream_job_request import UpdateIndividualStreamJobRequest
from huaweicloudsdkcloudrtc.v2.model.update_individual_stream_job_response import UpdateIndividualStreamJobResponse
from huaweicloudsdkcloudrtc.v2.model.update_mix_job_req import UpdateMixJobReq
from huaweicloudsdkcloudrtc.v2.model.update_mix_job_request import UpdateMixJobRequest
from huaweicloudsdkcloudrtc.v2.model.update_mix_job_response import UpdateMixJobResponse
from huaweicloudsdkcloudrtc.v2.model.update_mix_param import UpdateMixParam
from huaweicloudsdkcloudrtc.v2.model.update_record_callback_request import UpdateRecordCallbackRequest
from huaweicloudsdkcloudrtc.v2.model.update_record_callback_response import UpdateRecordCallbackResponse
from huaweicloudsdkcloudrtc.v2.model.update_record_rule_request import UpdateRecordRuleRequest
from huaweicloudsdkcloudrtc.v2.model.update_record_rule_response import UpdateRecordRuleResponse
from huaweicloudsdkcloudrtc.v2.model.update_url_auth_request import UpdateUrlAuthRequest
from huaweicloudsdkcloudrtc.v2.model.update_url_auth_response import UpdateUrlAuthResponse

