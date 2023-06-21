# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkclassroom.v3.model.apply_judgement_request import ApplyJudgementRequest
from huaweicloudsdkclassroom.v3.model.apply_judgement_response import ApplyJudgementResponse
from huaweicloudsdkclassroom.v3.model.classroom_card import ClassroomCard
from huaweicloudsdkclassroom.v3.model.classroom_member import ClassroomMember
from huaweicloudsdkclassroom.v3.model.difficult_info import DifficultInfo
from huaweicloudsdkclassroom.v3.model.execute_exercise_request import ExecuteExerciseRequest
from huaweicloudsdkclassroom.v3.model.execute_exercise_response import ExecuteExerciseResponse
from huaweicloudsdkclassroom.v3.model.exercise_card import ExerciseCard
from huaweicloudsdkclassroom.v3.model.exercise_case_resource import ExerciseCaseResource
from huaweicloudsdkclassroom.v3.model.exercise_code_resource import ExerciseCodeResource
from huaweicloudsdkclassroom.v3.model.exercise_detail_data import ExerciseDetailData
from huaweicloudsdkclassroom.v3.model.exercise_filter import ExerciseFilter
from huaweicloudsdkclassroom.v3.model.exercise_group import ExerciseGroup
from huaweicloudsdkclassroom.v3.model.exercises_list_request_body import ExercisesListRequestBody
from huaweicloudsdkclassroom.v3.model.job_card import JobCard
from huaweicloudsdkclassroom.v3.model.job_records import JobRecords
from huaweicloudsdkclassroom.v3.model.judgement_case_info import JudgementCaseInfo
from huaweicloudsdkclassroom.v3.model.judgement_case_result import JudgementCaseResult
from huaweicloudsdkclassroom.v3.model.judgement_result import JudgementResult
from huaweicloudsdkclassroom.v3.model.judgement_task_request_body import JudgementTaskRequestBody
from huaweicloudsdkclassroom.v3.model.knowledge_point_info import KnowledgePointInfo
from huaweicloudsdkclassroom.v3.model.knowledge_points_list_request_body import KnowledgePointsListRequestBody
from huaweicloudsdkclassroom.v3.model.list_all_difficults_request import ListAllDifficultsRequest
from huaweicloudsdkclassroom.v3.model.list_all_difficults_response import ListAllDifficultsResponse
from huaweicloudsdkclassroom.v3.model.list_classroom_member_jobs_request import ListClassroomMemberJobsRequest
from huaweicloudsdkclassroom.v3.model.list_classroom_member_jobs_response import ListClassroomMemberJobsResponse
from huaweicloudsdkclassroom.v3.model.list_classroom_members_request import ListClassroomMembersRequest
from huaweicloudsdkclassroom.v3.model.list_classroom_members_response import ListClassroomMembersResponse
from huaweicloudsdkclassroom.v3.model.list_classrooms_request import ListClassroomsRequest
from huaweicloudsdkclassroom.v3.model.list_classrooms_response import ListClassroomsResponse
from huaweicloudsdkclassroom.v3.model.list_exercises_request import ListExercisesRequest
from huaweicloudsdkclassroom.v3.model.list_exercises_response import ListExercisesResponse
from huaweicloudsdkclassroom.v3.model.list_jobs_request import ListJobsRequest
from huaweicloudsdkclassroom.v3.model.list_jobs_response import ListJobsResponse
from huaweicloudsdkclassroom.v3.model.list_member_job_records_request import ListMemberJobRecordsRequest
from huaweicloudsdkclassroom.v3.model.list_member_job_records_response import ListMemberJobRecordsResponse
from huaweicloudsdkclassroom.v3.model.list_my_knowledge_points_request import ListMyKnowledgePointsRequest
from huaweicloudsdkclassroom.v3.model.list_my_knowledge_points_response import ListMyKnowledgePointsResponse
from huaweicloudsdkclassroom.v3.model.list_packages_request import ListPackagesRequest
from huaweicloudsdkclassroom.v3.model.list_packages_response import ListPackagesResponse
from huaweicloudsdkclassroom.v3.model.member_job_card import MemberJobCard
from huaweicloudsdkclassroom.v3.model.package_card import PackageCard
from huaweicloudsdkclassroom.v3.model.package_exercise_card import PackageExerciseCard
from huaweicloudsdkclassroom.v3.model.package_exercise_judge_request_body import PackageExerciseJudgeRequestBody
from huaweicloudsdkclassroom.v3.model.package_filter import PackageFilter
from huaweicloudsdkclassroom.v3.model.packages_list_request_body import PackagesListRequestBody
from huaweicloudsdkclassroom.v3.model.show_classroom_detail_request import ShowClassroomDetailRequest
from huaweicloudsdkclassroom.v3.model.show_classroom_detail_response import ShowClassroomDetailResponse
from huaweicloudsdkclassroom.v3.model.show_exercise_detail_request import ShowExerciseDetailRequest
from huaweicloudsdkclassroom.v3.model.show_exercise_detail_response import ShowExerciseDetailResponse
from huaweicloudsdkclassroom.v3.model.show_job_detail_request import ShowJobDetailRequest
from huaweicloudsdkclassroom.v3.model.show_job_detail_response import ShowJobDetailResponse
from huaweicloudsdkclassroom.v3.model.show_job_exercises_request import ShowJobExercisesRequest
from huaweicloudsdkclassroom.v3.model.show_job_exercises_response import ShowJobExercisesResponse
from huaweicloudsdkclassroom.v3.model.show_judgement_detail_request import ShowJudgementDetailRequest
from huaweicloudsdkclassroom.v3.model.show_judgement_detail_response import ShowJudgementDetailResponse
from huaweicloudsdkclassroom.v3.model.show_judgement_file_request import ShowJudgementFileRequest
from huaweicloudsdkclassroom.v3.model.show_judgement_file_response import ShowJudgementFileResponse
from huaweicloudsdkclassroom.v3.model.show_package_detail_request import ShowPackageDetailRequest
from huaweicloudsdkclassroom.v3.model.show_package_detail_response import ShowPackageDetailResponse
