from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host="db",
            database="flask_db",
            user="postgres",
            password="123456qq"
        )
        return "✅ Connected to PostgreSQL!"
    except Exception as e:
        return f"❌ Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
