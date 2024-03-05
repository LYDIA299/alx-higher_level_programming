#!/bin/bash
# takes a URL and displays HTTP methods the server accepts
curl -s "$1" | grep -i "Allow" | cut -d " " -f 2
