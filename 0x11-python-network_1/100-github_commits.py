#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge:
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(owner_name, repo_name))
    json = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(json[i].get('sha'), json[i].get('commit')
                                  .get('author').get('name')))
    except IndexError:
        pass
