import mysql.connector

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