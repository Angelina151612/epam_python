from hw.hw_03_task_02 import fast_calculate, slow_calculate


def test_fast_calculate():
    res_slow = sum(slow_calculate(i) for i in range(501))
    res_fast = fast_calculate()
    assert res_slow == res_fast
