import sqlite3
import pandas as pd

# Database Connection
con = sqlite3.connect("events.db", check_same_thread=False)
cur = con.cursor()

# Create Table
cur.execute('''CREATE TABLE IF NOT EXISTS events (
    Event_ID INTEGER PRIMARY KEY,
    Event_Name TEXT,
    Organizer TEXT,
    Event_Type TEXT,
    Budget REAL,
    Event_Date TEXT
)''')
con.commit()


def get_events():
    return pd.read_sql_query("SELECT * FROM events", con)


def add_event(eid, name, organizer, etype, budget, date):
    cur.execute(
        "INSERT INTO events VALUES (?, ?, ?, ?, ?, ?)",
        (eid, name, organizer, etype, budget, date),
    )
    con.commit()


def delete_event(eid):
    cur.execute("DELETE FROM events WHERE Event_ID = ?", (eid,))
    con.commit()
    return cur.rowcount


def update_event(eid, field, new_value):
    cur.execute(
        f"UPDATE events SET {field} = ? WHERE Event_ID = ?",
        (new_value, eid)
    )
    con.commit()
    return cur.rowcount
