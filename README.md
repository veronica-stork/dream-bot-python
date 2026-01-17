# Dream Bot: 20-Year Subconscious Archive Parser

A Python-based ETL pipeline that transforms over two decades of dream journals (2004–2025) into a structured, machine-readable dataset for AI/ML experimentation.

## Project Overview

This project was built to refresh my Python knowledge while preparing a personal dataset for Generative AI applications. It handles the extraction, cleaning, and enrichment of longitudinal text data stored in legacy .docx formats.

## Features

1. **Unstructured Data Extraction**: Custom parser using python-docx and Regular Expressions to identify dates and content boundaries.
2. **Data Normalization**: Converts varied date strings into ISO-standard datetime objects using Pandas.
3. **Feature Engineering (Data Enrichment)**: Automatically calculates word counts, extracts "Day of Week" patterns, and performs sentiment analysis using TextBlob. *(Coming Soon)*
4. **AI Readiness**: Exports data to a flattened CSV format optimized for Vector Database ingestion (RAG).

## Technical Stack

**Language**: Python 3.12.3  
**Libraries**: pandas, python-docx, textblob, re  
**Environment**: Virtual Environment (venv) with PEP 668 compliance.  

# Getting Started 

1. Clone the repo  
`git clone https://github.com/veronica-stork/dream-bot-python.git`

2. Set up the environment  
`python3 -m venv venv`  
`source venv/bin/activate`

3. Install dependencies  
`pip install -r requirements.txt`

4. Run the parser  
`python3 dream-bot.py`
