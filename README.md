# Meeting Summarizer Bot

A web app that summarizes meeting recordings using Google's Gemini API.

## Features
- Upload audio/video meeting files.
- Extract key points and action items using LLM.
- Store summaries in SQLite.

## Setup

```bash
git clone https://github.com/Asish8880/meeting-summarizer-bot.git
cd meeting-summarizer-bot
pip install -r requirements.txt
export GOOGLE_API_KEY=your_gemini_key
python run.py
