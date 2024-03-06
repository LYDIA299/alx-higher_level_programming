#!/usr/bin/python3
"""
- takesin a URL and an email
- sends a POST request to it with email as parameter
- displays the body of the response(decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
