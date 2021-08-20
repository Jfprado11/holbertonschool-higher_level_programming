#!/usr/bin/python3
"""a URL, sends a request to the URL and displays the
value of the variable"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    value = response.headers["X-Request-Id"]
    print(value)
