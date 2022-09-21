import pytest

def test_square_area():
    assert square_area(8) == 64
    assert square_area(5) == 25

def square_area(x):
    return x*x

