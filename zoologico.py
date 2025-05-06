import sqlite3

conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

with open('tabelas.sql', 'r') as f:
    script = f.read()

cursor.executescript(script)
conn.commit()