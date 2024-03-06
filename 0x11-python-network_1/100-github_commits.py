#!/usr/bin/python3
""" lists 10 commits (from the most recent to oldest) of the repository “rails”
by the user “rails”
"""

if __name == '__main__':
    import sys
    import requests

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
