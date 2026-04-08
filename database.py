import sqlite3

conn = sqlite3.connect("assistant.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    date TEXT,
    time TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    deadline TEXT
)
""")

conn.commit()

def add_event(title, date, time):
    cursor.execute("INSERT INTO events (title, date, time) VALUES (?, ?, ?)", (title, date, time))
    conn.commit()

def add_task(task, deadline):
    cursor.execute("INSERT INTO tasks (task, deadline) VALUES (?, ?)", (task, deadline))
    conn.commit()