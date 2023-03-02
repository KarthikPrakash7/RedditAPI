import pandas as pd
import nltk
# import wordcloud
# from wordcloud import WordCloud as WC
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
from PIL import Image
import chardet
from wordcloud_util import generate_wordcloud

nltk.download('stopwords')
# Read the comments from the CSV file
with open('outputmaybe.csv', 'rb') as f:
    result = chardet.detect(f.read())
encoding = result['encoding']
comments_df = pd.read_csv('outputmaybe.csv', encoding=encoding)

# Preprocess the comments
stop_words = set(stopwords.words('english'))
def preprocess(comment):
    # Convert the comment to lowercase
    comment = comment.lower()
    # Remove punctuation
    comment = comment.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the comment
    tokens = word_tokenize(comment)
    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]
    # Join the tokens back into a string
    comment = ' '.join(tokens)
    return comment

comments_df['Comment Body'] = comments_df['Comment Body'].apply(preprocess)

# Combine all comments into a single string
all_comments = ' '.join(comments_df['Comment Body'])

# Generate a word cloud
# mask = np.array(Image.open("cloud.png")) # optional mask for the wordcloud
wc= generate_wordcloud(all_comments)

# Plot the word cloud
plt.figure(figsize=(8,8))
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('wordcloud.png')