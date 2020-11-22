from datetime import timedelta

from hw.hw_05_task_01 import Student, Teacher

import pytest


@pytest.fixture()
def teacher():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture()
def student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def expired_homework(teacher):
    return teacher.create_homework("Learn functions", 0)


@pytest.fixture()
def current_homework(teacher):
    return teacher.create_homework("create 2 simple classes", 5)


def test_create_teacher(teacher):
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_create_student(student):
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_create_homework(expired_homework):
    assert expired_homework.deadline == timedelta(0, 0, 0)
    assert expired_homework.text == "Learn functions"


def test_do_current_homework(student, current_homework):
    assert student.do_homework(current_homework) == current_homework


def test_do_expired_homework(student, expired_homework, capsys):
    assert student.do_homework(expired_homework) is None
    out, err = capsys.readouterr()
    assert out == "You are late\n"
