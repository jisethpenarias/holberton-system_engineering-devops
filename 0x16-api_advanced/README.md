<h1 class="gap">0x16. API advanced</h1>

<article id="description" class="gap formatted-content">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png" alt="" style=""></p>

<h2>Background Context</h2>

<p>Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.</p>

<p>A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.</p>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/QgcmfOXHHyyRcSQvgngOgg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to read API documentation to find the endpoints you’re looking for</li>
<li>How to use an API with pagination</li>
<li>How to parse JSON results from an API</li>
<li>How to make a recursive API call</li>
<li>How to sort a dictionary by value</li>
</ul>

 <h4 class="task">
    0. How many subs?
  </h4>

<!-- Task Body -->
  <p>Write a function that queries the <a href="/rltoken/odMvR9obKnQCx5EaM6_YFA" title="Reddit API" target="_blank">Reddit API</a> and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.</p>

<p>Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def number_of_subscribers(subreddit)</code></li>
<li>If not a valid subreddit, return 0.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

<pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) &lt; 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
</code></pre>


 <h4 class="task">
    1. Top Ten
  </h4>

<!-- Task Body -->
  <p>Write a function that queries the <a href="/rltoken/odMvR9obKnQCx5EaM6_YFA" title="Reddit API" target="_blank">Reddit API</a> and prints the titles of the first 10 hot posts listed for a given subreddit.</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def top_ten(subreddit)</code></li>
<li>If not a valid subreddit, print None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

<pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 1-main.py
#!/usr/bin/python3
"""
1-main
"""
import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) &lt; 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py this_is_a_fake_subreddit
None
wintermancer@lapbox ~/reddit_api/project $ 
</code></pre>

  <h4 class="task">
    2. Recurse it!
  </h4>

<!-- Task Body -->
  <p>Write a <em>recursive function</em> that queries the <a href="/rltoken/odMvR9obKnQCx5EaM6_YFA" title="Reddit API" target="_blank">Reddit API</a> and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.</p>

<p>Hint: The Reddit API uses pagination for separating pages of responses.</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def recurse(subreddit, hot_list=[])</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.</li>
<li>If not a valid subreddit, return None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

<p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>

<pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 2-main.py
#!/usr/bin/python3
"""
2-main
"""
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) &lt; 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py programming
932
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py this_is_a_fake_subreddit
None
</code></pre>
