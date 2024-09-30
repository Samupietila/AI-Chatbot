import mysql.connector

def insert_user():
    connection = None  # Initialize connection variable
    cursor = None  # Initialize cursor variable

    try:
        # Establish the connection to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='ChatAppDatabase',
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Insert query to add a new user
        insert_query = """INSERT INTO User (Username, Email, Password, RegistrationDate, LastLogin)
                          VALUES (%s, %s, %s, NOW(), NOW())"""

        # Values to insert into the User table
        user_data = ('Matti Meneperilleastinytsaatana', 'matti@example.com', 'salasana123')

        # Execute the query
        cursor.execute(insert_query, user_data)

        # Commit the transaction to save changes
        connection.commit()

        print(f"User added successfully!")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection if they are open
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
# Call the function to insert a user
insert_user()
