import bsddb3
import os

def create_berkeley_db(db_path):
    # Ensure the directory exists
    if not os.path.exists(db_path):
        os.makedirs(db_path)

    # Open (or create) the Berkeley DB environment
    db_env = bsddb3.db.DBEnv()
    db_env.open(db_path, bsddb3.db.DB_CREATE | bsddb3.db.DB_INIT_MPOOL)

    # Open (or create) the database
    db = bsddb3.db.DB(db_env)
    db.open("my_berkeley_db.db", bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)

    return db, db_env

def create_gps_table(db, key, value):
    # Store data in the "gps" table using key-value pairs
    db.put(key.encode('utf-8'), value.encode('utf-8'))

def close_berkeley_db(db, db_env):
    # Close the database and environment
    db.close()
    db_env.close()

# Example usage
db_path = "./berkeley_db"
key = "location_1"
value = "Latitude: 37.7749, Longitude: -122.4194"

db, db_env = create_berkeley_db(db_path)
create_gps_table(db, key, value)
close_berkeley_db(db, db_env)
