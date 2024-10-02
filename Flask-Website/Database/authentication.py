import mysql
from Database.DbConnection import db_connection
from website.models import User

# Authentication
def authenticate_user(username, password):
    
    connection = db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM User WHERE Username = %s AND Password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            #Login successful
            return User(**user)
        else:
            #Login Failed
            return False
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

#Registering
def register(email, username, password):
    connection = db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("select MAX(UserID) from user")
        userid = cursor.fetchone()[0]
        if userid == None:
            userid = 1
        else:
            userid += 1
        insertion = "insert into user (UserID, username, email, password, registrationdate) values (%s, %s, %s, %s, CURDATE())"
        cursor.execute(insertion, (userid, username, email, password))
        connection.commit()
        return print("registered")

    except Exception as e:
        return print(e)

    finally:
        cursor.close()
        connection.close()
        
def emailCheck(email):
    connection = db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("Select * from user where email = %s ", (email,))
        already_exists = cursor.fetchone()
        if already_exists:
            return True
        else:
            return False
        
    except Exception as e:
        return print(e)
    
    finally:
        cursor.close()
        connection.close()
        
def load_user(user_id):
    connection = db_connection()
    cursor = connection.cursor(dictionary=True)  # Fetch data as dictionary

    try:
        query = "SELECT * FROM User WHERE UserID = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

        if user:
            return User(**user)
        else:
            return None
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()