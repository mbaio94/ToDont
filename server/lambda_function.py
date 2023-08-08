import sys
import json


def handler(event, context):
    return 'Hello from AWS Lambda using Python' + sys.version + '!' + 'Event: ' + json.dumps(event)
