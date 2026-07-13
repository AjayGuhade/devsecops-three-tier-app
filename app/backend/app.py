from flask import Flask
import mysql.connector
from mysql.connector import Error
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database configuration from environment variables
DB_HOST = os.getenv("DB_HOST", "mysql-db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root123")
DB_NAME = os.getenv("DB_NAME", "employee_db")


def get_db_connection():
    """Create and return a MySQL database connection."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


@app.route("/")
def home():
    connection = None

    try:
        connection = get_db_connection()

        if connection.is_connected():
            return """
            <h1>🚀 DevSecOps Three-Tier Application</h1>
            <h2>✅ Flask Backend Connected to MySQL Successfully!</h2>
            """

    except Error as err:
        logging.error(f"Database connection error: {err}")
        return f"""
        <h2>❌ Database Connection Failed</h2>
        <p>Please check the application logs for more details.</p>
        """, 500

    finally:
        if connection and connection.is_connected():
            connection.close()


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


@app.route("/ready")
def readiness():
    connection = None

    try:
        connection = get_db_connection()

        if connection.is_connected():
            return {"status": "ready"}, 200

    except Error:
        return {"status": "not ready"}, 503

    finally:
        if connection and connection.is_connected():
            connection.close()


@app.route("/live")
def liveness():
    return {"status": "alive"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)