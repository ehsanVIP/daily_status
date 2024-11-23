import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("daily_notebook.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute(
    """
CREATE TABLE users (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER NOT NULL,
      email TEXT NOT NULL
      date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
)

# Commit the changes and close the connection
conn.commit()
conn.close()
