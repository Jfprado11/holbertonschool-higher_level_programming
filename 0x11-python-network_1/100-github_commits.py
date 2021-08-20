#!/usr/bin/python3
"""taking an api show the commir"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo)

    response = requests.get(url)
    data = response.json()
    for x in range(0, 10):
        print("{}: {}".format(data[x]["sha"],
              data[x]["commit"]["author"]["name"]))
