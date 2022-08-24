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
        "name": "Water · 200 ml",
        "description": "200ml of filtered water",
        "imageUrl": "https://www.indywaterpros.com/hs-fs/hubfs/2019-0~3-min.jpg?width=600&name=2019-0~3-min.jpg"
    },
    "receivers": [
        {
            "sendAmount": 0.2,
            "currencyCode": "USD",
            "destination": "rjseibane"
        }
    ],
    "requestedUserData": ["paymail"],  # Any of [paymail, email, phoneNumber]
    "notifications": {
        "webhook": {
            "customParameters": {
                "fountainId": "madrid-0018",
                "productId": "00002"
            },
            "webhookUrl": "https://glacial-mountain-91065.herokuapp.com/webhooks/handcash"
        },
        "email": "rafa@handcash.io"
    },
    "expirationType": "never",
    "redirectUrl": "https://www.o25.eu"
}
response = requests.post(url, json=payload, headers=headers)

print(f'{response.status_code} - {response.text}')
if 'application/json' in response.headers.get('content-type'):
    print(json.dumps(response.json(), indent=3))
else:
    print(response.text)
