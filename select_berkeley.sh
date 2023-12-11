#!/bin/bash

# Specify the values for "who"
who_values="0 1"

# Copy a fresh empty Berkeley DB directory
cp -r berkeley_db_empty berkeley_db

# Loop through combinations of "who"
for who in $who_values; do
    # Run insert script
    python3 insert_berkeley.py $who 0.00000000001

    # Check for errors in insert script
    if [ $? -ne 0 ]; then
        echo "Error in insertion for who value $who"
        continue
    fi

    # Run select script and log the output
    output=$(python3 select_berkeley.py $who)
    echo -e "$who\n$output" >> output_berkeley_select.txt
done
