import pytest
import random
from integration import trapezoid, simpson, monte_carlo

def square(x):
    return x ** 2

def test_trapezoid_square_on_1_to_3():
    result = trapezoid(square, 1, 3, 1000)
    assert result == pytest.approx(26/3, rel=1e-3)


def test_simpson_square_on_1_to_3():
    result = simpson(square, 1, 3, 1000)
    assert result == pytest.approx(26/3, rel=1e-3)


def test_monte_carlo_square_on_1_to_3():
    random.seed(0)
    result = monte_carlo(square, 1, 3, 100_000)
    assert result == pytest.approx(26/3, rel=1e-2)