from entities.user import User
from database import db
import uuid

class WrongPasswordError(BaseException):
	pass

class UsernameNotExistsError(BaseException):
	pass

class UserModel:
	def __init__(self) -> None:
		self._connection = db.get_connection()

	def login(self, username, password) -> User:
		cursor = self._connection.cursor()
		cursor.execute(''' SELECT username, password 
			FROM users 
			WHERE username=? ''', 
			(username,)
		)
		user = cursor.fetchone()
		if user:
			if user[1] == password:
				return User(username)
			else:
				raise WrongPasswordError
		else:
			raise UsernameNotExistsError


	def create_user(self, username, password1, password2) -> User:
		if password1 == password2 and len(password1) > 2 and len(username) > 2:
			cursor = self._connection.cursor()
			cursor.execute("INSERT INTO users VALUES (?,?,?)", (uuid.hex(), username, password1))
			self._connection.commit()
			return User(username)
		else:
			# TODO: raise error
			print('Username or password too short, or password mismatch')
			return None