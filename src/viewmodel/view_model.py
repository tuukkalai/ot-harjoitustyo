import tkinter

from model.user_model import UserModel
from view.login_view import LoginView
from view.create_user_view import CreateUser
from view.diary_view import DiaryView

class ViewModel:
    def __init__(self):
        self.root = tkinter.Tk()
        self.user_model = UserModel()
        self.login_view = LoginView(self.root, self.login, self.show_create_user_view)
        self.__current_view = self.login_view
        self._user_logged_in = None

    def run(self):
        self.root.title('PyDiary')
        self.root.mainloop()

    def hide_current_view(self):
        if self._user_logged_in:
            print(self._user_logged_in.username)
        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def show_login_view(self):
        self.hide_current_view()
        self.__current_view = LoginView(self.root, self.login, self.show_create_user_view)
        self.__current_view.pack()

    def show_create_user_view(self):
        self.hide_current_view()
        self.__current_view = CreateUser(self.root, self.create_user, self.show_login_view)
        self.__current_view.pack()

    def show_diary_view(self):
        self.hide_current_view()
        self.__current_view = DiaryView(self.root, self._user_logged_in)
        self.__current_view.pack()

    def login(self, username, password):
        try:
            self._user_logged_in = self.user_model.login(username, password)
            self.show_diary_view()
        except ValueError:
            print('error')

    def create_user(self, username, password_1, password_2):
        print('creating user', username, password_1, password_2)


        