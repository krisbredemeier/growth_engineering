import praw
import time
import smtplib


#import creds
USERAGENT = 'holberton keyword search by /u/school_bot'
USERNAME = 'school_bot'
PASSWORD = 'holberton'

SUBREDDIT_TITLE = "test"
MAXPOSTS = 10
REPLY = 'truth'

SENDER_EMAIL = 'myschoolbot@gmail.com'
RECIPIENT_EMAIL = ['kris.bredemeier@holbertonschool.com']


r = praw.Reddit(user_agent= USERAGENT)
r.login(USERNAME, PASSWORD)

words_to_match = ['getting better at python programming']
cache = []

def run_bot():
    print("Grabbing subreddit...")
    subreddit = r.get_subreddit(SUBREDDIT_TITLE)
    print("Grabbing comments...")
    comments = subreddit.get_comments(limit= MAXPOSTS)
    # message = subreddit.get_message(limit= MAXPOSTS)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print("Match found! comment ID: " + comment.id)
            comment.reply(REPLY)
            print("Reply successful!")
            cache.append(comment.id)
    print("Comments loop finished, time to sleep")

def send_email():
    content = 'test' #url of reddit post that has our keyword in it
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(SENDER_EMAIL, PASSWORD)
    mail.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, content)
    mail.close

while True:
    run_bot()
    send_email()
    time.sleep(10)

# KEYWORDS ['CS']
# SUBREDDITS ['technology', 'software engineering', 'career questions']
# FLAIR ['software']
