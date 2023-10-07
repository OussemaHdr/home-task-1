#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <database_name> <username> <password> <table_name>"
    exit 1
fi

# db config
DB_NAME="$1"
DB_USER="$2"
DB_PASSWORD="$3"
TABLE_NAME="$4"

sudo -i -u postgres bash << EOF
whoami
psql -c "CREATE DATABASE $DB_NAME;"
psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
EOF

PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -d $DB_NAME -h 127.0.0.1 << EOF
CREATE TABLE $TABLE_NAME (
    id VARCHAR(36) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    location VARCHAR(50) NOT NULL
);
EOF