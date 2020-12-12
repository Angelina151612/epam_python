import sqlite3
from typing import Callable, Tuple


def connect_database(func: Callable) -> sqlite3.Cursor:
    def wrapper(self, *args, **kwargs):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            return func(self, cursor, *args, **kwargs)

    return wrapper


# flake8: noqa: S608
class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    @connect_database
    def __len__(self, cursor) -> int:
        cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return cursor.fetchone()[0]

    @connect_database
    def __getitem__(self, cursor, item: str) -> Tuple:
        cursor.execute(
            f"SELECT * from  {self.table_name} WHERE name = :item", {"item": item}
        )
        return cursor.fetchone()

    @connect_database
    def __contains__(self, cursor, item: str) -> bool:
        cursor.execute(
            f"SELECT * from {self.table_name} WHERE name =:item", {"item": item}
        )
        return cursor.fetchone()

    @connect_database
    def __iter__(self, cursor) -> Tuple:
        cursor.execute(f"SELECT * from {self.table_name}")
        return cursor
