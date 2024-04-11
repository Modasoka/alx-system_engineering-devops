#!/usr/bin/python3
"""
this module is used to query the Reddit API in order to retrieve
subscriber count for a given subreddit
"""


def number_of_subscribers(subreddit):
    """
    Retrieves the number of total subscribers of a subreddit
    """
    # headers = {'User-Agent': 'Mozilla/5.0'}
    # url = f'https://wwww.reddit.com/r/{subreddit}/about.json'
    # response = requests.get(url, headers=headers)

    # if response.status_code == 200:
    #     data = response.json()
    #     return data.get('data').get('sunscribers')
    # else:
    #     return 0
    import requests
    
    info_subreddit = requests.get("https://www.reddit.com/r/{}/about.json"
                                  .format(subreddit),
                                  headers={"User-Agent": "My-User-Agent"},
                                  allow_redirects=False)
    
    if info_subreddit.status_code >= 300:
        return 0
    
    return info_subreddit.json().get("data").get("subscribers")
