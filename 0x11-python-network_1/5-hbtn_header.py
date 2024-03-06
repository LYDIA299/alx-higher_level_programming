#!/usr/bin/python3
"""
- takes in URL
- sends request to it
- displays the X-Request-Id in response header
"""

if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1]).headers
    print(r.get('X-Request-Id'))
