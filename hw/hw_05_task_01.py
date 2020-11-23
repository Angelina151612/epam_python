"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher, Homework).

Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from datetime import datetime, timedelta


class Homework:
    """
    A class to represent a homework.

    Attributes
    ----------
    text : str
        text of homework
    deadline: int
        num of days to do homework
    created: datetime.timedelta
        date and time of deadline

    """

    def __init__(self, text: str, deadline: int):
        """Create an instance of a homework."""
        self.text = text
        self.deadline = timedelta(deadline)
        self.created = datetime.now()

    def is_active(self) -> bool:
        """Return False if deadline is expired, True otherwise."""
        hw_deadline = self.created + self.deadline
        now = datetime.now()
        return not now > hw_deadline


class Student:
    """
    A class to represent a student.

    Attributes
    ----------
    last_name : str
        last name of a student
    first_name: str
        first name of a student

    Methods
    -------
    do_homework():
        Return homework if deadline is available, None otherwise.

    """

    def __init__(self, first_name: str, last_name: str):
        """Create an instance of a student."""
        self.last_name = last_name
        self.first_name = first_name

    # flake8: noqa: T001
    def do_homework(self, hw: Homework) -> Homework or None:
        """Return None and print message if deadline is passed, an instance of homework otherwise."""
        if not hw.is_active():
            print("You are late")
            return None
        return hw


class Teacher:
    """
    A class to represent a teacher.

    Attributes
    ----------
    last_name : str
        last name of a teacher
    first_name: str
        first name of a teacher

    Methods
    -------
    create_homework():
        Create homework.

    """

    def __init__(self, first_name: str, last_name: str):
        """Create an instance of a teacher."""
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text: str, deadline: int) -> Homework:
        """Return an instance of created homework."""
        return Homework(text, deadline)
