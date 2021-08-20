#!/usr/bin/python3
"""a URL and an email, sends a POST request to the
passed URL with the email as a parameter"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        page = page.decode("UTF-8")
        print(page)
