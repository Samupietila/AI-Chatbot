from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, UserID, Username, Email, Password, RegistrationDate, LastLogin,is_active=True):
        self.id = UserID
        self.username = Username
        self.email = Email
        self.password = Password
        self.registrationDate = RegistrationDate
        self.lastLogin = LastLogin
        self._is_active = is_active

    def get_id(self):
        return self.id

    @property
    def is_active(self):
        return self._is_active