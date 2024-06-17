import sqlite3

# This will create a new SQLite database file named `diagdb` in the specified directory if it doesn't exist.
conn = sqlite3.connect('C:\\Users\\Student\\Desktop\\TroubleShooter\\project_directory\\server\\database\\database_dev.sqlite')

# Don't forget to close the connection when you're done.
conn.close()