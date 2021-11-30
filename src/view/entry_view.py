from tkinter import StringVar, ttk, constants, Text
from entities.entry import Entry

PADDING = 5

class EntryView:
	def __init__(self, root, entry, save) -> None:
		self._root = root
		self._frame = None
		self._entry = entry
		self._entry_heading_var = StringVar()
		self._entry_heading_var.set(self._entry._heading)
		self._save = save
		self._initialize()

	def pack(self):
		self._frame.pack(fill=constants.X)

	def destroy(self):
		self._frame.destroy()

	def _initialize(self):
		self._frame = ttk.Frame(master=self._root)

		entry_heading_label = ttk.Label(master=self._frame, text='Heading')
		entry_heading_entry = ttk.Entry(
			master=self._frame, 
			textvariable=self._entry_heading_var
		)

		entry_content_label = ttk.Label(master=self._frame, text='Content')
		entry_content_entry = Text(
			master=self._frame 
		)
		entry_content_entry.insert('1.0', self._entry._content)

		save_button = ttk.Button(
			master=self._frame, 
			text='Save and exit', 
			command=lambda : self._save(
				Entry(
					self._entry._id, 
					self._entry_heading_var.get(), 
					entry_content_entry.get('1.0', 'end')
				)
			)
		)

		entry_heading_label.grid(
			row=0, 
			column=0, 
			sticky=constants.W, 
			padx=PADDING, 
			pady=PADDING
		)

		entry_heading_entry.grid(
			row=0,
			column=1,
			sticky=constants.EW,
			padx=PADDING,
			pady=PADDING
		)

		entry_content_label.grid(
			row=1, 
			column=0, 
			sticky=constants.NW, 
			padx=PADDING, 
			pady=PADDING
		)

		entry_content_entry.grid(
			row=1,
			rowspan=6,
			column=1,
			sticky=constants.EW,
			padx=PADDING,
			pady=PADDING
		)

		save_button.grid(row=7, column=1, sticky=constants.E, padx=PADDING, pady=PADDING)

		self._frame.grid_columnconfigure(1, minsize=400, weight=1)
		self.pack()
