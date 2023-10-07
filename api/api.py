import psycopg2
import logging

from flask import Flask, jsonify, request

app = Flask(__name__)

# logging config
logging.basicConfig(filename='logs/api.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

DB_HOST = "localhost"
DB_PORT = "5432"

@app.route('/read/first-chunk', methods=['GET'])
def read_first_chunk():
    try:
        conn = psycopg2.connect(
            dbname= request.args.get('db_name'),
            user= request.args.get('user'),
            password= request.args.get('password'),
            host= DB_HOST,
            port= DB_PORT
        )
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {request.args.get('table_name')} LIMIT {request.args.get('num_records')};")
        data = cursor.fetchall()

        result = []
        for row in data:
            result.append({
                'id': row[0],
                'first_name': row[1],  
                'last_name': row[2],   
                'age': row[3],
                'location': row[4]  
            })

        cursor.close()
        conn.close()

        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Error in query: {str(e)}")
        return jsonify({'error': 'Error occurred while fetching data'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)