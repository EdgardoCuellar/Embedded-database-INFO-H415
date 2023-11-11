#!/bin/bash

# Specify the values for "who" and "speed"
who_values="0 1"
speed_values="0.01 0.001 0.0001 0.00000001"

# Loop through combinations of "who" and "speed"
for who in $who_values; do
    for speed in $speed_values; do
        # Delete existing SQLite database file
        rm -f sqlite.db

        # Copy a fresh empty SQLite database
        cp sqlite_empty.db sqlite.db

        # Run insert.py with different parameters and log the output
        output=$(python3 insert_sqlite.py $who $speed)
        echo "$who $speed $output" >> output_sqlite_insert.txt
    done
done
