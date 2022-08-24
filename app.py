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

recent_payments = []


@app.route("/")
def list_products():
    url = "https://cloud.handcash.io/v2/paymentRequests"
    response = requests.get(url, headers=headers)

    print(f'{response.status_code} - {response.text}')
    if response.ok:
        return render_template("list-products.html", paymentRequests=response.json()["items"],
                               recentPayments=recent_payments)
    return response.text


@app.route("/webhooks/handcash", methods=["POST"])
def on_payment_completed():
    data = request.json
    print(data)
    if data['appSecret'] == Credentials.app_secret:  # Make sure the request comes from HandCash
        recent_payments.insert(0, data)
        # You can trigger your own process on payment completed: unlock some content, send a custom email...
    return 'OK'
