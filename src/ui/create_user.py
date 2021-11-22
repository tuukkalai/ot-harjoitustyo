from tkinter import ttk, constants

PADDING = 5

class CreateUser:
	def __init__(self, root, create_success, cancel) -> None:
		self._root = root
		self._frame = None
		self._create_success = create_success
		self._cancel = cancel
		self._username_entry = None
		self._password_entry_1 = None
		self._password_entry_2 = None
		self.initialize()

	def initialize(self):
		self._frame = ttk.Frame(master=self._root)
		# Create user view items
		heading_label = ttk.Label(master=self._frame, text='Create new user')

		username_label = ttk.Label(master=self._frame, text='Username')
		self._username_entry = ttk.Entry(master=self._frame)

		password_label_1 = ttk.Label(master=self._frame, text='Password')
		self._password_entry_1 = ttk.Entry(master=self._frame, show='*')
		password_label_2 = ttk.Label(master=self._frame, text='Password again')
		self._password_entry_2 = ttk.Entry(master=self._frame, show='*')

		create_user_button = ttk.Button(
			master=self._frame, 
			text='Create user',
			command=lambda : self._handle_create_user()
		)
		cancel_button = ttk.Button(
			master=self._frame,
			text='Cancel',
			command=lambda : self._cancel()
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

		password_label_1.grid(
			row=2, 
			column=0, 
			padx=PADDING, 
			pady=PADDING
		)
		self._password_entry_1.grid(
			row=2, 
			column=1, 
			sticky=constants.W, 
			padx=PADDING, 
			pady=PADDING
		)
		password_label_2.grid(
			row=3, 
			column=0, 
			padx=PADDING, 
			pady=PADDING
		)
		self._password_entry_2.grid(
			row=3, 
			column=1, 
			sticky=constants.W, 
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
		cancel_button.grid(
			row=5, 
			column=0, 
			columnspan=2, 
			padx=PADDING, 
			pady=PADDING
		)

		# Fill extra space if window is resized
		self._frame.grid_columnconfigure(1, weight=1)
		self._frame.pack(fill=constants.X)

	def _handle_create_user(self):
		print('Create new user')

	def destroy(self):
		self._frame.destroy()