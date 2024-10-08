from DbConnection import db_connection

def register():
    email = input("email")
    username = input("username")
    password = input("password")
    connection = db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("Select * from user where email = %s ", (email,))
        already_exists = cursor.fetchone()
        if already_exists:
            return print("already exists")

        cursor.execute("select MAX(UserID) from user")
        userid = cursor.fetchone()[0]
        if userid == None :
            userid = 1
        else: userid += 1
        insertion = "insert into user (UserID, username, email, password, registrationdate) values (%s, %s, %s, %s, CURDATE())"
        cursor.execute(insertion, (userid, username, email, password))
        connection.commit()
        return print("registered")

    except Exception as e:
        return print(e)

    finally:
        cursor.close()
        connection.close()

