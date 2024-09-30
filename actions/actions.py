from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime
import mysql.connector

class ActionLogMessageTime(Action):

    def name(self) -> str:
        return "action_log_message_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        # Get the current timestamp
        current_time = datetime.datetime.now()

        # Get the user ID from the conversation tracker
        user_id = tracker.sender_id  # `sender_id` returns a string (conversation ID)

        # Log the time and other relevant data to the database
        try:
            # Add a debug log to check if the action is triggered
            print(f"Action triggered for user: {user_id} at {current_time}")

            # Establish database connection
            print("Attempting to connect to the database...")
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin',
                database='ChatAppDatabase'
            )
            cursor = connection.cursor()

            # Insert query to log the message timestamp
            print(f"Executing SQL query: INSERT INTO UserMessageLogs with values: ({user_id}, {current_time})")
            insert_query = """INSERT INTO UserMessageLogs (UserID, MessageTimeStamp) 
                              VALUES (%s, %s)"""
            cursor.execute(insert_query, (user_id, current_time))

            connection.commit()

            # Confirm the data was inserted
            print(f"Data inserted successfully for user {user_id} at {current_time}")

        except mysql.connector.Error as error:
            # Log any error that occurs during database interaction
            print(f"Error while logging to database: {error}")
            dispatcher.utter_message(text=f"Failed to log the time: {error}")
        finally:
            # Ensure the cursor and connection are closed if they were created
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
            print("Database connection closed")

        dispatcher.utter_message(text=f"Message time logged at {current_time}")
        return []
