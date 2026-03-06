import sqlite3

conn = sqlite3.connect("AnimalKingdom.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT
)
""")

cursor.execute("INSERT INTO Animals (name, type) VALUES ('Лев', 'Ссавець')")
cursor.execute("INSERT INTO Animals (name, type) VALUES ('Крокодил', 'Плазун')")
cursor.execute("INSERT INTO Animals (name, type) VALUES ('Орел', 'Птах')")
cursor.execute("INSERT INTO Animals (name, type) VALUES ('Морська черепаха', 'Плазун')")
cursor.execute("INSERT INTO Animals (name, type) VALUES ('Мавпа', 'Ссавець')")

cursor.execute("UPDATE Animals SET name='Сокіл' WHERE name='Орел'")

cursor.execute("SELECT * FROM Animals WHERE type='Ссавець'")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Animals")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()