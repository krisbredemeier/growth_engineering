import praw
import time

r = praw.Reddit(user_agent= "holberton keyword search bot by kris bredemeier")
r.login()

words_to_match = ['yo', 'tap']
cache = []

def run_bot():
    print("Grabbing subreddit...")
    subreddit = r.get_subreddit("funny")
    print("Grabbing comments...")
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print("Match found! comment ID: " + comment.id)
            comment.reply('test')
            print("Reply successful!")
            cache.append(comment.id)
    print("Comments loop finished, time to sleep")

while True:
    run_bot()
    time.sleep(10)


# [Holberton School](https://www.holbertonschool.com)
