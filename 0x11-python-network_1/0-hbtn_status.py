#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status using urllib
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode('utf-8')))
