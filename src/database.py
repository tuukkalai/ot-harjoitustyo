import os
import sqlite3
import dotenv
from sqlite3.dbapi2 import Error

class Database:
    def __init__(self) -> None:
        dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
        self._connection = sqlite3.connect(
            os.path.join(os.path.dirname(__file__), '..', 'data', os.getenv('DATABASE_FILE'))
        )
        self.init_database()

    def init_database(self) -> bool:
        cursor = self._connection.cursor()

        try:
            cursor.execute(''' CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
                ) ''')
            
            self._connection.commit()

            cursor.execute(''' CREATE TABLE IF NOT EXISTS diaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                heading TEXT NOT NULL,
                content TEXT NOT NULL,
                categories TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
                ) ''')

            self._connection.commit()

            return True
        except Error as e:
            print(e)
            return False
        
    def get_connection(self):
        return self._connection

    def empty_database(self):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM users')
        cursor.execute('DELETE FROM diaries')
        self._connection.commit()

    def delete_database(self):
        try:
            os.remove(os.path.join(os.path.dirname(__file__), '..', 'data', os.getenv('DATABASE_FILE')))
        except Error as e:
            print(e)

db = Database()
