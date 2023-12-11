#!/bin/bash

# Specify the values for "who" 
who_values="0 1"

# Copy a fresh empty SQLite database
cp -r berkeley_db_empty berkeley_db

# Loop through combinations of "who"
for who in $who_values; do
    python3 insert_berkeley.py $who 0.00000000001

    # Run select.py with different parameters and log the output
    output=$(python3 select_berkeley.py $who)
    echo "$who $speed $output" >> output_berkeley_select.txt
done