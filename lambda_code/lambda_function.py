import json


def lambda_handler(event, context):
    print("rest api ")
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }