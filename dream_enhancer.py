import pandas as pd
from textblob import TextBlob

# Read the new dream CSV
dreams_df = pd.read_csv('dreams.csv')

# Read the "lifeline" CSV (Life events) 
lifeline_df = pd.read_csv('lifeline.csv')

# Convert the date column to datetime format
dreams_df['date'] = pd.to_datetime(dreams_df['date'], format='mixed')

# Add a year column
dreams_df['year'] = dreams_df['date'].dt.year

# Calculate the length of the dreams in words
dreams_df['word_count'] = dreams_df['content'].str.split().str.len()

# Analyze the sentiment of the dream
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

dreams_df['sentiment'] = dreams_df['content'].apply(analyze_sentiment)

# Merge life events with dreams
merged_df = pd.merge(dreams_df, lifeline_df, on='year', how='left')

# if no major event noted, fill with default string
merged_df['event'] = merged_df['event'].fillna("Nothing crazy happened")

# Save it as a new enhanced CSV file
merged_df.to_csv('enhanced_dreams.csv', index=False)
