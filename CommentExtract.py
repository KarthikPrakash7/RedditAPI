import praw

reddit = praw.Reddit(client_id='nb3VtwmfQQn3J-LDko4WCg',
                     client_secret='bDO6b_86XP7E94p7-8eTJCwml_s8gA',
                     username='MaybeDeveloper100',
                     password='cookieshaha',
                     user_agent='scrape_reddit'
                     )

subreddit = reddit.subreddit('air pollution')

for comment in subreddit.stream.comments():
    try:
        parent_id = str(comment.parent())
        original = reddit.comment(parent_id)
        print('Parent:')
        print(original.body)
        print('Reply:')
        print(comment.body)
    except praw.exceptions.PRAWException as e:
        pass
