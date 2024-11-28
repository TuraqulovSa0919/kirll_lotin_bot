import sqlite3

conn = sqlite3.connect("user_datebase.db")
cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
            number INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name  text,
            username text,
            bio text,
            user_ID int
            )
            """)
conn.commit()

def insert_user(full_name, username, bio, user_ID):

    cur.execute("SELECT user_ID FROM users WHERE user_ID = ?", (user_ID,))
    check_id = cur.fetchone()
    if check_id:
        print(f"Foydalanuvchi {user_ID} allaqachon mavjud!")
    else:
        cur.execute("""INSERT INTO users(full_name, username, bio, user_ID) VALUES (?, ?, ?, ?) """, (full_name, username, bio, user_ID))
        conn.commit()
        




