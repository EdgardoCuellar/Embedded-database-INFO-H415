import bsddb3
import sqlite3
import os

def create_berkeley_db(db_path):
    # Ensure the directory exists
    if not os.path.exists(db_path):
        os.makedirs(db_path)

    # Open (or create) the Berkeley DB environment
    db_env = bsddb3.db.DBEnv()
    db_env.open(db_path, bsddb3.db.DB_CREATE | bsddb3.db.DB_INIT_MPOOL)

    # Open (or create) the Berkeley DB database
    db = bsddb3.db.DB(db_env)
    db.open("berkeley_db.db", bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)

    return db, db_env

def copy_table_to_berkeley_db(db, table_name, sqlite_conn):
    # Fetch data from SQLite table
    cursor = sqlite_conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Insert data into Berkeley DB
    for row in rows:
        timestamp = row[0]
        values = ','.join(map(str, row[1:]))  # Combine values into a string
        key_value_pair = f"{table_name}_{timestamp}"
        db.put(key_value_pair.encode('utf-8'), values.encode('utf-8'))

def close_berkeley_db(db, db_env):
    # Close the database and environment
    db.close()
    db_env.close()

# SQLite database connection
sqlite_conn = sqlite3.connect('sqlite_empty.db')

# Berkeley DB environment
db_path = "./berkeley_db"
db, db_env = create_berkeley_db(db_path)

# Copy tables from SQLite to Berkeley DB
copy_table_to_berkeley_db(db, 'gps_left', sqlite_conn)
copy_table_to_berkeley_db(db, 'gps', sqlite_conn)

# Close connections
close_berkeley_db(db, db_env)
sqlite_conn.close()
