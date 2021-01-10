import sqlite3


def test_db():
    with sqlite3.connect("hw/homework12/db.sqlite3") as conn:
        cursor = conn.cursor()

    cursor.execute("SELECT * from 'example_teacher'")
    row = cursor.fetchone()
    assert row[1] == "Shadrin"
    assert row[2] == "Daniil"

    cursor.execute("SELECT * from 'example_student'")
    row = cursor.fetchone()
    assert row[1] == "Sokolov"
    assert row[2] == "Lev"

    cursor.execute("SELECT * from 'example_homework'")
    row = cursor.fetchone()
    assert row[1] == "I have done this hw."

    cursor.execute("SELECT * from 'example_homework'")
    row = cursor.fetchone()
    assert row[1] == "I have done this hw."

    cursor.execute("SELECT * from 'example_homeworkresult'")
    row = cursor.fetchone()
    assert row[1] == "I have done this hw."
