from python.database.connection import get_session
from python.database.models.User import User


class AuthController:
    def __init__(self):
        self.session = get_session()

    def login(self, login: str, password: str):
        user = (
            self.session
            .query(User)
            .filter(User.login == login, User.password == password)
            .first())

        if user:
            return user
        else:
            return None
