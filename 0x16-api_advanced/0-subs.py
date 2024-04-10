#!/usr/bin/python3
"""
this module is used to query the Reddit API in order to retrieve
subscriber count for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of total subscribers of a subreddit
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://wwww.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('sunscribers')
    else:
        return 0
