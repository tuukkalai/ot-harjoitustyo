from tkinter import StringVar, ttk, constants, Text, messagebox
from entities.entry import Entry

PADDING = 5


class EntryView:
    def __init__(self, root, entry, save_exit, cancel, delete) -> None:
        self._root = root
        self._frame = None
        self._entry = entry
        self._entry_heading_var = StringVar()
        self._entry_heading_var.set(self._entry.heading)
        self._entry_categories_var = StringVar()
        self._entry_categories_var.set(",".join(self._entry.categories))
        self._save_exit = save_exit
        self._cancel = cancel
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

        entry_categories_label = ttk.Label(
            master=self._frame, text='Categories')
        entry_categories_entry = ttk.Entry(
            master=self._frame,
            textvariable=self._entry_categories_var
        )

        save_exit_button = ttk.Button(
            master=self._frame,
            text='Save and exit',
            command=lambda: self._save_exit(
                Entry(
                    self._entry._id,
                    self._entry_heading_var.get(),
                    entry_content_entry.get('1.0', 'end').strip(),
                    self._entry_categories_var.get()
                ), True
            )
        )

        save_button = ttk.Button(
            master=self._frame,
            text='Save',
            command=lambda: self._save_exit(
                Entry(
                    self._entry._id,
                    self._entry_heading_var.get(),
                    entry_content_entry.get('1.0', 'end').strip(),
                    self._entry_categories_var.get()
                ), False
            )
        )

        cancel_button = ttk.Button(
            master=self._frame,
            text='Cancel',
            command=lambda: self._cancel()
        )

        delete_button = ttk.Button(
            master=self._frame,
            text='Delete',
            command=lambda: self._delete_prompt()
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
            columnspan=4,
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
            rowspan=5,
            column=1,
            columnspan=4,
            sticky=constants.EW,
            padx=PADDING,
            pady=PADDING
        )

        entry_categories_label.grid(
            row=6,
            column=0,
            sticky=constants.NW,
            padx=PADDING,
            pady=PADDING
        )

        entry_categories_entry.grid(
            row=6,
            column=1,
            columnspan=4,
            sticky=constants.EW,
            padx=PADDING,
            pady=PADDING
        )

        save_exit_button.grid(row=7, column=4, sticky=constants.E,
                              padx=PADDING, pady=PADDING)

        save_button.grid(row=7, column=3, sticky=constants.E,
                         padx=PADDING, pady=PADDING)

        cancel_button.grid(row=7, column=2, sticky=constants.E,
                           padx=PADDING, pady=PADDING)

        delete_button.grid(row=7, column=1, sticky=constants.E,
                           padx=PADDING, pady=PADDING)

        self._frame.grid_columnconfigure(1, minsize=200, weight=1)
        self.pack()
