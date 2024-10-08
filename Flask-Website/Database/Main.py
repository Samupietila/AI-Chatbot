from DbConnection import db_connection
from authentication import authenticate_user
from registration import register

def main():
    register()
    authenticate_user()

if __name__ == "__main__":
    main()
