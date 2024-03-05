#!/bin/bash
# takes a URL and displays HTTP methods the server accepts
curl -sI "$url" | grep -i "Allow" | tr -d '\r' | cut -d ' ' -f2
