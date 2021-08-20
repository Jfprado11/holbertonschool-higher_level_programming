#!/usr/bin/python3
"""taking an api show the commir"""

import requests
import sys

if __name__ == "__main__":
    owner_name = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo)

    response = requests.get(url)
    try:
        data = response.json()
        for x in range(10):
            print("{}: {}".format(data[x]["sha"],
                                  data[x]["commit"]["author"]["name"]))
    except:
        pass
