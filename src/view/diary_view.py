from tkinter import StringVar, ttk, constants

PADDING = 5

class DiaryView:
	def __init__(self, root, user) -> None:
		self._root = root
		self._frame = None
		self._user = user
		self._initialize()

	def pack(self):
		self._frame.pack(fill=constants.X)

	def destroy(self):
		self._frame.destroy()

	def _initialize(self):
		self._frame = ttk.Frame(master=self._root)

		# Login view items
		heading_label = ttk.Label(master=self._frame, text='Diary')

		user_var = StringVar(self._frame)
		user_info = ttk.Label(
			master=self._frame,
			textvariable=self._user
		)

		heading_label.grid(
			row=0, 
			column=0, 
			sticky=constants.W, 
			padx=PADDING, 
			pady=PADDING
		)

		user_info.grid(
			row=1, 
			column=0, 
			sticky=constants.W, 
			padx=PADDING, 
			pady=PADDING
		)

		self._frame.grid_columnconfigure(1, minsize=400, weight=1)
		self.pack()
