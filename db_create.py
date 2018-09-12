import sqlite3
from _config import  DATABASE_PATH


with sqlite3.connect(DATABASE_PATH) as connection:
    # get the cursor object used to execute SQL commands
    cursor = connection.cursor()

    # create the table
    cursor.execute("""
    CREATE TABLE tasks
    (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    due_date TEXT NOT NULL,
    priority INTEGER NOT NULL,
    status INTEGER NOT NULL
    )""")

    # insert data into the table
    cursor.execute("INSERT INTO tasks (name, due_date, priority, status) VALUES ('Finish the tutorial', '12/09/2018', 10, 1)")

    cursor.execute("INSERT INTO tasks (name, due_date, priority, status) VALUES ('Finish Real Python Course', '30/09/2018', 10, 1)")

