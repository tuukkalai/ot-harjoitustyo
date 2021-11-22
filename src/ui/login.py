from tkinter import ttk, constants

PADDING = 5

class Login:
	def __init__(self, root, login_success) -> None:
		self._root = root
		self._login_success = login_success
		self._username_entry = None
		self._password_entry = None
		self._initialize()

	def _initialize(self):
		# Login view items
		heading_label = ttk.Label(master=self._root, text='Login')

		username_label = ttk.Label(master=self._root, text='Username')
		self._username_entry = ttk.Entry(master=self._root)

		password_label = ttk.Label(master=self._root, text='Password')
		self._password_entry = ttk.Entry(master=self._root, show='*')

		login_button = ttk.Button(
			master=self._root, 
			text='Login',
			command=lambda : self._handle_login_button()
		)
		create_user_button = ttk.Button(
			master=self._root,
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
			padx=PADDING, 
			pady=PADDING
		)
		self._username_entry.grid(
			row=1, 
			column=1, 
			sticky=constants.E,
			padx=PADDING, 
			pady=PADDING
		)

		password_label.grid(
			row=2, 
			column=0, 
			padx=PADDING, 
			pady=PADDING
		)
		self._password_entry.grid(
			row=2, 
			column=1, 
			sticky=constants.W, 
			padx=PADDING, 
			pady=PADDING
		)

		login_button.grid(
			row=3, 
			column=0, 
			columnspan=2, 
			padx=PADDING, 
			pady=PADDING
		)
		create_user_button.grid(
			row=4, 
			column=0, 
			columnspan=2, 
			padx=PADDING, 
			pady=PADDING
		)

		# Fill extra space if window is resized
		self._root.grid_columnconfigure(1, weight=1)

	def _handle_login_button(self):
		username = self._username_entry.get()
		password = self._password_entry.get()
		print(' ---> ', username, ' - ', password, ' <--- ')
		self._login_success()

	def _handle_create_user_button(self):
		print('Create new user')
