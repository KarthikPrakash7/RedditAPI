import praw
import pandas as pd

reddit = praw.Reddit(client_id='nb3VtwmfQQn3J-LDko4WCg',
                     client_secret='bDO6b_86XP7E94p7-8eTJCwml_s8gA',
                     username='MaybeDeveloper100',
                     password='cookieshaha',
                     user_agent='scrape_reddit'
                     )

subreddit = reddit.subreddit('airpollution')

# for comment in subreddit.stream.comments():
#     try:
#         parent_id = str(comment.parent())
#         original = reddit.comment(parent_id)
#         print('Parent:')
#         print(original.body)
#         print('Reply:')
#         print(comment.body)
#     except praw.exceptions.PRAWException as e:
#         pass

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
topics_data = pd.DataFrame(topics_dict)

csv_data = topics_data.to_csv('pollutiondata.csv', index=True)
print('\nCSV String:\n', csv_data)