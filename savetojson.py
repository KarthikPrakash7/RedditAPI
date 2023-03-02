import praw
import csv
import json

def search_subreddits(subreddits, keywords):
    reddit = praw.Reddit(client_id='nb3VtwmfQQn3J-LDko4WCg',
                     client_secret='bDO6b_86XP7E94p7-8eTJCwml_s8gA',
                     username='MaybeDeveloper100',
                     password='cookieshaha',
                     user_agent='search_reddit')
    comments = []
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.top(time_filter='all'):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                for keyword in keywords:
                    if keyword in comment.body:
                        comments.append({subreddit_name, keyword, comment.body})
    return comments

def save_comments(comments):
    fieldnames = ['subreddit name', 'keyword', 'body']
    comments1 = [{k: list(v) if isinstance(v, set) else v for k, v in comments.data()} for comment in comments]
    with open('test1.json', 'w', encoding='utf-8') as jsonfile:
        data = {'fieldnames': fieldnames, 'comments': comments1}
        json.dump(data, jsonfile, indent=4)

subreddits = ['airpollution', 'sustainability', 'europe']
keywords = ['air', 'pollution', 'environment', 'dust', 'smog', 'soot', 'acid rain','gas pollution', 'CO2', 'NO2', 'carbon dioxide', 'nitrogen dioxide', 'fog', 'smoke', 'haze']
comments = search_subreddits(subreddits, keywords)
save_comments(comments)