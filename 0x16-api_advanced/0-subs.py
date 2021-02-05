#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0. """

import requests


def number_of_subscribers(subreddit):
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'Browser'}
    response = requests.get(url, headers=headers)
    # Error 404 Not Found
    if response.status_code == 404:
        return 0
    res_json = response.json()
    subs = res_json.get('data').get('subscribers')
    return subs
