import unittest
import pytest
from model.user_model import InvalidCredentialsError, PasswordMismatchError, UserModel, UsernameAlreadyExistsError
from database import db


class TestUserModel(unittest.TestCase):
    def setUp(self) -> None:
        self.user_model = UserModel()
        self.database = db

    def test_create_user_correct(self) -> None:
        username = 'matias'
        password = 'sala5ana'
        self.user_model.create_user(username, password, password)
        self.assertEqual(username in self.user_model._get_all_users(), True)

    def test_create_user_with_short_username(self):
        with pytest.raises(InvalidCredentialsError) as Error:
            self.user_model.create_user('as', '1234', '1234')
        self.assertEqual(
            str(Error.value), 'Username or password too short, min. 3 characters')
        created_users = self.user_model._get_all_users()
        self.assertEqual('as' not in created_users, True)

    def test_create_user_with_short_password(self):
        with pytest.raises(InvalidCredentialsError) as Error:
            self.user_model.create_user('user', '12', '12')
        self.assertEqual(
            str(Error.value), 'Username or password too short, min. 3 characters')
        created_users = self.user_model._get_all_users()
        self.assertEqual('user' not in created_users, True)

    def test_create_user_with_mismatch_password(self):
        with pytest.raises(PasswordMismatchError) as Error:
            self.user_model.create_user('user', '1234', '1243')
        self.assertEqual(str(Error.value), 'Passwords do not match')
        created_users = self.user_model._get_all_users()
        self.assertEqual('user' not in created_users, True)

    def test_create_user_that_already_exists(self):
        username = 'Paavo'
        self.user_model.create_user(username, '1234', '1234')
        self.assertEqual(username in self.user_model._get_all_users(), True)
        with pytest.raises(UsernameAlreadyExistsError) as Error:
            self.user_model.create_user(username, '1234', '1234')
        self.assertEqual(str(Error.value),
                         f'Username `{username}` already exists')
        created_users = self.user_model._get_all_users()
        self.assertEqual(created_users.count(username), 1)

    def test_delete_user(self):
        username = 'toDelete'
        user_to_be_deleted = self.user_model.create_user(
            username, '1234', '1234')
        self.assertEqual(username in self.user_model._get_all_users(), True)
        self.user_model.delete_user(user_to_be_deleted)
        created_users = self.user_model._get_all_users()
        self.assertEqual(created_users.count(username), 0)

    def tearDown(self) -> None:
        self.database.empty_database()
