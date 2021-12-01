from entities.entry import Entry
from database import db


class DiaryModel:
    def __init__(self) -> None:
        self._connection = db.get_connection()

    def get_user_entries(self, user) -> list:
        cursor = self._connection.cursor()
        cursor.execute(
            '''SELECT id, heading, content FROM diaries WHERE user_id=?''',
            (user.id,))
        rows = cursor.fetchall()
        entries = list(map(lambda entry: Entry(
            entry['id'], entry['heading'], entry['content']), rows))
        return entries

    def create_first_entry(self, user) -> None:
        heading = 'Welcome'
        content = '''This is the welcoming content.
        PyDiary is an application to create Diary entries with various topics.
        At first it works in simple way, by editing heading and content of the entry.
        Thank you for using PyDiary.'''
        cursor = self._connection.cursor()
        cursor.execute(''' INSERT INTO diaries (user_id, heading, content)
			VALUES (?,?,?)
			''', (user.id, heading, content))
        self._connection.commit()

    def save_entry(self, entry) -> None:
        cursor = self._connection.cursor()
        cursor.execute('''UPDATE diaries
			SET heading=?, 
			content=? 
			WHERE id=?''', (entry.heading, entry.content, entry.id))
        self._connection.commit()

    def create_entry(self, user) -> None:
        heading = 'New entry'
        content = ''
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO diaries (user_id, heading, content)
			VALUES (?,?,?)''', (user.id, heading, content))
        self._connection.commit()
