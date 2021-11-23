from tkinter import ttk, constants
from services.diary_service import InvalidPasswordError, InvalidUsernameError 

PADDING = 5

class Login:
	def __init__(self, root, login_success, create_new_user) -> None:
		self._root = root
		self._frame = None
		self._login_success = login_success
		self._create_new_user = create_new_user
		self._username_entry = None
		self._password_entry = None
		self._initialize()

	def _initialize(self):
		self._frame = ttk.Frame(master=self._root)

		# Login view items
		heading_label = ttk.Label(master=self._frame, text='Login')

		username_label = ttk.Label(master=self._frame, text='Username')
		self._username_entry = ttk.Entry(master=self._frame)

		password_label = ttk.Label(master=self._frame, text='Password')
		self._password_entry = ttk.Entry(master=self._frame, show='*')

		login_button = ttk.Button(
			master=self._frame, 
			text='Login',
			command=lambda : self._handle_login_button()
		)
		create_user_button = ttk.Button(
			master=self._frame,
			text='Create new user',
			command=lambda : self._handle_create_user_button()
		)

		# Positioning items to grid
		heading_label.grid(
			row=0, 
			column=0, 
			columnspan=2, 
			sticky=constants.W, 
			padx=PADDING, 
			pady=PADDING
		)

		username_label.grid(
			row=1, 
			column=0, 
			sticky=constants.E,
			padx=PADDING, 
			pady=PADDING
		)
		self._username_entry.grid(
			row=1, 
			column=1, 
			sticky=constants.EW,
			padx=PADDING, 
			pady=PADDING
		)

		password_label.grid(
			row=2, 
			column=0, 
			sticky=constants.E,
			padx=PADDING, 
			pady=PADDING
		)
		self._password_entry.grid(
			row=2, 
			column=1, 
			sticky=constants.EW, 
			padx=PADDING, 
			pady=PADDING
		)

		login_button.grid(
			row=3, 
			column=0, 
			columnspan=2, 
			sticky=constants.EW,
			padx=PADDING, 
			pady=PADDING
		)
		create_user_button.grid(
			row=4, 
			column=0, 
			columnspan=2, 
			sticky=constants.EW,
			padx=PADDING, 
			pady=PADDING
		)

		# Fill extra space if window is resized
		self._frame.grid_columnconfigure(1, minsize=400, weight=1)
		self._frame.pack(fill=constants.X)

	def _handle_login_button(self):
		username = self._username_entry.get()
		password = self._password_entry.get()
		if username and password:
			self._login_success()
		elif not username:
			raise InvalidUsernameError('Username empty.')
		elif not password:
			raise InvalidPasswordError('Password empty.')

	def _handle_create_user_button(self):
		self._create_new_user()

	def destroy(self):
		self._frame.destroy()
