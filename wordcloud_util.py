# wordcloud_utils.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    # Create a WordCloud object
    wordcloud = WordCloud(width=3200, height=3200, background_color='white').generate(text)

    # Display the word cloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
