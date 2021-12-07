import os
import sqlite3
from dotenv import load_dotenv


dirname = os.path.dirname(__file__)


class Database:
    def __init__(self) -> None:
        load_dotenv(os.path.join(dirname, '..', '.env'))
        self._connection = sqlite3.connect(
            os.path.join(dirname, '..',
                         'data', os.getenv('DATABASE_FILE'))
        )
        self._connection.row_factory = sqlite3.Row
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
                CONSTRAINT fk_users 
                    FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
                ) ''')

            self._connection.commit()

            cursor.execute('PRAGMA foreign_keys=1')

            self._connection.commit()

            return True
        except sqlite3.Error as error:
            print(error)
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
            os.remove(os.path.join(dirname,
                      '..', 'data', os.getenv('DATABASE_FILE')))
        except sqlite3.Error as error:
            print(error)


db = Database()
