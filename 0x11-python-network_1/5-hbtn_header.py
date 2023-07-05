#!/usr/bin/python3
"""
takes in a URL, sends a request and displays X-Request-Id in the response
"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    print(type(response.headers).get('X-Request-Id'))
