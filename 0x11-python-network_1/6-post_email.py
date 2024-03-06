#!/usr/bin/python3
"""
- takesin a URL and an email
- sends a POST request to it with email as parameter
- displays the body of the response(decoded in utf-8)
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    r = requests.post(url, data=values)
    print(r.text)
