#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
"""


if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    val = {'q': ""}
    if sys.argv[1]:
        val['q'] = sys.argv[1]
    r = requests.post(url, data=val)
    try:
        response = r.json()
        if response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), reponse.get('name')))
    except ValueError:
        print('Not a valid JSON')
