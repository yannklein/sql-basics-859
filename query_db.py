import sqlite3

conn = sqlite3.connect("data/database.sqlite")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM Country")
rows = cursor.fetchall()

for row in rows:
    print(f"{row['id']} - {row['name']}")

# cursor.execute("SELECT * FROM Country WHERE id = 7809")
# row = cursor.fetchone()

# print(dict(row))