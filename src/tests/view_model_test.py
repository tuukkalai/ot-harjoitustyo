import unittest
from viewmodel.view_model import ViewModel
from model.user_model import UserModel
from database import db


class TestUserModel(unittest.TestCase):
    def setUp(self) -> None:
        self.view_model = ViewModel()
        self.user_model = UserModel()
        self.database = db

    def test_viewmodel_init(self) -> None:
        self.assertEqual(self.view_model._user_logged_in, None)

    def test_viewmodel_create_user(self) -> None:
        username = 'viewmodeltestuser'
        password = 'password'
        self.view_model.create_user(username, password, password)
        created_users = self.user_model._get_all_users()
        self.assertEqual(username in created_users, True)

    def tearDown(self) -> None:
        self.database.empty_database()