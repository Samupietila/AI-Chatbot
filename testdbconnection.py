import mysql.connector
import datetime

def log_message_time():
    current_time = datetime.datetime.now()
    user_id = 1  # Hardcoded for now
    connection = None  # Initialize the connection variable to None
    cursor = None

    try:
        # Establish the connection with utf8mb4 charset
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='ChatAppDatabase',
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )

        # Create a cursor
        cursor = connection.cursor()

        # Set the collation for the session to utf8mb4_unicode_ci
        cursor.execute("SET collation_connection = 'utf8mb4_unicode_ci';")


        # Insert query to log the message timestamp
        insert_query = """INSERT INTO UserMessageLogs (UserID, MessageTimeStamp)
                          VALUES (%s, %s)"""
        cursor.execute(insert_query, (user_id, current_time))
        connection.commit()

        print(f"Data inserted successfully at {current_time}")

    except mysql.connector.Error as error:
        print(f"Error: {error}")  # Improved error message for clarity

    finally:
        # Close the cursor if it was created
        if cursor:
            cursor.close()
        # Check if connection is established before closing it
        if connection and connection.is_connected():
            connection.close()

log_message_time()
