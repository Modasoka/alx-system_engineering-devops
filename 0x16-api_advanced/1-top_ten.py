#!/usr/bin/python3
"""
this module is used to print the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Retrieves the top 10 hot posts of a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:myserver:v5.11.0 (by /u/linda)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data")
    children = data.get("children")
    for i in range(10):
        print(children[i].get("data").get("title"))
