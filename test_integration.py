import pytest
import random
import math
from integration import trapezoid, simpson, monte_carlo, monte_carlo_nd, trapezoid_2d, simpson_2d, trapezoid_nd, simpson_nd


def square(x):
    return x ** 2

def test_trapezoid_square_on_1_to_3():
    estimate = trapezoid(square, 1, 3, 1000)
    assert estimate == pytest.approx(26/3, rel=1e-3)

def test_simpson_square_on_1_to_3():
    estimate = simpson(square, 1, 3, 1000)
    assert estimate == pytest.approx(26/3, rel=1e-3)

def test_monte_carlo_square_on_1_to_3():
    random.seed(0)
    estimate = monte_carlo(square, 1, 3, 100_000)
    assert estimate == pytest.approx(26/3, rel=1e-2)


def exponential(x):
    return math.exp(x)

def test_trapezoid_exponential():
    estimate = trapezoid(exponential, 0, 1, 1000)
    assert estimate == pytest.approx(math.e - 1, rel=1e-3)

def test_simpson_exponential():
    estimate = simpson(exponential, 0, 1, 1000)
    assert estimate == pytest.approx(math.e-1, rel=1e-3)

def test_monte_carlo_exponential():
    random.seed(0)
    estimate = monte_carlo(exponential, 0, 1, 1000)
    assert estimate == pytest.approx(math.e-1, rel=1e-2)


def exponential_nd(point):
    return math.exp(sum(point))

def test_monte_carlo_nd():
    random.seed(0)
    estimate = monte_carlo_nd(exponential_nd, 2, 100_000)
    exact = (math.e - 1) ** 2
    assert estimate == pytest.approx(exact, rel=1e-2)

def test_trapezoid_2d():
    estimate = trapezoid_2d(exponential_nd, 100)
    exact = (math.e - 1) ** 2
    assert estimate == pytest.approx(exact, rel=1e-3)

def test_simpson_2d():
    estimate = simpson_2d(exponential_nd, 100)
    exact = (math.e - 1) ** 2
    assert estimate == pytest.approx(exact, rel=1e-3)

def test_trapezoid_nd():
    estimate = trapezoid_nd(exponential_nd, 3, 30)
    exact = (math.e - 1) ** 3
    assert estimate == pytest.approx(exact, rel=1e-3)

def test_simpson_nd():
    estimate = simpson_nd(exponential_nd, 3, 10)
    exact = (math.e - 1) ** 3
    assert estimate == pytest.approx(exact, rel=1e-3)