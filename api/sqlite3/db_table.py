import sqlite3

create_table = """
CREATE TABLE IF NOT EXISTS music (
id INTEGER PRIMARY KEY AUTOINCREMENT,
reght_answer TEXT NOT NULL,
wrong_answesrs TEXT NOT NULL
);
"""

connect = sqlite3.connect("DATABASE.db")
cursor = connect.cursor()

cursor.execute(create_table)
connect.commit()

