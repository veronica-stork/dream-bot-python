from docx import Document
import re
import pandas as pd

# Load in the dreams
document = Document('Dreams_to_2025.docx')

# Create list to hold the dreams
dreams = []

# Create variable to hold current dream
current_dream = None

# RegEx pattern to identify dates
date_pattern = r'\d{1,2}/\d{1,2}/\d{2,4}'

# Filters out headings
def is_heading(para):
    return para.style.name.startswith('Heading')

# Loop through each paragraph in the document
for para in document.paragraphs:
    text = para.text.strip()
    if not text or is_heading(para):
        continue  # Skip empty paragraphs

    # If that paragraph starts with a date, start a new dream
    if re.search("^" + date_pattern, para.text):
        # If there's already a dream in the hopper, stick it in the dreams list
        if current_dream is not None:
            dreams.append(current_dream)
        # Start a new dream
        match = re.search(date_pattern, text)
        found_date = match.group()
        remaining_text = text[match.end():].strip("- ")
        current_dream = {
            "date": found_date,
            "content": remaining_text + "\n"
        }
        # Otherwise, keep adding to the current dream
    else:
        if current_dream is not None:
            current_dream["content"] += text + "\n"
        else:
            print(f"Skipping intro text: {text[:30]}...")
if current_dream:
    dreams.append(current_dream)

# Convert the list of dreams to a DataFrame
dreams_df = pd.DataFrame(dreams)

dreams_df['content'] = dreams_df['content'].str.strip()

#Save the DataFrame to a CSV file
dreams_df.to_csv('dreams.csv', index=False)

print("Dreams have been successfully extracted and saved to dreams.csv")