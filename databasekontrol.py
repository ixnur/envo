import sqlite3

database_name = 'db.sqlite3'
connection = sqlite3.connect(database_name)
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"\nTable: {table_name}\n{'=' * 20}")
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    print("Columns:")
    for column in columns:
        print(f"  {column[1]} - {column[2]} - {column[3]} - {column[4]}")#column0?
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    print("\nData:")
    for row in rows:
        print(row)
connection.close()
