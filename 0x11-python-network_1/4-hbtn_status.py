#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    res = r.text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
