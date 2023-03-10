import praw
import csv

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
    with open('test1.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['subreddit name', 'keyword', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for comment in comments:
            writer.writerow(fieldnames)
            writer.writerow(comment)
            # writer.writerow()
        # csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(fieldnames)
        # csvwriter.writerow(comments)
        # csvwriter.writerow('\n')

subreddits = ['airpollution', 'sustainability', 'europe']
keywords = ['air', 'pollution', 'environment', 'dust','air pollution', 'environmental pollution']
comments = search_subreddits(subreddits, keywords)
save_comments(comments)