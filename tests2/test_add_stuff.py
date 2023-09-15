from Class_chinchin import math_func


def test_addition():
    assert math_func.math_func(7, 3) == 10
    assert math_func.math_func(17, 3) == 20


def test_subtract():
    assert math_func.subtract(3, 7) == -4

def test_divide():
    assert math_func.divide(9, 3) == 3
