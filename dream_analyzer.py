import pandas as pd

dreams_df = pd.read_csv('enhanced_dreams.csv')

most_positive_index = dreams_df['sentiment'].idxmax()

dream_at_max_sentiment = dreams_df.loc[most_positive_index, ['date', 'content']]

print("Most positive dream: " + dream_at_max_sentiment)

most_negative_index = dreams_df['sentiment'].idxmin()

dream_at_min_sentiment = dreams_df.loc[most_negative_index, ['date', 'content']]

print("Most negative dream: ", dream_at_min_sentiment)

dream_count = len(dreams_df)

print(f"Number of dreams: {dream_count}")