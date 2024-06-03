import pytest
from p1000 import add

# import할 때 숫자로 시작하면 안됨!

"""
def test_add():
    assert add(1, 2) == 3
"""


@pytest.mark.parametrize(("a", "b", "expected"), [(1, 2, 3), (3, 4, 7), (5, 6, 11)])
def test_add(a, b, expected):
    assert add(a, b) == expected
