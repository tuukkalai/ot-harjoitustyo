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
        self.__initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def __initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text=f'{self._user.username}\'s diary')

        heading_label.grid(
            row=0,
            column=0,
            sticky=constants.W,
            padx=PADDING,
            pady=PADDING
        )

        logout_button = ttk.Button(
            master=self._frame, text='Logout', command=lambda : self._logout())

        logout_button.grid(
            row=0,
            column=2,
            sticky=constants.E,
            padx=PADDING,
            pady=PADDING
        )

        i = 1
        for entry in self._entries:
            i += 1
            button = ttk.Button(
                self._frame,
                text=f'{entry._heading}\n{entry._content[:32]+"..." if len(entry._content) > 35 else entry._content}',
                command=lambda x=entry: self._open_entry(x)
            )
            button.grid(row=i, column=0, sticky=constants.EW)

        button = ttk.Button(
            self._frame,
            text='+ new entry',
            command=lambda x=entry: self._new_entry()
        )
        button.grid(row=i+1, column=0, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, minsize=400, weight=1)
        self.pack()
