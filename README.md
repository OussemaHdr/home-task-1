# Home Task - Data Engineer - 1
## Setup
1. Clone the repository:

   ```bash
   git clone https://github.com/OussemaHdr/home-task-1.git
   cd home-task-1
   ```
   ```bash
   pip install -r requirements.txt
2. PostgreSQL Configuration:  
First ensure you have Postgres installed. [You can download it from the official Postgres website](https://www.postgresql.org/download/).  
Start the Postgres service:  
    ```bash
    sudo service postgresql start
    ```
    Run the setup bash script to create the Postgres db, user and table (all the variables used here will be used to run the rest of the scripts): 
    ```bash
    chmod +x postgres_setup.sh
    ./postgres_setup.sh <database_name> <username> <password> <table_name>
    ```
## Running the ETL Pipeline  
Run the ETL pipeline to read the CSV sample, transform the data, and load it into the Postgres db:  
```bash
python etl/etl.py data/sample.csv <database_name> <username> <password> <table_name>
```
## Running the REST API
Run the REST API to expose an endpoint for retrieving data from the Postgres db:
```bash
python api/api.py
```
## Testing the API
Run the test script to send a request to the API and print the response:
```bash
python api/test_api.py  data/sample.csv <database_name> <username> <password> <table_name>
```
## Deployment system diagram (AWS)