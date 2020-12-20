from hw.hw_04_task_05 import fizzbuzz


def test_fizzbuzz_gen():
    assert list(fizzbuzz(5)) == ["1", "2", "Fizz", "4", "Buzz"]
