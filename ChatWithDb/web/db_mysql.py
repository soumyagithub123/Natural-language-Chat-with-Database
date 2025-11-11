import mysql.connector
import pandas as pd

def connect_server(host, user, password):
    """Connect without selecting DB (for SHOW DATABASES)"""
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    return conn

def connect_db(host, user, password, database):
    """Connect to specific DB"""
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conn

def get_databases(conn):
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES;")
    return [db[0] for db in cursor.fetchall()]

def get_schema_info(conn):
    schema = {}
    # ✅ buffered=True fixes “Unread result found”
    cursor = conn.cursor(buffered=True)

    cursor.execute("SHOW TABLES;")
    tables = [t[0] for t in cursor.fetchall()]

    for t in tables:
        cursor.execute(f"DESCRIBE {t}")
        columns = [row[0] for row in cursor.fetchall()]
        schema[t] = columns

    cursor.close()
    return schema


def execute_query(conn, query):
    try:
        cursor = conn.cursor(dictionary=True, buffered=True)
        cursor.execute(query)

        # ✅ Always try to fetch results (even for DESCRIBE, SHOW, etc.)
        try:
            result = cursor.fetchall()
            if result:
                cursor.close()
                return pd.DataFrame(result)
        except:
            # Some queries don’t return rows
            pass

        # ✅ Commit for write queries
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        return f"✅ {affected} row(s) affected."
    except Exception as e:
        return f"⚠ Error: {e}"
