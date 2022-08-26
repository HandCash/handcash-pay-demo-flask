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
        "name": "5L - O25 Drink Clean",
        "description": "Enjoy your shot of pure water 💧 · 5000 ml",
        "imageUrl": "https://docs.o25.eu/photos/water%20wallpaper.jpg"
    },
    "receivers": [
        {
            "sendAmount": 2.00,
            "currencyCode": "EUR",
            "destination": "o25drinkclean"
        }
    ],
    "requestedUserData": ["paymail"],  # Any of [paymail, email, phoneNumber]
    "notifications": {
        "webhook": {
            "customParameters": {
                "fountainId": "davidlloyd-0001",
                "productId": "05000"
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
