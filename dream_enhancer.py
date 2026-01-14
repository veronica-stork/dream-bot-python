import pandas as pd
from textblob import TextBlob

# Read the new dream CSV
dreams_df = pd.read_csv('dreams.csv')

# Convert the date column to datetime format
dreams_df['date'] = pd.to_datetime(dreams_df['date'], format='mixed')

# Calculate the length of the dreams in words
dreams_df['word_count'] = dreams_df['content'].str.split().str.len()

# Analyze the sentiment of the dream
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

dreams_df['sentiment'] = dreams_df['content'].apply(analyze_sentiment)

# Save it as a new enhanced CSV file
dreams_df.to_csv('enhanced_dreams.csv', index=False)
