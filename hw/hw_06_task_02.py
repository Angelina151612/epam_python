"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции (Student, Teacher, Homework).

Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Optional


class DeadlineError(Exception):
    def __init__(self):
        super().__init__("You are late.")


class Person:
    """
    A class to represent a person.

    Attributes
    ----------
    last_name : str
        last name of a person
    first_name: str
        first name of a person

    """

    def __init__(self, first_name: str, last_name: str):
        """Create an instance of a person."""
        self.last_name = last_name
        self.first_name = first_name


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


class Student(Person):
    """
    A class to represent a student.

    Methods
    -------
    do_homework():
        Return homework if deadline is available, raise exception otherwise.

    """

    # flake8: noqa: T001
    def do_homework(self, hw: Homework, solution: str) -> Optional[Homework]:
        """Return None and print message if deadline is passed, an instance of homework otherwise."""
        if not hw.is_active():
            raise DeadlineError()
        return HomeworkResult(self, hw, solution)


class HomeworkResult:
    """
    A class to represent successfully completed homeworks.

    Attributes
    ----------
    homework : Homework
        Homework object
    solution: str
        text of answer
    author : Student
        Student object
    created: datetime.timedelta
        date and time of creation

    """

    def __init__(self, student: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object.")
        self.homework = homework
        self.solution = solution
        self.author = student
        self.created = datetime.now()


class Teacher(Person):
    """
    A class to represent a teacher.

    Methods
    -------
    create_homework():
        Create homework.

    check_homework():
        Check if text of answer is longer than 5 symbols and doesn't duplicate someone else's.
        Add homework to the dict with approved ones and return True afterwards, False in any other cases

    reset_results():
        Delete homework from the dict if argument was given, сlear it otherwise.

    """

    homework_done = defaultdict(list)

    def create_homework(self, text: str, deadline: int) -> Homework:
        """Return an instance of created homework."""
        return Homework(text, deadline)

    def check_homework(self, hw: HomeworkResult) -> bool:
        if len(hw.solution) > 5:
            if not any(hw in s for s in self.homework_done.values()):
                self.homework_done[hw.homework].append(hw)
                return True

        return False

    def reset_results(hw: Optional[Homework] = None) -> None:
        if hw is None:
            Teacher.homework_done.clear()
        else:
            del Teacher.homework_done[hw]
