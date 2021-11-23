import os

class InvalidUsernameError(Exception):
	pass

class InvalidPasswordError(Exception):
	pass

class InvalidPasswordMatchError(Exception):
	pass

class UsernameExistsError(Exception):
	pass

class DiaryService:
	def __init__(self) -> None:
		self._user = None
		self._users_file = self.check_users_file()
		self._all_users = self.get_all_users()

	def check_users_file(self):
		data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../data'))
		if not os.path.isdir(data_dir):
			os.mkdir(data_dir)
		if not os.path.isfile(os.path.join(data_dir, 'users.txt')):
			with open(os.path.join(data_dir, 'users.txt'), 'w') as file:
				file.write('')
		return os.path.join(data_dir, 'users.txt')

	def get_current_user(self):
		return self._user

	def get_all_users(self):
		all_users = []
		with open(self._users_file) as users_file:
			for row in users_file:
				row = row.replace('\n', '')
				all_users.append(row.split()[0])
		return all_users

	def create_user(self, username, password_1, password_2):
		if username not in self.get_all_users() and len(username) >= 3 and len(password_1) >= 3 and password_1 == password_2:
			with open(self._users_file, 'a') as users_file:
				users_file.write(f'{username} {password_1}\n')
			self._user = username
		elif len(username) < 3:
			raise InvalidUsernameError
		elif len(password_1) < 3:
			raise InvalidPasswordError
		elif password_1 != password_2:
			raise InvalidPasswordMatchError
		else:
			raise UsernameExistsError

diary_service = DiaryService()