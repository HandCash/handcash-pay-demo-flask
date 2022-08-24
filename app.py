from flask import Flask, render_template, request
import requests

from config import Credentials

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

headers = {
    "Accept": "application/json",
    "app-secret": Credentials.app_secret,
    "app-id": Credentials.app_id
}

recent_payments = [
    {
        'paymentRequestId': '123123123132131',
        'transactionId': '123123123132131',
        'requestedUserData': {
            'paymail': 'rafa@handcash.io'
        }
    },
    {
        'paymentRequestId': '123123123132131',
        'transactionId': '123123123132131',
        'requestedUserData': {
            'paymail': 'rafa@handcash.io'
        }
    },
    {
        'paymentRequestId': '123123123132131',
        'transactionId': '123123123132131',
        'requestedUserData': {
            'paymail': 'rafa@handcash.io'
        }
    }
]


@app.route("/")
def list_products():
    url = "https://cloud.handcash.io/v2/paymentRequests"
    response = requests.get(url, headers=headers)

    print(f'{response.status_code} - {response.text}')
    if response.ok:
        return render_template("list-products.html", paymentRequests=response.json()["items"],
                               recentPayments=recent_payments)
    return response.text


@app.route("/webhooks/handcash")
def on_payment_completed():
    data = request.json
    print(data)
    recent_payments.insert(0, data)
    return 'OK'
