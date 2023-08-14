import sys
import json
from aws_lambda_context import LambdaContext
from test_module import Test


def handler(event, context: LambdaContext):
    print("testing")
    Test()
    return 'Hello from AWS Lambda using Python' + sys.version + '!' + 'Event: ' + json.dumps(event)
