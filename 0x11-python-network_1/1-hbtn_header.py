#!/usr/bin/python3
"""
- Takes in a URL
- sends a request to the URL
- displays the value of the X-Request-Id variable found in the header of the response"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
