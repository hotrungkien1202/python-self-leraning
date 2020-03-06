from flask import Flask, render_template, request
import os
import requests
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/save', methods = ['POST'])
@auth.login_required
def home():
    data = request.data
    content = data.decode("utf-8")
    f = open('demofile.txt', 'w')
    f.write(content)
    f.close()
    return "Data saved"


@app.route("/get-log", methods = ['GET'])
@auth.login_required
def get_data():
    f = open("demofile.txt", 'r')
    data = f.read()
    return data


if __name__ == '__main__':
   app.run()