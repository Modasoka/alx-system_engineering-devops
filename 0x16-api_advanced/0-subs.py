#!/usr/bin/python3
"""
this module is used to retrieve subscriber count for a subreddit
"""
import requests
import json

def number_of_subscribers(subreddit):
    """
    Retrieves the number of total subscribers of a subreddit
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://wwww.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
    
    data = response.json()
    return data.get("data").get("subscribers")
