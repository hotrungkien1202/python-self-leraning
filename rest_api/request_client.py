import requests
import json 
import datetime
from requests.auth import HTTPBasicAuth


def post_request(url, content):
    res = requests.post(url, data=content, auth=HTTPBasicAuth('john', 'hello'))
    if res.status_code == 200:
        return "post request successfully"
    else:
        return "post request error {}".format(res.status_code)


def get_request(url):
    res = requests.get(url, auth=HTTPBasicAuth('john', 'hello'))
    if res.status_code == 200:
        data = res.text
    else:
        data = "error {}".format(res.status_code)
    return data


if __name__ == "__main__":
    while 1:
        print("method = ", end="")
        method = int(input())
        if method == 1:
            url = "http://localhost:5000/save"
            d = datetime.datetime.now()
            content = "Contents is {}".format(d)
            print(post_request(url, content))
        elif method == 2:
            url = "http://localhost:5000/get-log"
            print(get_request(url))
        else:
            exit(0)