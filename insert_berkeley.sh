#!/bin/bash

# Specify the values for "who" and "speed"
who_values="0 1"
speed_values="0.00000001"

# Loop through combinations of "who" and "speed"
for who in $who_values; do
    for speed in $speed_values; do
        # Delete existing Berkeley DB directory
        rm -rf ./berkeley_db 

        # Create a fresh Berkeley DB directory
        mkdir ./berkeley_db

        # Run insert.py with different parameters and log the output
        output=$(python3 insert_berkeley.py $who $speed)
        echo "$who $speed $output" >> output_berkeley_insert.txt
    done
done
