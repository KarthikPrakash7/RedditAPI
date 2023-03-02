import praw
import csv
import json

reddit = praw.Reddit(client_id='nb3VtwmfQQn3J-LDko4WCg',
                     client_secret='bDO6b_86XP7E94p7-8eTJCwml_s8gA',
                     username='MaybeDeveloper100',
                     password='cookieshaha',
                     user_agent='search_reddit')

subreddits = ['airpollution', 'sustainability', 'europe']  # List of subreddits to search
keywords = ['air', 'pollution', 'environment', 'dust', 'smog', 'soot', 'acid rain','gas pollution', 'CO2', 'NO2', 'carbon dioxide', 'nitrogen dioxide', 'fog', 'smoke', 'haze']  # Get keywords from user

# Initialize the list of dictionaries
rows = []

# Loop through each subreddit and search for posts with the keywords
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.search(' '.join(keywords), limit=None):
        # Add a dictionary for the post details to the list
        rows.append({
            'Subreddit': subreddit_name,
            'Title': post.title,
            'Post Text': post.selftext,
            'comments': []
        })

#         # Loop through the comments of the post and add a dictionary for each comment to the list
#         for comment in post.comments:
#             rows.append({
#                 'Subreddit': subreddit_name,
#                 'Title': '',
#                 'Post Text': '',
#                 'Comment': comment.body
#             })

# # Open a CSV file to save the results
# with open('reddit_posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     # Define the header row of the CSV file
#     fieldnames = ['Subreddit', 'Title', 'Post Text', 'Comment']

#     # Create a CSV writer object and write the header row
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()

#     # Loop through the list of dictionaries and write each row to the CSV file
#     for row in rows:
#         writer.writerow(row)
# Loop through the comments of the post and add a dictionary for each comment to the list
        post.comments.replace_more(limit=None)
        for comment in post.comments:
            rows[-1]['comments'].append({
                'comment_text': comment.body if isinstance(comment, praw.models.Comment) else "[deleted]"
            })

# Save the data to a JSON file
with open('reddit_posts2.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(rows, jsonfile, indent=4)