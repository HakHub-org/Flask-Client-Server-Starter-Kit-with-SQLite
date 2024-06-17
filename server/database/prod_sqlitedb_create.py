import sqlite3

# This will create a new SQLite database file named `database_test.sqlite` in the specified directory if it doesn't exist.
conn = sqlite3.connect('C:\\Users\\Student\\Desktop\\TroubleShooter\\project_directory\\server\\database\\database_prod.sqlite')

# Don't forget to close the connection when you're done.
conn.close()