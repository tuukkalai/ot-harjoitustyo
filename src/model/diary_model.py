from entities.entry import Entry
from database import db

class DiaryModel:
	def __init__(self) -> None:
		self._connection = db.get_connection()

	def _get_user_entries(self, user) -> list:
		cursor = self._connection.cursor()
		rows = cursor.execute(
			'''SELECT id, heading, content FROM diaries WHERE user_id=?''', 
			(user.id,)).fetchall()
		entries = list(
			map(
				lambda entry : Entry(entry['id'], entry['heading'], entry['content']), rows)
			)
		return entries

	def _create_first_entry(self, user):
		heading = 'Welcome'
		content = '''This is the welcoming content.\nPyDiary is an application to create Diary entries with various topics. At first it works in minimalistic simple way, by adding heading and content to the entry.\nThank you for using PyDiary.'''
		cursor = self._connection.cursor()
		cursor.execute(''' INSERT INTO diaries (user_id, heading, content)
			VALUES (?,?,?)
			''', (user.id, heading, content))
		self._connection.commit()

	def _save_entry(self, user, entry):
		cursor = self._connection.cursor()
		cursor.execute('''UPDATE diaries 
			SET heading=?, 
			content=? 
			WHERE id=?''', 
			(entry._heading, entry._content, entry._id)
		)
		self._connection.commit()
