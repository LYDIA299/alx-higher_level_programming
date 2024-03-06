#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status

import requests

if __name__ == '__main__':

    r = requests.get('https://alx-intranet.hbtn.io/status')
    content = r
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(r))
