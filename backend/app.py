from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Local DB CONFIG
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "5002"
DB_NAME = "dinelogic_db"

def connect_to_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# -----------------------------
# 1️⃣ Get All Restaurants
# -----------------------------
@app.route("/restaurants", methods=["GET"])
def get_restaurants():
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)

    location = request.args.get("location")

    if location:
        cursor.execute("SELECT * FROM restaurants WHERE location=%s LIMIT 50;", (location,))
    else:
        cursor.execute("SELECT * FROM restaurants LIMIT 50;")

    results = cursor.fetchall()
    connection.close()

    return jsonify(results)


# -----------------------------
# 2️⃣ Top Rated Restaurants
# -----------------------------
@app.route("/analytics/top-rated", methods=["GET"])
def top_rated():
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT restaurant_name, rating_clean, total_ratings_clean
        FROM restaurants
        ORDER BY rating_clean DESC
        LIMIT 10;
    """)

    results = cursor.fetchall()
    connection.close()

    return jsonify(results)


# -----------------------------
# 3️⃣ Best Value (Performance Score)
# -----------------------------
@app.route("/analytics/top-performance", methods=["GET"])
def top_performance():
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT restaurant_name, performance_score
        FROM restaurants
        ORDER BY performance_score DESC
        LIMIT 10;
    """)

    results = cursor.fetchall()
    connection.close()

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)