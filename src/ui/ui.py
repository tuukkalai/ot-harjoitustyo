from ui.create_user import CreateUser
from ui.login import Login

class UI:
	def __init__(self, root):
		self._root = root
		self._current_view = None

	def start(self):
		self._show_login_view()

	def _hide_current_view(self):
		if self._current_view:
			self._current_view.destroy()

		self._current_view = None
		
	def _show_login_view(self):
		self._hide_current_view()
		self._current_view = Login(
			self._root, 
			self._show_diary_view, 
			self._show_create_new_user_view
		)

	def _show_create_new_user_view(self):
		self._hide_current_view()
		self._current_view = CreateUser(
			self._root,
			self._show_diary_view,
			self._show_login_view
		)

	def _show_diary_view(self):
		print('ui: showing diary view')