# Reddit API Python Project

This project focuses on utilizing the Reddit API to perform various tasks using Python. The tasks involve querying the Reddit API, parsing JSON responses, and implementing recursive functions to achieve specific objectives related to subreddits and their posts. The goal is to enhance your understanding of API calls, pagination, JSON parsing, and recursive functions, which are crucial skills for interviews and real-world applications.

## Project Structure

The project is organized into several Python scripts, each addressing a specific task:

- **`0-subs.py`**: Queries the Reddit API to retrieve the number of subscribers for a given subreddit.
- **`1-top_ten.py`**: Queries the Reddit API to print the titles of the first 10 hot posts for a given subreddit.
- **`2-recurse.py`**: Implements a recursive function to retrieve all hot articles' titles for a given subreddit.
- **`100-count.py`**: Uses a recursive function to count the occurrences of specified keywords in hot article titles for a given subreddit.

## Project Tasks

### 0. How many subs?

This task involves querying the Reddit API to retrieve the number of subscribers for a given subreddit. The function `number_of_subscribers(subreddit)` accomplishes this by making a GET request to the subreddit's API endpoint and parsing the JSON response to extract the subscriber count.

### 1. Top Ten

This task requires querying the Reddit API to print the titles of the first 10 hot posts for a given subreddit. The function `top_ten(subreddit)` achieves this by making a GET request to the subreddit's API endpoint with a limit parameter set to 10, ensuring only the top 10 posts are retrieved and their titles are printed.

### 2. Recurse it!

In this task, a recursive function, `recurse(subreddit, hot_list=[], after=None)`, is implemented to retrieve all hot articles' titles for a given subreddit. The Reddit API uses pagination, and the function utilizes recursion to handle multiple pages of responses, appending the titles to the `hot_list` until all posts are retrieved.

### 3. Count it!

This advanced task involves querying the Reddit API recursively, parsing hot article titles, and counting the occurrences of specified keywords. The function `count_words(subreddit, word_list, after=None, counts={})` uses recursion to handle pagination and keeps track of keyword occurrences in hot article titles. The results are then sorted by count in descending order, and if counts are equal, the keywords are sorted alphabetically.

## How to Run the Scripts

To run the scripts, use the following format in the terminal:

```bash
python3 <script_name>.py <subreddit> <additional_arguments>
```

Replace `<script_name>` with the name of the Python script you want to execute and provide the required arguments as described in the specific task instructions.

## Prerequisites

- Python 3.x
- Requests module (install using `pip install requests` if not already installed)

## Notes

- Ensure you have a stable internet connection to make API calls.
- Handle potential errors gracefully, such as invalid subreddits or API rate limits, to prevent unexpected behavior.
- Follow the specified naming conventions, coding style, and project structure to maintain consistency and readability.
