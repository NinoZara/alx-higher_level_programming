#!/usr/bin/python3
"""A Python script that fetches
https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        r = requests.post(url, data={'q': q})
        json_obj = r.json()
        if not bool(json_obj):
            print('No result')
        else:
            print('[{}] {}'.format(json_obj['id'], json_obj['name']))
    except ValueError:
        print('Not a valid JSON')
