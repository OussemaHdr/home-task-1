import requests
import json
import argparse

api_url = "http://127.0.0.1:5000/read/first-chunk"

def test_api():
    params = {
    "db_name": args.db_name,
    "user": args.user_name,
    "password": args.user_password,
    "table_name": args.table_name,
    "num_records": 10  
}
    try:
        response = requests.get(api_url, params = params)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4))
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("db_name", help="db name")
    parser.add_argument("user_name", help="user name")
    parser.add_argument("user_password", help="user password")
    parser.add_argument("table_name", help="table name")
    args = parser.parse_args()

    test_api()