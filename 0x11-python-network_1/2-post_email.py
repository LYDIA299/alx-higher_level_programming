#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request, and displays body """

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    val = {'email' : sys.argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
