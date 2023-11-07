#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit: str) -> int:
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: Number of subscribers, or 0 for invalid subreddits or API errors.
    """
    try:
        response = requests.get(f'http://www.reddit.com/r/{subreddit}/about.json',
                                headers={'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)'})

        # Raise an exception for bad response status codes
        response.raise_for_status()

        data = response.json().get("data", {})
        subscribers = data.get("subscribers", 0)
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return 0
