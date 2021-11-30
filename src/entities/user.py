class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username

    def __str__(self):
        return f'({self.id}) {self.username}'
