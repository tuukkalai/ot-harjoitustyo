import os
import sqlite3
from sqlite3.dbapi2 import DatabaseError

class Database:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'test.db'))
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
        except DatabaseError:
            return False
        
    def get_connection(self):
        return self._connection

db = Database()
