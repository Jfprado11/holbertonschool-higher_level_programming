#!/usr/bin/python3
"""taking an api to post an email"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))
    try:
        information = response.json()
        print(information["id"])
    except:
        print("None")
