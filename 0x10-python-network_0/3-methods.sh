#!/bin/bash
# show all options for methods
curl -sI $1 | grep Allow: | cut -b 8-
