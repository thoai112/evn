from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAARynmWpSZCIBOZBOZCSO0ybd4BB4ZAkOZB7IVu1l7OAQXt9FJTc3dbcEnJqogORqKjLkJWQCge4AZBMoiKlZCgHVKZAJjZB6bZArVaEreFK6TBpqsP6RYZBagLLKNTz6eZCUOi2bXboQuZB3zI1AuzgzAFJfMiyz2OqZBQs3lSYeuBFn7gpgXU5mmta4uzZC9wQCEqj5H2dBI99ZCnTK70PV1tmSgZDZD"
sender_id = "7670798873002030"
customer_id = "PC08CC0332738"
reqAuth = {
    "url": f"https://graph.facebook.com/v20.0/me/messages?access_token={PAGE_ACCESS_TOKEN}",
    "login": "https://cskh-api.cpc.vn/api/cskh/user/login",
    "data": "https://cskh-api.cpc.vn/api/remote/meter/rf/sl-tieu-thu-view",
    "payment": "https://appcskh.cpc.vn:4433/api/v4/customer/home/",
    "postmethod": "POST",
    "getMethod": "GET"
}


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        body = json.dumps({
            "username": username,
            "password": password,
            "grant_type": "password",
            "scope": "CSKH",
            "ThongTinCaptcha": {
                "captcha": "undefined",
                "token": "undefined"
            }
        })
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json;charset=UTF-8",
            "Access-Control-Allow-Origin": "*",
            "Connection": "keep-alive"
        }

        # Make the HTTP request
        response = requests.post(reqAuth['login'], headers=headers, data=body)

        # Return the response from the external service
        return jsonify(response.json()), response.status_code
    elif request.method == 'GET':
        # Define logic for GET request or simply return a message
        return 'GET request to /login is not supported', 405
