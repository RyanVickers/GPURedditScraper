import praw
from win10toast import ToastNotifier
import time
import config

# Calling Praw Api
reddit_read_only = praw.Reddit(client_id=config.client_key,  # Client Id
                               client_secret=config.secret_key,  # Client Secret
                               user_agent=config.user_key)  # User Agent
# Subreddit Name
subreddit_name = "bapcsalescanada"
# Getting Read Only Subreddit
subreddit = reddit_read_only.subreddit(subreddit_name)
# Set to Store previous posts
previous_posts = set()

while True:
    # Checking for posts in subreddit
    for post in subreddit.new(limit=1):
        # Checking if post is new
        if post.title not in previous_posts:
            # Add to Previous Posts Set
            previous_posts.add(post.title)
            # Creating Windows Notification
            toast = ToastNotifier()
            toast.show_toast(
                "GPU Alert",
                post.title,
            )
            print(post.title + " Url: " + post.url)
            # Stop Checking for 60 Seconds
            time.sleep(60)
