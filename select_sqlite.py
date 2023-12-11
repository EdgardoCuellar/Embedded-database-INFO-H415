import sqlite3
import time
import sys

def count_rows(cursor, table_name):
    query = f'SELECT COUNT(*) FROM {table_name};'
    start_time = time.time()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    end_time = time.time()
    print(end_time - start_time)
    print(f"count_rows: {len(rows)} rows")

def select_all(cursor, table_name):
    query = f'SELECT * FROM {table_name};'
    start_time = time.time()
    cursor.execute(query)
    rows = cursor.fetchall()
    end_time = time.time()
    print(end_time - start_time)
    print(f"select_all: {len(rows)} rows")

def select_by_latitude(cursor, table_name):
    query = f'SELECT timestamp FROM {table_name} WHERE latitude = (SELECT latitude FROM {table_name} WHERE rowid = (SELECT rowid + 1 FROM {table_name}));'
    start_time = time.time()
    cursor.execute(query)
    rows = cursor.fetchall()
    end_time = time.time()
    print(end_time - start_time)
    print(f"select_by_latitude: {len(rows)} rows")

def select_by_acc_x(cursor, table_name, threshold):
    query = f'SELECT timestamp FROM {table_name} WHERE acc_x_dashboard > {threshold};'
    start_time = time.time()
    cursor.execute(query)
    rows = cursor.fetchall()
    end_time = time.time()
    print(end_time - start_time)
    print(f"select_by_acc_x: {len(rows)} rows")

def select_by_acc_y(cursor, table_name, threshold):
    query = f'SELECT timestamp FROM {table_name} WHERE acc_y_dashboard > {threshold};'
    start_time = time.time()
    cursor.execute(query)
    rows = cursor.fetchall()
    end_time = time.time()
    print(end_time - start_time)
    print(f"select_by_acc_y: {len(rows)} rows")


def main():
    db_path = 'sqlite.db'

    who = int(sys.argv[1])
    
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        table_name = "gps" if who == 0 else "gps_left"

        count_rows(cursor, table_name)
        select_all(cursor, table_name)
        if who == 0:
            select_by_latitude(cursor, table_name)
        else:
            select_by_acc_x(cursor, table_name, 0.35)
            select_by_acc_y(cursor, table_name, 0.15)
    finally:
        connection.close()

if __name__ == '__main__':
    main()
