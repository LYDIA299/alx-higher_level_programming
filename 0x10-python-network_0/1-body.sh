#!/bin/bash
# takes in a URL, sends GET request and displays the response body
curl -sL -X GET "$1"
