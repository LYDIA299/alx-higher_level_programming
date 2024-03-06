#!/usr/bin/python3
"""
- takes in a URL
- sends request to it
- displays the response body(decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        data = urllib.request.urlopen(req)
        print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
