import tkinter

from model.user_model import (
    UserModel,
    InvalidCredentialsError,
    PasswordMismatchError,
    UsernameAlreadyExistsError,
    UsernameNotExistsError,
    WrongPasswordError
)
from model.diary_model import DiaryModel
from view.login_view import LoginView
from view.create_user_view import CreateUserView
from view.diary_view import DiaryView
from view.entry_view import EntryView


class ViewModel:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('600x600')
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
        self.root.title('PyDiary')
        self.root.mainloop()

    def hide_current_view(self):
        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def show_login_view(self):
        self.hide_current_view()
        self.__current_view = LoginView(
            self.root,
            self.login,
            self.show_create_user_view
        )
        self.__current_view.pack()

    def show_create_user_view(self):
        self.hide_current_view()
        self.__current_view = CreateUserView(
            self.root,
            self.create_user,
            self.show_login_view
        )
        self.__current_view.pack()

    def show_diary_view(self):
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
        self.hide_current_view()
        self.__current_view = EntryView(
            self.root,
            entry,
            self.save_entry
        )
        self.__current_view.pack()

    def login(self, username, password):
        try:
            self._user_logged_in = self.user_model.login(username, password)
            self.show_diary_view()
        except WrongPasswordError:
            self.__current_view.show_error('Wrong password')
        except UsernameNotExistsError:
            self.__current_view.show_error(f'Username `{username}` not found')

    def logout(self):
        if self._user_logged_in:
            self._user_logged_in = None
            self.show_login_view()

    def create_user(self, username, password_1, password_2):
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

    def save_entry(self, entry):
        self.diary_model.save_entry(entry)
        self.show_diary_view()

    def create_entry(self):
        self.diary_model.create_entry(self._user_logged_in)
        self.show_diary_view()
