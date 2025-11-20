# myapp/tests/test_utils.py (Using pytest style)
from .utils import add, subtract, multiply, divide
import pytest

def test_add_function():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0

def test_subtract_function():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5

def test_multiply_function():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

def test_divide_function():
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5

def test_divide_by_zero_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
