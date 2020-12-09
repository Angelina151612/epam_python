import sqlite3
from typing import Tuple


# flake8: noqa: S608
class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    @staticmethod
    def connect_database(database_name: str) -> sqlite3.Cursor:
        conn = sqlite3.connect(database_name)
        return conn.cursor()

    def __len__(self) -> int:
        cursor = TableData.connect_database(self.database_name)
        cursor.execute("SELECT COUNT(*) from " + self.table_name)
        return cursor.fetchone()[0]

    def __getitem__(self, item: str) -> Tuple:
        cursor = TableData.connect_database(self.database_name)
        cursor.execute("SELECT * from " + self.table_name + " WHERE name =?", (item,))
        return cursor.fetchone()

    def __contains__(self, item: str) -> bool:
        cursor = TableData.connect_database(self.database_name)
        cursor.execute("SELECT * from " + self.table_name + " WHERE name =?", (item,))
        return False if cursor.fetchone() is None else True

    def __iter__(self) -> Tuple:
        cursor = TableData.connect_database(self.database_name)
        cursor.execute("SELECT * from " + self.table_name)
        return cursor
