#!/usr/bin/python3
"""
takes in a URL, sends a request and displays the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    req = urllib.request.Requst('{}'.format(url))

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
