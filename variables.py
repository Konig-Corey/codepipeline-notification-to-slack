import os

def attempt_split_with_comma(val):
    if val is None:
        return None
    try:
        return val.split(",")
    except:
        return val

#env vars
pipelines = attempt_split_with_comma(os.environ.get('pipelines', None))
states = attempt_split_with_comma(os.environ.get('states', None))
slackToken = attempt_split_with_comma(os.environ.get('slacktoken', None))
