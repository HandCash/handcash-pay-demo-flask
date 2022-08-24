import json

import requests

from config import Credentials

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "app-secret": Credentials.app_secret,
    "app-id": Credentials.app_id,
}

url = "https://cloud.handcash.io/v2/paymentRequests"
payload = {
    "product": {
        "name": "Water · 500 ml",
        "description": "500ml of filtered water",
        "imageUrl": "https://www.indywaterpros.com/hs-fs/hubfs/2019-0~3-min.jpg?width=600&name=2019-0~3-min.jpg"
    },
    "receivers": [
        {
            "sendAmount": 0.5,
            "currencyCode": "USD",
            "destination": "rjseibane"
        }
    ],
    "requestedUserData": ["paymail"],  # Any of [paymail, email, phoneNumber]
    "notifications": {
        "webhook": {
            "customParameters": {
                "fountainId": "1002913",
                "productId": "00006"
            },
            "webhookUrl": "https://www.o25.eu"
        },
        "email": "rafa@handcash.io"
    },
    "expirationType": "never",
    "redirectUrl": "https://glacial-mountain-91065.herokuapp.com/webhooks/handcash"
}
response = requests.post(url, json=payload, headers=headers)

print(f'{response.status_code} - {response.text}')
if 'application/json' in response.headers.get('content-type'):
    print(json.dumps(response.json(), indent=3))
else:
    print(response.text)
