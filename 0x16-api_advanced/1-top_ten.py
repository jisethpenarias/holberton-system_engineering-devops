#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit. """

import requests


def top_ten(subreddit):
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Browser'}
    response = requests.get(url, headers=headers, params={'limit': '10'})
    if response.status_code == 404:
        print("None")
        return 0
    res_json = response.json()
    post_child = res_json.get('data').get('children')
    for post in post_child:
        print(post['data']['title'])
