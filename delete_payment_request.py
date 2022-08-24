import requests

from config import Credentials

headers = {
    "app-secret": Credentials.app_secret,
    "app-id": Credentials.app_id,
}

payment_request_id = '63066e5f375d83b7f62e765f'
url = f"https://cloud.handcash.io/v2/paymentRequests/{payment_request_id}"

response = requests.delete(url, headers=headers)
print(f'{response.status_code} - {response.text}')
