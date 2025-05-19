import sqlite3

DB_NAME = "app.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS summaries (
                id INTEGER PRIMARY KEY,
                filename TEXT,
                summary TEXT,
                timestamp TEXT
            )
        ''')

def insert_summary(filename, summary):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO summaries (filename, summary, timestamp) VALUES (?, ?, datetime('now'))", (filename, summary))

def get_all_summaries():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT * FROM summaries").fetchall()
