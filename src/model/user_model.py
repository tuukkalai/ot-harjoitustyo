from entities.user import User
from database import db


class WrongPasswordError(BaseException):
    pass


class UsernameNotExistsError(BaseException):
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
        cursor = self._connection.cursor()
        cursor.execute(''' SELECT id, username, password
			FROM users
			WHERE username = ? ''', (username,))
        user = cursor.fetchone()
        if not user:
            raise UsernameNotExistsError(f'Username `{username}` not found')
        if user[2] == password:
            return User(user[0], user[1])
        raise WrongPasswordError('Wrong password')

    def create_user(self, username, password_1, password_2) -> User:
        if username in self._get_all_users():
            raise UsernameAlreadyExistsError(
                f'Username `{username}` already exists')

        if password_1 != password_2:
            raise PasswordMismatchError('Passwords do not match')

        if len(password_1) > 2 and len(username) > 2:
            cursor = self._connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?,?)", (username, password_1))
            self._connection.commit()
            return User(cursor.lastrowid, username)
        raise InvalidCredentialsError(
            'Username or password too short, min. 3 characters')

    def delete_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM users WHERE id=?', (user.id,))
        self._connection.commit()
