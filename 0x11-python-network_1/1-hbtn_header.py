#!/usr/bin/python3
""" takes in a URL, sends a request URL and displays the X-Request-Id """

if __name__ == '__main__':
    import sys
    import urllib.request

    req = urllib.request.Request('{}'.format(sys.argv[1]))
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
