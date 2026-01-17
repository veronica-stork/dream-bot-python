import json
import pandas as pd

dreams_df = pd.read_csv('enhanced_dreams.csv')


with open("training_data.jsonl", "w") as f:
    for index, row in dreams_df.iterrows():
        data = {
            "messages": [
                {"role": "system", "content": "You are a dream-writing bot that mimics Veronica's subconscious voice."},
                {"role": "user", "content": f"Write a dream from {row['year']}."},
                {"role": "assistant", "content": row['content']}
            ]
        }
        f.write(json.dumps(data) + "\n")