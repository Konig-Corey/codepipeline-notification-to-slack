import json
import boto3

codepipeline = boto3.client('codepipeline', region_name='us-east-1')

def get_pipelines_execution_details(executionId, pipeline):
    '''get execution details '''
    return codepipeline.get_job_details(executionId)


def get_commit_details_of_build():
    '''gets details about commit from current stage, commit info is only available in build'''
    pass