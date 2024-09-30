#this file is for taking timestamp and pushing it to the database, it does not work
import mysql.connector
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionLogMessageTime(Action):
    def name(self):
        return "action_log_message_time"

    def log_message_time(self, conversation_id, timestamp):
        connection = None
        cursor = None
        try:
            # Establish the connection with utf8mb4 charset
            connection = mysql.connector.connect(
                host='localhost',
                user='yourusername',
                password='yourpassword',
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
            cursor.execute(insert_query, (conversation_id, timestamp))
            connection.commit()

            print(f"Data inserted successfully at {timestamp}")

        except mysql.connector.Error as error:
            print(f"Error: {error}")

        finally:
            # Close the cursor if it was created
            if cursor:
                cursor.close()
            # Check if connection is established before closing it
            if connection and connection.is_connected():
                connection.close()

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Get the conversation ID from the tracker
        conversation_id = tracker.sender_id

        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log the timestamp to the database
        self.log_message_time(conversation_id, timestamp)

        # Send a confirmation message back to the user
        dispatcher.utter_message(text=f"Your message timestamp has been logged at {timestamp}.")

        return []
