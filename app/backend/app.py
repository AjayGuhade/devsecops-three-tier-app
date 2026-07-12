from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        connection = mysql.connector.connect(
            host="mysql-db",
            user="root",
            password="root123",
            database="employee_db"
        )

        if connection.is_connected():
            return """
            <h1>Docker Three-Tier Application</h1>
            <h2>✅ Backend Connected to MySQL Successfully!</h2>
            """

    except Exception as e:
        return f"<h2>❌ Database Connection Failed</h2><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
