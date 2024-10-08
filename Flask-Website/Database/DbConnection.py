import mysql.connector
from config import DB_CONFIG

def db_connection():
    config = DB_CONFIG
    return mysql.connector.connect(**config)