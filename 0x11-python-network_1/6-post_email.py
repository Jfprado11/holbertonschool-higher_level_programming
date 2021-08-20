#!/usr/bin/python3
"""posting a email address"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data_send = {"email": sys.argv[2]}

    response = requests.post(url, data=data_send)
    print(response.text)
