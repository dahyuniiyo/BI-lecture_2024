import pytest


def test_function():
    assert (1, 2, 3) == (1, 2, 3)
    # True이면 pass


def test_function2():
    assert (1, 2, 3) == (1, 4, 3)


# pytest를 실행하면 test로 시작하는 함수를 찾음
# pytest test_function.py // python -m pytest test_function.py 같은 말
