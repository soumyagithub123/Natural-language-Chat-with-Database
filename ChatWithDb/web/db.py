import sqlite3
import pandas as pd

def connect_db(db_name="sample.db"):
    conn = sqlite3.connect(db_name, check_same_thread=False)
    return conn

def execute_query(conn, query):
    try:
        query = query.strip()
        if not query:
            return "⚠ Empty query"
        if query.lower().startswith("select"):
            df = pd.read_sql_query(query, conn)
            return df
        else:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return f"✅ {cursor.rowcount} row(s) affected."
    except Exception as e:
        return f"⚠ Error: {e}"

def get_schema_info(conn):
    schema = {}
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [t[0] for t in cursor.fetchall()]
    for t in tables:
        cursor.execute(f"PRAGMA table_info({t});")
        schema[t] = [r[1] for r in cursor.fetchall()]
    return schema
