from tkinter import StringVar, ttk, constants

PADDING = 5


class DiaryView:
    def __init__(self, root, user, entries, open_entry, new_entry, logout) -> None:
        self._root = root
        self._frame = None
        self._user = user
        self._entries = entries
        self._open_entry = open_entry
        self._new_entry = new_entry
        self._logout = logout
        self._error_label = None
        self._error_variable = None
        self._categories_dropdown_var = StringVar()
        self.__filter = 'all'
        self.__initialize(self.__filter)

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def show_error(self, error_message):
        self._error_variable.set(error_message)
        self._error_label.grid()

    def hide_error(self):
        self._error_label.grid_remove()

    def _generate_category_list(self) -> list:
        categories_in_diary = ['Filter by category', 'all']
        for entry in self._entries:
            for category in entry.categories:
                if category not in categories_in_diary:
                    categories_in_diary.append(category)
        return categories_in_diary

    def _filter_by_category(self, filter_cat):
        self.__filter = filter_cat
        self.destroy()
        self.__initialize(self.__filter)

    def __initialize(self, cat_filter):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text=f'{self._user.username}\'s diary')

        heading_label.grid(
            row=1,
            column=0,
            sticky=constants.W,
            padx=PADDING,
            pady=PADDING
        )

        new_entry_button = ttk.Button(
            self._frame,
            text='+ New entry',
            command=self._new_entry
        )

        new_entry_button.grid(
            row=1, column=1, sticky=constants.W)

        self._categories_dropdown_var.set(self._generate_category_list()[0])
        categories_dropdown = ttk.OptionMenu(
            self._frame,
            self._categories_dropdown_var,
            *self._generate_category_list(),
            command=lambda x: self._filter_by_category(x)
        )

        categories_dropdown.grid(
            row=1,
            column=2,
            sticky=constants.W,
            padx=PADDING,
            pady=PADDING
        )

        logout_button = ttk.Button(
            master=self._frame, text='Logout', command=lambda: self._logout())

        logout_button.grid(
            row=1,
            column=3,
            sticky=constants.E,
            padx=PADDING,
            pady=PADDING
        )

        i = 1

        filtered_entries = filter(
            lambda entry: self.__filter in entry.categories, self._entries)
        if self.__filter == 'all':
            filtered_entries = self._entries
        for entry in filtered_entries:
            i += 1
            button = ttk.Button(
                self._frame,
                text=f'{entry._heading}\n{entry._content[:32]+"..." if len(entry._content) > 35 else entry._content}',
                command=lambda x=entry: self._open_entry(x)
            )
            button.grid(row=i, column=0, columnspan=4, sticky=constants.EW)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='#dd3333'
        )

        self._error_label.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky=constants.EW,
            padx=PADDING,
            pady=PADDING
        )

        self._frame.grid_columnconfigure(0, minsize=400, weight=1)
        self.pack()
