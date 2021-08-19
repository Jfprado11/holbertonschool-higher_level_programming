#!/bin/bash
# sends a request to a URL passed as an argument
curl -o /dev/null -s --head -w '%{http_code}' $1
