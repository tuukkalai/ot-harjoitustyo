from datetime import datetime
from entities.entry import Entry
from database import db


class DeleteEntryError(Exception):
    pass


class DiaryModel:
    def __init__(self) -> None:
        self._connection = db.get_connection()

    def get_user_entries(self, user) -> list:
        cursor = self._connection.cursor()
        cursor.execute(
            '''SELECT
                id, heading, content, categories, created, updated
            FROM diaries
            WHERE user_id=?''',
            (user.id,)
        )
        rows = cursor.fetchall()
        entries = list(map(lambda entry: Entry(
            entry['id'],
            entry['heading'],
            entry['content'],
            entry['categories'],
            entry['created'],
            entry['updated']), rows)
        )
        return entries

    def create_first_entry(self, user) -> None:
        heading = 'Welcome'
        content = '''This is the welcoming content.
PyDiary is an application to create Diary entries with various topics.
At first it works in simple way, by editing heading and content of the entry.
Thank you for using PyDiary.'''
        cursor = self._connection.cursor()
        date_now = datetime.now().strftime('%d.%m.%Y %H.%M')
        cursor.execute('''INSERT INTO diaries (user_id, heading, content, created, updated)
			VALUES (?,?,?,?,?)
			''', (user.id, heading, content, date_now, date_now)
        )
        self._connection.commit()

    def save_entry(self, entry) -> None:
        cursor = self._connection.cursor()
        cursor.execute('''UPDATE diaries
			SET heading=?, 
			content=?,
            categories=?,
            updated=?
			WHERE id=?''',
                       (
                           entry.heading,
                           entry.content,
                           ",".join(entry.categories),
                           datetime.now().strftime('%d.%m.%Y %H.%M'),
                           entry.id
                       )
                       )
        self._connection.commit()

    def create_entry(self, user) -> None:
        heading = 'New entry'
        content = ''
        date_now = datetime.now().strftime('%d.%m.%Y %H.%M')
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO diaries
            (user_id, heading, content, created, updated)
			VALUES (?,?,?,?,?)''', (user.id, heading, content, date_now, date_now)
                       )
        self._connection.commit()

    def delete_entry(self, user, entry) -> None:
        user_entries_before = self.get_user_entries(user)
        cursor = self._connection.cursor()
        cursor.execute(
            'DELETE FROM diaries WHERE id=? AND user_id=?', (entry.id, user.id)
        )
        self._connection.commit()
        user_entries_after = self.get_user_entries(user)
        if len(user_entries_before) - 1 != len(user_entries_after):
            raise DeleteEntryError('Error: Entry was already deleted')
