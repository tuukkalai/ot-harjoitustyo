import tkinter
import platform

from model.user_model import (
    UserModel,
    InvalidCredentialsError,
    PasswordMismatchError,
    UsernameAlreadyExistsError,
    WrongUsernamePasswordError
)
from model.diary_model import DeleteEntryError, DiaryModel
from view.login_view import LoginView
from view.create_user_view import CreateUserView
from view.diary_view import DiaryView
from view.entry_view import EntryView


class ViewModel:
    """ViewModel class that handles requests to backend (models) and injects values and methods to frontend (views).
    """

    def __init__(self):
        """Class constructor that initializes the TkInter frontend and models.
        """
        self.root = tkinter.Tk()
        if platform.system() != "Darwin":
            self.root.config(background='#555555')
            style = tkinter.ttk.Style()
            style.configure('TFrame', background='#555555')
            style.configure('TLabel', background='#555555',
                            foreground='#F5F5F5')
            style.configure('TButton', background='#222222',
                            foreground='#F5F5F5', borderwidth=0)
            style.map('TButton', background=[
                      ('active', '!disabled', '#333333')])
        self.user_model = UserModel()
        self.diary_model = DiaryModel()
        self.login_view = LoginView(
            self.root,
            self.login,
            self.show_create_user_view
        )
        self.__current_view = self.login_view
        self._user_logged_in = None

    def run(self):
        """Adds name for the application and starts the application loop.
        """

        self.root.title('PyDiary')
        self.root.mainloop()

    def hide_current_view(self):
        """Destroys the view currently in view.
        """

        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def show_login_view(self):
        """Hides the current view and sets LoginView as a current view.
        """

        self.hide_current_view()
        self.__current_view = LoginView(
            self.root,
            self.login,
            self.show_create_user_view
        )
        self.__current_view.pack()

    def show_create_user_view(self):
        """Hides the current view and sets CreateUserView as a current view.
        """

        self.hide_current_view()
        self.__current_view = CreateUserView(
            self.root,
            self.create_user,
            self.show_login_view
        )
        self.__current_view.pack()

    def show_diary_view(self):
        """Hides the current view and sets DiaryView as a current view.
        """

        if self._user_logged_in:
            self.hide_current_view()
            entries = self.diary_model.get_user_entries(self._user_logged_in)
            self.__current_view = DiaryView(
                self.root,
                self._user_logged_in,
                entries,
                self.show_entry_view,
                self.create_entry,
                self.logout
            )
            self.__current_view.pack()
        else:
            self.show_login_view()
            self.__current_view.show_error('No user logged in')

    def show_entry_view(self, entry):
        """Hides the current view and sets EntryView with selected entry as a current view.

        Args:
            entry (Entry): Entry objects that is opened in editable format in EntryView.
        """

        self.hide_current_view()
        self.__current_view = EntryView(
            self.root,
            entry,
            self.save_entry,
            self.show_diary_view,
            self.delete_entry
        )
        self.__current_view.pack()

    def login(self, username, password):
        """Injected method to LoginView that verifies the inserted user credentials from UserModel. In case of Exception, shows corresponding error message to current view.

        Args:
            username (str): Name value for User
            password (str): Password value for User
        """

        try:
            self._user_logged_in = self.user_model.login(username, password)
            self.show_diary_view()
        except WrongUsernamePasswordError:
            self.__current_view.show_error('Wrong username and/or password')
        except InvalidCredentialsError:
            self.__current_view.show_error(
                'Username or password too short, min. 3 characters')

    def logout(self):
        """Injected method to DiaryView that logs out current user.
        """

        if self._user_logged_in:
            self._user_logged_in = None
            self.show_login_view()

    def create_user(self, username, password_1, password_2):
        """Injected method for CreateUserView. create_user sends the inserted username and password values to UserModel, and based on response, sets new user as a current user or shows error message on current view.

        Args:
            username (str): Name value for User
            password_1 (str): Password value for User
            password_2 (str): Password verification value
        """
        try:
            self._user_logged_in = self.user_model.create_user(
                username,
                password_1,
                password_2
            )
            self.diary_model.create_first_entry(self._user_logged_in)
            self.show_diary_view()
        except UsernameAlreadyExistsError:
            self.__current_view.show_error(
                f'Username `{username}` already exists')
        except InvalidCredentialsError:
            self.__current_view.show_error(
                'Username or password too short, min. 3 characters'
            )
        except PasswordMismatchError:
            self.__current_view.show_error('Passwords do not match')

    def save_entry(self, entry, show_diary):
        """Injected method to EntryView. Save entry takes the updated Entry and sends it to DiaryModel.

        Args:
            entry (Entry): Updated Entry object
            show_diary (bool): Switching to DiaryView (True) or stay in EntryView (False)
        """

        self.diary_model.save_entry(entry)
        if show_diary:
            self.show_diary_view()

    def create_entry(self):
        """Injected method DiaryView. Calls DiaryModel create_entry method to create new empty method.
        """

        self.diary_model.create_entry(self._user_logged_in)
        self.show_diary_view()

    def delete_entry(self, entry):
        """Injected method to EntryView. Sends Entry object to DiaryModel delete_entry method and switches the view to DiaryView. If error occurs, shows error message on current view.

        Args:
            entry (Entry): Entry object
        """

        try:
            self.diary_model.delete_entry(self._user_logged_in, entry)
            self.show_diary_view()
        except DeleteEntryError:
            self.show_diary_view()
            self.__current_view.show_error('Error: Entry was already deleted')
