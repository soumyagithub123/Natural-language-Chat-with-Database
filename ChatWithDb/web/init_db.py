import sqlite3

def init(db_path="sample.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        age INTEGER
    );
    """)

    cur.executemany("INSERT OR IGNORE INTO users (id, name, email, age) VALUES (?, ?, ?, ?)", [
        (1, "Alice", "alice@example.com", 30),
        (2, "Bob", "bob@example.com", 25),
        (3, "Charlie", "charlie@example.com", 35)
    ])
    conn.commit()
    conn.close()
    print("✅ Sample DB initialized")

if __name__ == "__main__":
    init()
