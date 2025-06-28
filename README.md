# AI Chat Log Summarizer

This project reads a `.txt` file containing a conversation between a User and an AI, analyzes it and produces a simple summary.

## Features
- Parses chat log by speakers (User Vs AI).
- Counts total messages and per-speaker messages.
- Extracts most common keywords (excluding stopwords).
- Outputs a simple summary of the conversation.

## How to Run

1. Place your chat log file in the project root folder and make sure your chat log is saved as `chat.txt`.
2. Install NLTK (if not installed yet):
   ```
   pip install nltk
   ```
3. Download stopwords (only needed to run once):
   ```
   import nltk
   nltk.download('stopwords')
   ```
   Or run  ``` nltk_download_features.py ``` provided.
  
5. Run the script:
```
python chat_summarizer.py
```
