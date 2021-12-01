import unittest
from database import db
from model.diary_model import DiaryModel
from model.user_model import UserModel


class TestDiaryModel(unittest.TestCase):
    def setUp(self) -> None:
        self.diary_model = DiaryModel()
        self.user_model = UserModel()
        self.database = db
        username = 'diary_model_test'
        password = 'secret'
        self.test_user = self.user_model.create_user(username, password, password)

    def test_initial_entry(self) -> None:
        self.assertEqual(len(self.diary_model.get_user_entries(self.test_user)), 0)
    
    def test_creating_first_entry(self) -> None:
        self.diary_model.create_first_entry(self.test_user)
        self.assertEqual(len(self.diary_model.get_user_entries(self.test_user)), 1)
        self.assertEqual(self.diary_model.get_user_entries(self.test_user)[0].heading, 'Welcome')

    def test_creating_new_entry(self) -> None:
        self.diary_model.create_entry(self.test_user)
        self.assertEqual(len(self.diary_model.get_user_entries(self.test_user)), 1)
        self.assertEqual(self.diary_model.get_user_entries(self.test_user)[0].heading, 'New entry')

    def test_update_entry(self):
        self.diary_model.create_entry(self.test_user)
        test_entry = self.diary_model.get_user_entries(self.test_user)[0]
        test_entry.heading = 'Updated heading'
        test_entry.content = 'Updated content'
        self.diary_model.save_entry(test_entry)
        self.assertEqual(len(self.diary_model.get_user_entries(self.test_user)), 1)
        self.assertEqual(self.diary_model.get_user_entries(self.test_user)[0].heading, 'Updated heading')
        self.assertEqual(self.diary_model.get_user_entries(self.test_user)[0].content, 'Updated content')

    def tearDown(self) -> None:
        self.database.empty_database()
