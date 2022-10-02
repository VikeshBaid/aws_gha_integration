import json
import requests

webhook_url="https://dhdko4aog9.execute-api.us-east-1.amazonaws.com/webhook"
data = {'text': "waf applied to block my IP"}

response=requests.post(
    webhook_url, data=json.dumps(data),headers={'Content-Type': 'application/json'}
)

if response.status_code!=200:
    raise ValueError(
        'REquest to api gateway returned an error %s, the response is:\n%s'%(response.status_code, response.text)
    )