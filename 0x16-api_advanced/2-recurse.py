#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None."""

import requests


def recurse(subreddit, hot_list=[], after=""):

    headers = {'User-Agent': "Browser"}
    # URL that is goin to be used for the request
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    response = requests.get(url, headers=headers)
    json_r = response.json()
    if response.status_code == 200:
        for post in json_r['data']['children']:
            hot_list.append(post['data']['title'])
        new_after = json_r['data']['after']
        if new_after is None:
            return hot_list
        return recurse(subreddit, hot_list, new_after)
    else:
        return None
