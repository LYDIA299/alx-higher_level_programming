#!/bin/bash
# sends a request to URL, passes an argument and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
