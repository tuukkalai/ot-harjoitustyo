from entities.user import User
from database import db


class WrongUsernamePasswordError(BaseException):
    pass


class UsernameAlreadyExistsError(BaseException):
    pass


class InvalidCredentialsError(BaseException):
    pass


class PasswordMismatchError(BaseException):
    pass


class UserModel:
    def __init__(self) -> None:
        self._connection = db.get_connection()

    def _get_all_users(self) -> list:
        cursor = self._connection.cursor()
        rows = cursor.execute('SELECT username FROM users').fetchall()
        usernames = list(map(lambda row: row['username'], rows))
        return usernames

    def login(self, username, password) -> User:
        if not self.__is_input_correct(username, password):
            raise WrongUsernamePasswordError('Wrong username and/or password')
        cursor = self._connection.cursor()
        cursor.execute(''' SELECT id, username, password
            FROM users
            WHERE username = ? ''', (username,))
        user = cursor.fetchone()
        if user and user[2] == password:
            return User(user[0], user[1])
        raise WrongUsernamePasswordError('Wrong username and/or password')

    def create_user(self, username, password_1, password_2) -> User:
        if username in self._get_all_users():
            raise UsernameAlreadyExistsError(
                f'Username `{username}` already exists')

        if password_1 != password_2:
            raise PasswordMismatchError('Passwords do not match')

        if not self.__is_input_correct(username, password_1):
            raise InvalidCredentialsError(
                'Username or password too short, min. 3 characters')

        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?,?)", (username, password_1))
        self._connection.commit()
        return User(cursor.lastrowid, username)

    def delete_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM users WHERE id=?', (user.id,))
        self._connection.commit()

    def __is_input_correct(self, username, *passwords) -> bool:
        if len(username) < 3:
            return False
        for password in passwords:
            if len(password) < 3:
                return False
        return True
