#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of response
curl -s "$1" | wc -c
