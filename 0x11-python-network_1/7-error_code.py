#!/usr/bin/python3
"""
- takes in a URL
- sends request to it
- displays the response body(decoded in utf-8)
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    s = r.status_code
    if (s >= 400):
        print("Error code: {}".format(s))
    else:
        print(r.text)
