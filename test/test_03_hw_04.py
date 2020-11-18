from hw.hw_04_task_03 import my_precious_logger


def test_stdout(capsys):
    text = "Hello, world"
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert out == text
    assert err == ""


def test_stderr(capsys):
    text = "error: file not found"
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert err == text
    assert out == ""


def test_empty_str(capsys):
    text = ""
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert err == ""
    assert out == ""
