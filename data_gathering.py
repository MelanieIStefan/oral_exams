import json
import praw
import requests
from praw.models import MoreComments
import pprint
import pandas as pd
import time

# set credentials and create reddit instance 

credentials = '/home/melanie/Documents/sandbox/reddit_api/client_secrets.json'
 

with open(credentials) as f:
    creds = json.load(f)


reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

reddit.read_only = True


def gather_data(subreddit, query):

    # create empty list of data to append to
    all_data = []

    # extract submissions and comments from a particular subreddit

    for submission in reddit.subreddit(subreddit).search(query=query,time_filter="all"):
        submission_data = [
            submission.id,
            "submission", 
            submission.author, 
            submission.created_utc, 
            submission.subreddit.display_name,
            submission.title,
            submission.selftext,
            "n/a",
            submission.url
            ]
        all_data.append(submission_data)
        
        # submission.comments.replace_more(limit=None)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            comment_data = [
                comment.id,
                "comment",
                comment.author,
                comment.created_utc,
                comment.subreddit.display_name,
                "n/a,",
                comment.body,
                comment.parent_id,
                "n/a",
            ] 
            all_data.append(comment_data)


    # turn list into data frame

    all_data_frame = pd.DataFrame(all_data)
    all_data_frame.columns = ["ID","Type", "Author", "Created", "Subreddit","Title","Body","Parent ID","url"]


    # save panda as .csv
    filename = "./"+subreddit+".csv"

    all_data_frame.to_csv(filename)
    print(subreddit+": "+str(len(all_data_frame.index)))
    oldest = min(all_data_frame["Created"])
    print(time.strftime("%D %H:%M", time.localtime(oldest)))


# gather_data(subreddit="medizin")

keywords = '"M1" OR "M3" OR "Physikum" OR "mündlich" OR "mündliche" OR "Prüfung" OR "Staatsexamen" OR "Prüfer" OR "Prüferin"' 


# gather_data(subreddit="medizin", query = keywords)
gather_data(subreddit="medizinstudium", query = keywords)


# Docs and Tutorials that helped me do all of this:
# https://www.jcchouinard.com/post-on-reddit-api-with-python-praw/
# https://praw.readthedocs.io/en/stable/tutorials/comments.
# https://tomvannuenen.medium.com/exploring-reddit-communities-with-python-part-1-introduction-4ce4836ad7ba
# https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-and-then-filling-it

