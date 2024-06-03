import pytest
from p2420 import absolute_difference


@pytest.mark.parametrize(("A", "B", "expected"), [(-2, 5, 7), (-1, 4, 5), (-1, -2, 3)])
def test_absolute_difference(A, B, expected):
    assert absolute_difference(A, B) == expected
