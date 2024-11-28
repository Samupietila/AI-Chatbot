import mysql

from DbConnection import db_connection


# Authentication
def authenticate_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    connection = db_connection()
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM User WHERE Username = %s AND Password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:

            #placeholder for actual website authentication

            print(f"Welcome, {username}!")

        else:
            print("Invalid username or password. Please try again.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

