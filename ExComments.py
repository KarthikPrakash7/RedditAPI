import praw
import csv

keywords = ['air', 'pollution', 'environment', 'dust', 'smog', 'soot', 'acid rain','gas pollution', 'CO2', 'NO2', 'carbon dioxide', 'nitrogen dioxide', 'fog', 'smoke', 'haze']  # Get keywords from user


reddit = praw.Reddit(client_id='nb3VtwmfQQn3J-LDko4WCg',
                     client_secret='bDO6b_86XP7E94p7-8eTJCwml_s8gA',
                     username='MaybeDeveloper100',
                     password='cookieshaha',
                     user_agent='search_reddit')


subreddit_list = ['airpollution', 'sustainability', 'europe']


comments_list = []


for subreddit_name in subreddit_list:
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.top(time_filter='all'):
        submission.comments.replace_more(limit=0)
        for comment in subreddit.comments():
            if any(keyword in comment.body.lower() for keyword in keywords):
                comments_list.append([comment.id, comment.body])
            # elif isinstance(comment, praw.models.MoreComments):
            #     for more_comments in comment.comments():
            #         if any(keyword in more_comments.body.lower() for keyword in keywords):
            #             comments_list.append([more_comments.id, more_comments.body])
        
    print(f"Finished extracting comments from r/{subreddit_name}")
        
with open('outputmaybe.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Comment id', 'Comment Body'])
    for comment in comments_list:
        writer.writerow(comment)
