# Embedded databases with Berkeley DB and SQLite
## The project goal
This project focuses on embedded databases and aims to analyze and compare the performance of two of them widely used today. These are Berkeley DB and SQLite. This analysis will be carried out using a dataset of vehicular data.\
It only runs on linux systems.\
You need to install these dependencies:
`sudo apt install python3`\
`sudo apt install sqlite3`\
`sudo apt install libdb-dev`\
`pip install bsddb3`
## How to run SQLite
### Insertion
You should simply use the script `insert_sqlite.sh`\
And the python file that is used should be run as:/
`python3 insert_sqlite.py who[0-1] speed_insertion`
### Selection
You should simply use the script `select_sqlite.sh`\
And the python file that is used should be run as:/
`python3 select_sqlite.py who[0-1]`
## How to run Berkeley DB
Firstly run `berkeley_setup.py` to setup the DB.
### Insertion
You should simply use the script `insert_berkeley.sh`\
And the python file that is used should be run as:/
`python3 insert_berkeley.py who[0-1] speed_insertion`
### Selection
You should simply use the script `select_berkeley.sh`\
And the python file that is used should be run as:/
`python3 select_berkeley.py who[0-1]`
