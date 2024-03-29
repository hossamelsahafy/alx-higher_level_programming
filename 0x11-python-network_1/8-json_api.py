#!/usr/bin/python3
"""
script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json = r.json()
        if 'id' in json and 'name' in json:
            print("[{}] {}".format(json['id'], json['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
