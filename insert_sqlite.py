import sqlite3
import time
import csv
import sys


def insert_row_gps(cursor, columns, row):
    placeholders = ', '.join(['?' for _ in columns])
    insert_query = f'INSERT INTO gps ({", ".join(columns)}) VALUES ({placeholders});'
    cursor.execute(insert_query, row)

def insert_row_gps_left(cursor, columns, row):
    placeholders = ', '.join(['?' for _ in columns])
    insert_query = f'INSERT INTO gps_left ({", ".join(columns)}) VALUES ({placeholders});'
    cursor.execute(insert_query, row)


def insert_data_from_csv(db_path, csv_path, columns, insertion_speed, who):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_row = [row[column] for column in columns]

                if who == 0:
                    insert_row_gps(cursor, columns, data_row)
                elif who == 1:
                    insert_row_gps_left(cursor, columns, data_row)

                if insertion_speed > 0.00001:
                    time.sleep(insertion_speed)

                connection.commit()
    finally:
        connection.close()

def main():
    start_time = time.time()
    db_path = 'sqlite.db'

    who = int(sys.argv[1])
    insertion_speed = float(sys.argv[2])

    if who == 0:
        csv_path = 'data/dataset_gps.csv'
        columns_to_insert = ["timestamp","latitude","longitude","elevation","accuracy"] 
    else:
        csv_path = 'data/dataset_mpu_left.csv'
        columns_to_insert = ["timestamp","acc_x_dashboard","acc_y_dashboard","acc_z_dashboard"] 

    insert_data_from_csv(db_path, csv_path, columns_to_insert, insertion_speed, who)

    print(time.time() - start_time)

if __name__ == '__main__':
    main()
    
