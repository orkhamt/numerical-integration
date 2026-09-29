import pytest
from integration import trapezoid

def square(x):
    return x ** 2

def test_trapezoid_square_on_1_to_3():
    result = trapezoid(square, 1, 3, 1000)
    assert result == pytest.approx(26/3, rel=1e-3)


from integration import trapezoid, simpson

def test_simpson_square_on_1_to_3():
    result = simpson(square, 1, 3, 1000)
    assert result == pytest.approx(26/3, rel=1e-3)
    