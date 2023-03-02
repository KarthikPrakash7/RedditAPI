import praw
import json

reddit = praw.Reddit(client_id='nb3VtwmfQQn3J-LDko4WCg',
                     client_secret='bDO6b_86XP7E94p7-8eTJCwml_s8gA',
                     username='MaybeDeveloper100',
                     password='cookieshaha',
                     user_agent='search_reddit')

subreddits = ['AskReddit', 'worldnews', 'technology']  # List of subreddits to search
keywords = ['air', 'pollution', 'environment', 'dust', 'smog', 'soot', 'acid rain','gas pollution', 'CO2', 'NO2', 'carbon dioxide', 'nitrogen dioxide', 'fog', 'smoke', 'haze']

# Initialize the list of dictionaries
data = []

# Loop through each subreddit and search for posts with the keywords
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.search(' '.join(keywords), limit=10):
        # Add a dictionary for the post details to the list
        post_dict = {
            'title': post.title,
            'comments': []
        }

        # Load all the comments
        post.comments.replace_more(limit=None)

        # Loop through the comments of the post and add a dictionary for each comment to the list
        for comment in post.comments:
            post_dict['comments'].append({
                'comment_text': comment.body if isinstance(comment, praw.models.Comment) else "[deleted]"
            })

        # Add the post dictionary to the data list
        data.append(post_dict)

# Save the data to a JSON file
with open('reddit_comments.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)
