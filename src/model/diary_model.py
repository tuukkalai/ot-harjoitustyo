from entities.entry import Entry
from database import db

class DiaryModel:
	def __init__(self) -> None:
		self._connection = db.get_connection()

	def _get_users_entries(self, user) -> list:
		cursor = self._connection.cursor()
		cursor.execute(''' SELECT heading
			FROM diaries
			WHERE user_id = ? ''', (user.id,))
		rows = cursor.fetchall()
		print(rows)
		return rows

	def _create_first_entry(self, user):
		heading = 'Welcome'
		content = '''This is the welcoming content.
			PyDiary is an application to create Diary entries with various topics. At first it works in minimalistic simple way, by adding heading and content to the entry.
			Thank you for using PyDiary.'''
		cursor = self._connection.cursor()
		cursor.execute(''' INSERT INTO diaries (user_id, heading, content)
			VALUES (?,?,?)
			''', (user.id, heading, content))
		self._connection.commit()
