#!/usr/bin/python3
"""
Function to retrieve and display the 10 most recent
commits of a repository by a given owner
"""

import requests
import sys


def get_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()

    if response.status_code != 200:
        print(f"Error: {commits['message']}")
        return

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repo, owner)
