import sqlite3
from datetime import datetime

DB_NAME = "business.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        issue TEXT,
        created_at TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        time TEXT,
        reason TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_customer(name, email, issue):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, email, issue, created_at) VALUES (?, ?, ?, ?)",
        (name, email, issue, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()
    return "Customer saved successfully."

def add_appointment(name, date, time, reason):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO appointments (name, date, time, reason, created_at) VALUES (?, ?, ?, ?, ?)",
        (name, date, time, reason, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()
    return "Appointment booked successfully."

def get_customers():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, issue, created_at FROM customers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_appointments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, date, time, reason, created_at FROM appointments")
    rows = cursor.fetchall()
    conn.close()
    return rows