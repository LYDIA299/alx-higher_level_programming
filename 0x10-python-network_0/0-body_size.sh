#!/bin/bash
# takes in a URL, sends request to it and displays the size of body response.
curl -s "$1" | wc -c
