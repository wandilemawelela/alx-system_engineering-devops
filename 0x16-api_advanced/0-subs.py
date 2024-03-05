#!/usr/bin/python3
"""
Number of subscribers module.
"""

import requests


def number_of_subscribers(subreddit):
    """ Uses the Reddit API to find the number of subs from a sub reddit. """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
