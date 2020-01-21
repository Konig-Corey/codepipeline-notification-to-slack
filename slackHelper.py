import json
import urllib3
import os

WEBHOOK_URL=os.getenv("WEBHOOK_URL", None)

def send_slack_message(payload):
    print("attempting to send slack message...")

    http = urllib3.PoolManager()
    r = http.request('POST', WEBHOOK_URL,
                     headers={'Content-Type': 'application/json'},
                     body=json.dumps(payload))
    if r.status_code != 200:
        return False
        print("An error occured sending to slack: %s" % r.read())
    else:
        return True
        print("Slack message has been sent...")

def get_slack_message(jobDetails, cloudwatchEvent):
    print("building slack message...")
    action = jobDetails['jobDetails']['data']['pipelineContext']['action']['name']
    stage = jobDetails['jobDetails']['data']['pipelineContext']['stage']['name']
    pipelineName = jobDetails['jobDetails']['data']['pipelineContext']['pipelineName']
    state = cloudwatchEvent['detail']['state']

    payload = {
        "attachments": [
            {
                "fallback": "Details about notification from codepipeline.",
                "color": get_color_by_status(state),
                "author_name": "Codepipeline Notifier",
                "title": "[{}] status has changed".format(pipelineName),
                "title_link": "https://api.slack.com/",
                "text": "[{}] was triggered in [{}] pipeline stage".format(action, stage),
                "ts": 123456789
            }
        ]
    }

    return payload

def get_color_by_status(state):
    print("converting state to color...")
    if state is 'SUCCEDED':
        return '#00ff00'
    elif state is 'FAILURE':
        return '#ff0000'
    elif state is 'CANCELLED':
        return '#ffff00'
    else:
        return '#0000ff'
