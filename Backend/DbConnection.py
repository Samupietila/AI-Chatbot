import mysql.connector

def db_connection():
    config = {
        'user': 'root',
        'password': 'mariadb',
        'host': 'localhost',
        'database': 'ChatAppDatabase',
        'raise_on_warnings': True
    }
    return mysql.connector.connect(**config)