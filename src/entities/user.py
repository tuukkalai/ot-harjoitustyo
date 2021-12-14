class User:
    def __init__(self, user_id: int, username: str) -> None:
        self.__id = user_id
        self.__username = username

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    def __str__(self):
        return f'({self.id}) {self.username}'
