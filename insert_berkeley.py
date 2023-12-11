import bsddb3
import time
import csv
import sys
import os

def insert_row_gps(db, timestamp, values, who):
    key = f"gps_{timestamp}" if who == 0 else f"gps_left_{timestamp}"
    db.put(key.encode('utf-8'), values.encode('utf-8'))

def insert_data_from_csv(db_path, csv_path, columns, insertion_speed, who):
    # Berkeley DB environment
    db_env = bsddb3.db.DBEnv()
    db_env.open(db_path, bsddb3.db.DB_CREATE | bsddb3.db.DB_INIT_MPOOL)

    # Berkeley DB database
    db = bsddb3.db.DB(db_env)
    db.open("berkeley_db.db", bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)

    try:
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                timestamp = row['timestamp']
                values = ','.join([row[column] for column in columns])

                start_time = time.time()

                insert_row_gps(db, timestamp, values, who)

                end_time = time.time()
                time_taken = end_time - start_time

                if insertion_speed > time_taken:
                    sleep_duration = insertion_speed - time_taken
                    time.sleep(sleep_duration)

    finally:
        # Close Berkeley DB connections
        db.close()
        db_env.close()

def main():
    start_time = time.time()
    db_path = "./berkeley_db"

    who = int(sys.argv[1])
    insertion_speed = float(sys.argv[2])

    if who == 0:
        csv_path = 'data/dataset_gps.csv'
        columns_to_insert = ["timestamp", "latitude", "longitude", "elevation", "accuracy"]
    else:
        csv_path = 'data/dataset_mpu_left.csv'
        columns_to_insert = ["timestamp", "acc_x_dashboard", "acc_y_dashboard", "acc_z_dashboard"]

    insert_data_from_csv(db_path, csv_path, columns_to_insert, insertion_speed, who)

    print(time.time() - start_time)

if __name__ == '__main__':
    main()
