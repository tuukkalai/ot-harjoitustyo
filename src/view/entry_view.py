from tkinter import StringVar, ttk, constants, Text, messagebox
from entities.entry import Entry

PADDING = 5


class EntryView:
    def __init__(self, root, entry, save, delete) -> None:
        self._root = root
        self._frame = None
        self._entry = entry
        self._entry_heading_var = StringVar()
        self._entry_heading_var.set(self._entry._heading)
        self._save = save
        self._delete = delete
        self.__initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def show_error(self, error_message):
        self._error_variable.set(error_message)
        self._error_label.grid()

    def hide_error(self):
        self._error_label.grid_remove()

    def _delete_prompt(self):
        confirmation = messagebox.askyesnocancel(
            title='Confirmation', message='Do you want to delete the note?')
        if confirmation:
            self._delete(self._entry)

    def __initialize(self):
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
            command=lambda: self._save(
                Entry(
                    self._entry._id,
                    self._entry_heading_var.get(),
                    entry_content_entry.get('1.0', 'end').strip()
                )
            )
        )

        delete_button = ttk.Button(
            master=self._frame,
            text='Delete',
            command=lambda: self._delete_prompt()
        )

        entry_heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=constants.W,
            padx=PADDING,
            pady=PADDING
        )

        entry_heading_entry.grid(
            row=0,
            column=1,
            columnspan=2,
            sticky=constants.EW,
            padx=PADDING,
            pady=PADDING
        )

        entry_content_label.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.NW,
            padx=PADDING,
            pady=PADDING
        )

        entry_content_entry.grid(
            row=1,
            rowspan=6,
            column=1,
            columnspan=2,
            sticky=constants.EW,
            padx=PADDING,
            pady=PADDING
        )

        save_button.grid(row=7, column=2, sticky=constants.E,
                         padx=PADDING, pady=PADDING)

        delete_button.grid(row=7, column=1, sticky=constants.E,
                           padx=PADDING, pady=PADDING)

        self._frame.grid_columnconfigure(1, minsize=400, weight=1)
        self.pack()
