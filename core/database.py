import sqlite3
from datetime import datetime

DB_NAME = "aurasync.db"

def init_db():
    """Initializes the SQLite database and creates the sessions table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_date TEXT,
            duration_seconds REAL,
            total_frames INTEGER,
            fatigue_alerts INTEGER,
            bad_posture_count INTEGER,
            overall_focus_score TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_session_to_db(report_data):
    """Saves completed session telemetry into the SQLite database."""
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sessions (session_date, duration_seconds, total_frames, fatigue_alerts, bad_posture_count, overall_focus_score)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        report_data['session_date'],
        report_data['duration_seconds'],
        report_data['total_frames_monitored'],
        report_data['fatigue_alerts_count'],
        report_data['bad_posture_count'],
        report_data['overall_focus_score']
    ))
    conn.commit()
    conn.close()
    print("[DATABASE] Session successfully logged to SQLite database!")

def fetch_all_sessions():
    """Retrieves all past session records for historical dashboard analytics."""
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT session_date, duration_seconds, overall_focus_score, fatigue_alerts, bad_posture_count FROM sessions ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows