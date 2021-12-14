import unittest
from view.login_view import LoginView
from viewmodel.view_model import ViewModel


class TestUserModel(unittest.TestCase):
    def setUp(self) -> None:
        self.view_model = ViewModel()

    def test_viewmodel_init(self) -> None:
        self.assertEqual(self.view_model._user_logged_in, None)
