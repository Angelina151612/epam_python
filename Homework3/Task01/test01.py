from Homework3.Task01.task01 import cache


def test_cache():
    rep = 2

    @cache(rep)
    def f():
        return 'my_decorator'

    val_1 = f()
    val_2 = f()

    assert val_1 is val_2