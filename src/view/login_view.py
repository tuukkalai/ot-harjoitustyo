from tkinter import StringVar, ttk, constants

PADDING = 5


class LoginView:
    def __init__(self, root, login, create_user) -> None:
        self._root = root
        self._frame = None
        self._login = login
        self._create_user = create_user
        self._username_entry = None
        self._password_entry = None
        self._error_label = None
        self._error_variable = None
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

    def __initialize(self):
        s = ttk.Style()
        s.configure('TFrame', background='#555555')
        s.configure('TLabel', background='#555555', foreground='#F5F5F5')
        s.configure('TButton', background='#222222', foreground='#F5F5F5', borderwidth=0)
        s.map('TButton', background=[('active', '!disabled', '#333333')])
        self._frame = ttk.Frame(master=self._root, padding=10)

        # Login view items
        heading_label = ttk.Label(
            master=self._frame,
            text='Login',
            font=('Arial', 16)
        )

        username_label = ttk.Label(master=self._frame, text='Username')
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text='Password')
        self._password_entry = ttk.Entry(master=self._frame, show='*')

        login_button = ttk.Button(
            master=self._frame,
            text='Login',
            command=lambda: self._login(
                self._username_entry.get(), self._password_entry.get())
        )
        create_user_button = ttk.Button(
            master=self._frame,
            text='Create new user',
            command=lambda: self._create_user()
        )

        heading_label.pack(fill=constants.X)

        username_label.pack(fill=constants.X, padx=2, pady=2)
        
        self._username_entry.pack(fill=constants.X, ipadx=8, ipady=6, padx=2, pady=6)

        password_label.pack(fill=constants.X, padx=2, pady=2)

        self._password_entry.pack(fill=constants.X, ipadx=6, ipady=6, padx=2, pady=6)

        login_button.pack(fill=constants.X, ipadx=6, ipady=6, padx=2, pady=2)

        create_user_button.pack(fill=constants.X, ipadx=6, ipady=6, padx=2, pady=2)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='#dd3333'
        )

        self._error_label.pack()

        self._frame.grid_columnconfigure(1, minsize=300, weight=1, pad=PADDING)
        self.pack()
