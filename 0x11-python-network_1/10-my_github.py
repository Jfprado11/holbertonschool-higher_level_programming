#!/usr/bin/python3
"""taking an api to post an email"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    datos = {"Authorization": "token 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"}

    response = requests.post(url, auth=(username, password))
    information = response.json()
    if any("id" == key for key in information.keys()):
        print(information["id"])
    else:
        print(None)
