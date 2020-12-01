from hw.hw_06_task_02 import DeadlineError, HomeworkResult, Student, Teacher

import pytest


@pytest.fixture()
def opp_teacher():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture()
def advanced_python_teacher():
    return Teacher("Aleksandr", "Smetanin")


@pytest.fixture()
def lazy_student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def good_student():
    return Student("Lev", "Sokolov")


@pytest.fixture()
def expired_homework(opp_teacher):
    return opp_teacher.create_homework("Learn functions", 0)


@pytest.fixture()
def oop_hw(opp_teacher):
    return opp_teacher.create_homework("Learn OOP", 1)


@pytest.fixture()
def docs_hw(opp_teacher):
    return opp_teacher.create_homework("Read docs", 5)


def test_create_teacher(opp_teacher):
    assert opp_teacher.first_name == "Daniil"
    assert opp_teacher.last_name == "Shadrin"


def test_create_student(lazy_student):
    assert lazy_student.first_name == "Roman"
    assert lazy_student.last_name == "Petrov"


def test_do_current_homework(good_student, docs_hw):
    hw = good_student.do_homework(docs_hw, "I have done this hw.")
    assert isinstance(hw, HomeworkResult)
    assert hw.author is good_student
    assert hw.solution == "I have done this hw."
    assert hw.homework is docs_hw


def test_do_expired_homework(lazy_student, expired_homework):
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(expired_homework, "I really tried.")


def test_add_only_unique_solution_to_homework_done(
    advanced_python_teacher, opp_teacher, good_student, oop_hw
):
    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    assert opp_teacher.check_homework(result_1) is True
    temp_1 = opp_teacher.homework_done
    assert advanced_python_teacher.check_homework(result_1) is False
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_not_a_homework_object():
    with pytest.raises(TypeError, match="You gave a not Homework object."):
        HomeworkResult(good_student, "fff", "Solution")


@pytest.fixture()
def _homeworks(opp_teacher, good_student, oop_hw, docs_hw):
    hw1 = good_student.do_homework(oop_hw, "I have done this hw")
    hw2 = good_student.do_homework(docs_hw, "And also this")
    opp_teacher.check_homework(hw1)
    opp_teacher.check_homework(hw2)


@pytest.mark.usefixtures("_homeworks")
def test_delete_hw_from_homework_done(oop_hw, docs_hw):
    all_homeworks = Teacher.homework_done
    assert oop_hw in all_homeworks
    Teacher.reset_results(oop_hw)
    assert oop_hw not in all_homeworks


def test_delete_all_hw_from_homework_done(oop_hw, docs_hw):
    Teacher.reset_results()
    assert not bool(Teacher.homework_done)
