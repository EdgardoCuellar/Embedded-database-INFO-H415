import csv
import glob

def calculate_time_difference(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Assuming "timestamp" is the name of the column
            timestamp_column = [row['timestamp'] for row in reader]

            nb = 100

            if len(timestamp_column) >= nb:
                time_difference = 0
                for i in range(0, nb):
                    difference = float(timestamp_column[i+1]) - float(timestamp_column[0])
                    time_difference += difference

                mean = time_difference / nb

                print(f'Time difference mean: {mean}')
            else:
                print('Not enough timestamps to calculate the difference.')
    except FileNotFoundError:
        print(f'File not found: {file_path}')

def count_rows(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
            
            row_count = sum(1 for row in reader)
            print(f'Number of rows in {file_path}: {row_count}')
    except FileNotFoundError:
        print(f'File not found: {file_path}')


def main():
    directory_path = 'data/*.csv'
    csv_files = glob.glob(directory_path)

    # Iterate through each CSV file and count the rows
    for csv_file in csv_files:
        print("*************************")
        print(csv_file)
        count_rows(csv_file)
        calculate_time_difference(csv_file)

if __name__ == '__main__':
    main()
    
