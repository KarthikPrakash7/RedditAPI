import praw

def search_subreddits(subreddits, keywords):
    reddit = praw.Reddit(client_id='nb3VtwmfQQn3J-LDko4WCg',
                     client_secret='bDO6b_86XP7E94p7-8eTJCwml_s8gA',
                     username='MaybeDeveloper100',
                     password='cookieshaha',
                     user_agent='search_reddit')

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.hot(limit=10):
            for comment in submission.comments:
                for keyword in keywords:
                    if keyword in comment.body:
                        print(f'Comment containing keyword "{keyword}" found in r/{subreddit_name}:')
                        print(comment.body)

subreddits = ['airpollution', 'sustainability', 'europe']
keywords = ['air', 'pollution', 'environment', 'dust']
search_subreddits(subreddits, keywords)