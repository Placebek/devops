from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host="db",
            database="university",
            user="student",
            password="secret"
        )
        return "✅ PostgreSQL-ге сәтті қосылдық!"
    except Exception as e:
        return f"❌ Қате: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
