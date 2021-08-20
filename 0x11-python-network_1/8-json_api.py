#!/usr/bin/python3
"""taking an api to post an email"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) <= 1:
        data = {"q": ""}
    else:
        data = {"q": sys.argv[1]}

    response = requests.post(url, data=data)
    info = response.json()
    if type(info) is not dict:
        print("Not a valid JSON")
    elif len(info) <= 0:
        print("No result")
    else:
        print("[{}] {}".format(info["id"], info["name"]))
