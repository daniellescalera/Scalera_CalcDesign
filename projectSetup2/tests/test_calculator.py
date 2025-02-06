"""Test suite for the calculator module."""


from calculator import add, subtract

def test_addition():
    """test the addition function."""
    assert add(2,2) == 4

def test_subtraction():
    """test the subtraction function."""
    assert subtract(2,2) == 0
