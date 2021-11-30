import unittest
from viewmodel.view_model import ViewModel
from model.user_model import UserModel

class TestViewModel(unittest.TestCase):
	def setUp(self) -> None:
		self.view_model = ViewModel()
		self.user_model = UserModel()

	def test_create_user_correct(self) -> None:
		username = 'matias'
		password = 'sala5ana'
		self.view_model.create_user(username, password, password)
		self.assertEqual(True, username in self.user_model._get_all_users())

	def tearDown(self) -> None:
		return super().tearDown()


		