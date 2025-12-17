from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database='appdb',
        user='appuser',
        password='apppass'
    )
    return conn

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'running'
    })

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({'status': 'healthy', 'database': 'connected'})
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)