import pytest
import random
import math
from integration import trapezoid, simpson, monte_carlo, monte_carlo_nd

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


def exponential(x):
    return math.exp(x)

def test_trapezoid_exponential():
    result = trapezoid(exponential, 0, 1, 1000)
    assert result == pytest.approx(math.e - 1, rel=1e-3)

def test_simpson_exponential():
    result = simpson(exponential, 0, 1, 1000)
    assert result == pytest.approx(math.e-1, rel=1e-3)

def test_monte_carlo_exponential():
    random.seed(0)
    result = monte_carlo(exponential, 0, 1, 1000)
    assert result == pytest.approx(math.e-1, rel=1e-2)


def exponential_nd(point):
    return math.exp(sum(point))

def test_monte_carlo_nd():
    random.seed(0)
    estimate = monte_carlo_nd(exponential_nd, 2, 100_000)
    result = (math.e - 1) ** 2
    assert estimate == pytest.approx(result, rel=1e-2)