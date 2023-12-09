import bsddb3
import time
import os

def count_rows(db, table_name):
    start_time = time.time()
    count = 0
    try:
        cursor = db.cursor()
        key = f"{table_name}_"
        if cursor.set_range(key.encode('utf-8')):
            while key.encode('utf-8').startswith(f"{table_name}_".encode('utf-8')):
                count += 1
                if not cursor.next():
                    break
    finally:
        cursor.close()

    end_time = time.time()
    print(f"Count rows query took {end_time - start_time} seconds. Result: {count} rows")

def select_all(db, table_name):
    start_time = time.time()
    rows = []
    try:
        cursor = db.cursor()
        key = f"{table_name}_"
        if cursor.set_range(key.encode('utf-8')):
            while key.encode('utf-8').startswith(f"{table_name}_".encode('utf-8')):
                timestamp, values = key[len(table_name) + 1:].split("_", 1)
                rows.append((timestamp, values))
                if not cursor.next():
                    break
    finally:
        cursor.close()

    end_time = time.time()
    print(f"Select all query took {end_time - start_time} seconds. Result: {len(rows)} rows")

def select_by_latitude(db, table_name):
    start_time = time.time()
    rows = []
    try:
        cursor = db.cursor()
        key = f"{table_name}_"
        if cursor.set_range(key.encode('utf-8')):
            while key.encode('utf-8').startswith(f"{table_name}_".encode('utf-8')):
                timestamp, values = key[len(table_name) + 1:].split("_", 1)
                rows.append((timestamp, values))
                if not cursor.next():
                    break
    finally:
        cursor.close()

    end_time = time.time()
    print(f"Select by latitude query took {end_time - start_time} seconds. Result: {len(rows)} rows")

def select_by_acc_x(db, table_name, threshold):
    start_time = time.time()
    rows = []
    try:
        cursor = db.cursor()
        key = f"{table_name}_"
        if cursor.set_range(key.encode('utf-8')):
            while key.encode('utf-8').startswith(f"{table_name}_".encode('utf-8')):
                timestamp, values = key[len(table_name) + 1:].split("_", 1)
                acc_x_value = float(values.split(",")[1])  # Assuming acc_x_dashboard is the second value
                if acc_x_value > threshold:
                    rows.append((timestamp, values))
                if not cursor.next():
                    break
    finally:
        cursor.close()

    end_time = time.time()
    print(f"Select by acc_x_dashboard query took {end_time - start_time} seconds. Result: {len(rows)} rows")

def select_by_acc_y(db, table_name, threshold):
    start_time = time.time()
    rows = []
    try:
        cursor = db.cursor()
        key = f"{table_name}_"
        if cursor.set_range(key.encode('utf-8')):
            while key.encode('utf-8').startswith(f"{table_name}_".encode('utf-8')):
                timestamp, values = key[len(table_name) + 1:].split("_", 1)
                acc_y_value = float(values.split(",")[2])  # Assuming acc_y_dashboard is the third value
                if acc_y_value > threshold:
                    rows.append((timestamp, values))
                if not cursor.next():
                    break
    finally:
        cursor.close()

    end_time = time.time()
    print(f"Select by acc_y_dashboard query took {end_time - start_time} seconds. Result: {len(rows)} rows")


def main():
    db_path = "./berkeley_db"

    who = int(sys.argv[1])

    # Berkeley DB environment
    db_env = bsddb3.db.DBEnv()
    db_env.open(db_path, bsddb3.db.DB_CREATE | bsddb3.db.DB_INIT_MPOOL)

    # Berkeley DB database
    db = bsddb3.db.DB(db_env)
    db.open("berkeley_db.db", bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)

    try:
        table_name = "gps" if who == 0 else "gps_left"

        count_rows(db, table_name)
        select_all(db, table_name)
        if who == 0:
            select_by_latitude(db, table_name)
        else:
            select_by_acc_x(db, table_name, 0.35)
            select_by_acc_y(db, table_name, 0.15)
    finally:
        # Close Berkeley DB connections
        db.close()
        db_env.close()

if __name__ == '__main__':
    main()