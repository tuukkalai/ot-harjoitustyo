import os
import unittest
import pytest
from services.diary_service import DiaryService, InvalidPasswordError, InvalidPasswordMatchError, InvalidUsernameError, UsernameExistsError

class TestDiaryService(unittest.TestCase):
	def setUp(self):
		self.diary_service = DiaryService('test_users.txt')
		self._users_file = self.diary_service.check_users_file('test_users.txt')

	def test_create_user_correct(self):
		username = 'Matias'
		password_1 = 'salasana'
		password_2 = 'salasana'
		self.diary_service.create_user(username, password_1, password_2)
		created_users = self.diary_service.get_all_users()
		self.assertEqual(username in created_users, True)

	def test_create_user_with_short_username(self):
		with pytest.raises(InvalidUsernameError) as e:
			self.diary_service.create_user('as', '1234', '1234')
		self.assertEqual(str(e.value), 'Invalid username')
		created_users = self.diary_service.get_all_users()
		self.assertEqual('as' not in created_users, True)

	def test_create_user_with_short_password(self):
		with pytest.raises(InvalidPasswordError) as e:
			self.diary_service.create_user('user', '12', '12')
		self.assertEqual(str(e.value), 'Invalid password')
		created_users = self.diary_service.get_all_users()
		self.assertEqual('user' not in created_users, True)

	def test_create_user_with_mismatch_password(self):
		with pytest.raises(InvalidPasswordMatchError) as e:
			self.diary_service.create_user('user', '1234', '1243')
		self.assertEqual(str(e.value), 'Passwords do not match')
		created_users = self.diary_service.get_all_users()
		self.assertEqual('user' not in created_users, True)

	def test_create_user_that_already_exists(self):
		username = 'Paavo'
		self.diary_service.create_user(username, '1234', '1234')
		self.assertEqual(username in self.diary_service.get_all_users(), True)
		with pytest.raises(UsernameExistsError) as e:
			self.diary_service.create_user(username, '1234', '1234')
		self.assertEqual(str(e.value), 'Username already exists')
		created_users = self.diary_service.get_all_users()
		self.assertEqual(created_users.count(username), 1)


	def tearDown(self):
		if os.path.isfile(self._users_file):
			os.remove(self._users_file)
