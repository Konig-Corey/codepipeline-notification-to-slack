import slackHelper
import pipelineHelper
import unittest
from unittest import mock
import json

class Test(unittest.TestCase):

    @mock.patch('pipelineHelper.get_pipelines_execution_details')
    def test_get_code_pipeline_details(self, MockPipeline):
        pipeline = MockPipeline()

        pipeline.return_value = '{"jobDetails": {"accountId": "111111111111","data": {"actionConfiguration": {"__type": "ActionConfiguration","configuration": {"ProjectName": "JenkinsTestProject"}},"actionTypeId": {"__type": "ActionTypeId","category": "Test","owner": "Custom","provider": "JenkinsProviderName","version": "1"},"artifactCredentials": {"__type": "AWSSessionCredentials","accessKeyId": "AKIAIOSFODNN7EXAMPLE","secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY","sessionToken": "fICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE="},"inputArtifacts": [{"__type": "Artifact","location": {"s3Location": {"bucketName": "codepipeline-us-east-1-11EXAMPLE11","objectKey": "MySecondPipeline/MyAppBuild/EXAMPLE"},"type": "S3"},"name": "MyAppBuild"}],"outputArtifacts": [],"pipelineContext": {"__type": "PipelineContext","action": {"name": "JenkinsTestAction"},"pipelineName": "MySecondPipeline","stage": {"name": "Testing"}}},"id": "ef66c259-EXAMPLE"}}'
        response = pipeline()
        self.assertIsNotNone(response)
        self.assertIsInstance(json.loads(response), dict)

    #slackHelper tests
    @mock.patch('slackHelper.send_slack_message')
    def test_send_slack_message(self, mock_post):
        fake_payload = {"attachments": [{"fallback": "Details about notification from codepipeline.","color": "#0000ff","author_name": "Codepipeline Notifier","title": "[MySecondPipeline] status has changed","title_link": "https://api.slack.com/","text": "[JenkinsTestAction] was triggered in [Testing] pipeline stage","ts": 123456789}]}
        mock_post.return_value = True
        resp =  slackHelper.send_slack_message(fake_payload)
        self.assertEqual(resp, True)

    def test_build_slack_message(self):
        #passed event, job details
        mock_event = {"version": "0","id": "ac3e6e4b-c294-4250-e9b3-f463c21daae9","detail-type": "CodePipeline Pipeline Execution State Change","source": "aws.codepipeline","account": "705750910119","time": "2018-02-11T05:02:03Z","region": "us-west-2","resources": ["arn:aws:codepipeline:us-west-2:705750910119:test-codepipeline"],"detail": {"pipeline": "test-codepipeline","execution-id": "dc023fbb-e8f6-44aa-911e-d2d47bb6b132","state": "STARTED","version": 4}}
        mock_pipeline = {"jobDetails": {"accountId": "111111111111","data": {"actionConfiguration": {"__type": "ActionConfiguration","configuration": {"ProjectName": "JenkinsTestProject"}},"actionTypeId": {"__type": "ActionTypeId","category": "Test","owner": "Custom","provider": "JenkinsProviderName","version": "1"},"artifactCredentials": {"__type": "AWSSessionCredentials","accessKeyId": "AKIAIOSFODNN7EXAMPLE","secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY","sessionToken": "fICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE="},"inputArtifacts": [{"__type": "Artifact","location": {"s3Location": {"bucketName": "codepipeline-us-east-1-11EXAMPLE11","objectKey": "MySecondPipeline/MyAppBuild/EXAMPLE"},"type": "S3"},"name": "MyAppBuild"}],"outputArtifacts": [],"pipelineContext": {"__type": "PipelineContext","action": {"name": "JenkinsTestAction"},"pipelineName": "MySecondPipeline","stage": {"name": "Testing"}}},"id": "ef66c259-EXAMPLE"}}

        #returns slack message payload
        correct_response = {"attachments": [{"fallback": "Details about notification from codepipeline.","color": "#0000ff","author_name": "Codepipeline Notifier","title": "[MySecondPipeline] status has changed","title_link": "https://api.slack.com/","text": "[JenkinsTestAction] was triggered in [Testing] pipeline stage","ts": 123456789}]}
        self.assertEqual(slackHelper.get_slack_message(mock_pipeline, mock_event), correct_response)

    def test_get_color_by_status(self):
        self.assertEqual(slackHelper.get_color_by_status('FAILURE'), '#ff0000')
        self.assertEqual(slackHelper.get_color_by_status('SUCCEDED'), '#00ff00')
        self.assertEqual(slackHelper.get_color_by_status('CANCELLED'), '#ffff00')
        self.assertEqual(slackHelper.get_color_by_status('TEST-OTHER'), '#0000ff')


if __name__ == "__main__":
    unittest.main()


