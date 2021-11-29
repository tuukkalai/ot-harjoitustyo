from tkinter import ttk, constants
# from services.diary_service import InvalidPasswordError, InvalidUsernameError 

PADDING = 5

class LoginView:
	def __init__(self, root, login, create_user) -> None:
		self._root = root
		self._frame = None
		self._login = login
		self._create_user = create_user
		self._username_entry = None
		self._password_entry = None
		self._initialize()

	def pack(self):
		self._frame.pack(fill=constants.X)

	def destroy(self):
		self._frame.destroy()

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
			command=lambda : self._login(self._username_entry.get(), self._password_entry.get())
		)
		create_user_button = ttk.Button(
			master=self._frame,
			text='Create new user',
			command=lambda : self._create_user()
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
		self.pack()