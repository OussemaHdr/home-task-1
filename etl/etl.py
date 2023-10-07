import argparse
import csv
import psycopg2
import logging
import uuid

# logging config
logging.basicConfig(filename='logs/etl_pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

DB_HOST = "localhost"
DB_PORT = "5432"

def get_from_csv(file): # Extracting data from sample csv
    data = []
    try:
        with open(file, 'r') as csv_file:
            csv_r = csv.DictReader(csv_file)
            for row in csv_r:
                data.append(row)
        return data
    except Exception as e:
        logger.error(f"Error in get_from_csv: {str(e)}")
        return None
    
def transform(data): # Basic transformation of sample data
    transformed_data = []
    try:
        for record in data:
            transformed_record = {
                "id": str(uuid.uuid4()),
                "first_name": record["fullname"].split()[0],
                "last_name": record["fullname"].split()[1],
                "age": int(record["age"]),
                "location": record["location"]
            }
            transformed_data.append(transformed_record)
        return transformed_data
    except Exception as e:
        logger.error(f"Error in transform: {str(e)}")
        return None

def load_to_db(data, db_name, user_name, user_password, table_name):
    try:
        conn = psycopg2.connect(
            dbname= db_name,
            user= user_name,
            password= user_password,
            host= DB_HOST,
            port= DB_PORT
        )
        cursor = conn.cursor()
        for record in data:
            cursor.execute(
                f"INSERT INTO {table_name} (id, first_name, last_name, location) VALUES (%s, %s, %s, %s)",
                (record['id'], record['first_name'], record['last_name'], record['location'])
            )
        conn.commit()
        logger.info("Data loaded successfully")
    except Exception as e:
        logger.error(f"Error loading: {str(e)}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to CSV sample")
    parser.add_argument("db_name", help="db name")
    parser.add_argument("user_name", help="user name")
    parser.add_argument("user_password", help="user password")
    parser.add_argument("table_name", help="table name")
    args = parser.parse_args()

    data = get_from_csv(args.file_path)
    if data:
        transformed_data = transform(data)
        if transformed_data:
            load_to_db(transformed_data, args.db_name, args.user_name, args.user_password, args.table_name)