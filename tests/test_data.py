from src.db.db_utils import *

def rebuild_test_tables():
    # Connect to the default database
    conn = connect()
    cur = conn.cursor()

    # Create a new test database
    cur.execute("CREATE DATABASE test_db;")
    conn.commit()

    # Close the connection to the default database
    cur.close()
    conn.close()

    # Modify the connect function in db_utils.py to connect to the test database
    # You can do this by adding a `dbname` parameter to the function, and passing 'test_db' when you call it here
    conn = connect(dbname='test_db')
    cur = conn.cursor()

    # Execute the SQL files on the test database
    exec_sql_file('src/db/schema.sql')
    exec_sql_file('src/db/test_schema.sql')

    # Drop the test database
    cur.execute("DROP DATABASE test_db;")
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()