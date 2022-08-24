# HandCash Pay demo for Flask

### Getting started
Sign into the HandCash Dashboard an create an app. 

Make sure you paste your `app-id` and `app-secret` into `config.py`.

You can find more at [HandCash for developers](https://docs.handcash.io).

### Start the server
Start the Flask server:
```shell script
flask --debug run
```

### Create a payment request
1) Open `create_payment_request.py` 
2) Edit the payload that contains all the properties for the payment request.
````python
payload = {
    "product": {
        "name": "Water · 250 ml",
        "description": "250ml of filtered water",
        "imageUrl": "https://www.indywaterpros.com/hs-fs/hubfs/2019-0~3-min.jpg?width=600&name=2019-0~3-min.jpg"
    },
    "receivers": [
        {
            "sendAmount": 0.25,
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
            "webhookUrl": "https://myservice.com/webhooks/handcash"
        },
        "email": "invoices@my-company.com"
    },
    "expirationType": "never",
    "redirectUrl": "https://myservice.com/purchase/success"
}
````

Once you are done, just run the script:
```shell script
python create_payment_request.py
```
