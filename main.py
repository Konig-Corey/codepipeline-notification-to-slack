import json
import slackHelper
import pipelineHelper
import variables

def main(event, context):
    print(f"Recieved Event - {json.dumps(event)}")

    pipeline = event['detail']['pipeline']
    state = event['detail']['state']

    #if event is relavent pipeline,
    if variables.pipelines is None or pipeline in variables.pipelines:
        if variables.states is None or state in variables.states:
            details = pipelineHelper.get_pipelines_execution_details(event["id"], pipeline)
            msg = slackHelper.get_slack_message(details, event)
            slackHelper.send_slack_message(msg)