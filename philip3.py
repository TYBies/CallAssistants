import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('VAPI_CALL_URL')

payload = {
    "maxDurationSeconds": 600,
    "phoneNumber": {
        "twilioPhoneNumber": os.getenv('TWILLIO_PHONENUMBER'),
        "twilioAccountSid": os.getenv('TWILLIO_ACCT_SID'),
        "twilioAuthToken": os.getenv('TWILLIO_AUTHTOKEN'),
        "serverUrl": os.getenv('WEBHOOK_SERVER_URL'),
        "name": "Emma"
    },
    "customer": {
        "number": os.getenv('TWILLIO_FORWARDING_NUMBER'),#using this for test purpose only
        "name": ""
    }
}
headers = {
    "Authorization": os.getenv('VAPI_BEARER_TOKEN'),
    "Content-Type": "application/json"
}

response = requests.get(url, headers={'Authorization': os.getenv('VAPI_BEARER_TOKEN')})
print(response.text)

