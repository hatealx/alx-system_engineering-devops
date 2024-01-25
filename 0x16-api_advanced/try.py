"""Function to query subscribers on a given Reddit subreddit."""
import requests
import json


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = json.load(response).get("data")
    return results.get("subscribers")



sub = number_of_subscribers("movies")
print(sub)
