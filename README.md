# 🧠 Meeting Summarizer Bot

A Flask-based web application that summarizes meeting recordings (audio/video) using Google's Gemini API. It extracts **key points** and **action items**, saves the results in a database, and provides a simple UI for users to interact with.

---

## 🚀 Features

- Upload audio/video meeting files.
- Extract **key points** and **action items** using Gemini (Google) LLM.
- Store summaries in a SQLite database.
- Simple HTML/CSS/JavaScript frontend.
- REST API endpoints for file handling and summarization.
- Ready for deployment on platforms like Render or Heroku.

---


## 🧩 Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Frontend     | HTML, CSS, JavaScript |
| Backend      | Python, Flask     |
| AI/LLM       | Gemini API (Google AI) |
| Database     | SQLite            |
| Deployment   | Render / Heroku   |

---


## Setup

```bash
git clone https://github.com/Asish8880/meeting-summarizer-bot.git
cd meeting-summarizer-bot
pip install -r requirements.txt
export GOOGLE_API_KEY=your_gemini_key (Add your Gemini API key in app/gemini_api.py)
python run.py
