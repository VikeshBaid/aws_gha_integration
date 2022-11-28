import boto3
import json
import hashlib
import hmac
import datetime
import os

SECRET_NAME = "TEST/sandbox/shodan-test-api"
SM_CLIENT = boto3.client('secretsmanager')
SECRET_VALUES = json.loads(
    SM_CLIENT.get_secret_value(SecretId=SECRET_NAME).get('SecretString', "{}")
)

def get_shodan_api_key():
    return SECRET_VALUES.get('api_key')

def lambda_handler(event, context):

    my_key = get_shodan_api_key()
    print(my_key)
#     print("rest api ")
#     print(event)
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }

