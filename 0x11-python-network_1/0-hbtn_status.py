#!/usr/bin/python3
"""usign urlib to fetch some pages"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("UTF-8")))
