#!/usr/bin/python3
"""takes in a URL, sends a request to the
URL and displays the body of the response"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            page = page.decode("UTF-8")
            print(page)
    except HTTPError as bad:
        print("Error code: {}".format(bad.status))
