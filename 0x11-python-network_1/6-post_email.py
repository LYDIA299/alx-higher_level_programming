#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request, and displays the body
"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    val = {'email': sys.argv[2]}

    response = requests.post(url, data=val)
    print(response.text)
