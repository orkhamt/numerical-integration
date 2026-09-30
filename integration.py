import random

def trapezoid(f, a, b, n):
    """Estimate the area under f from a to b using n trapezoids."""
    h = (b-a) / n
    total = (f(a) + f(b)) / 2
    for k in range(1,n):
        total = total + f(a + k * h)
    return h * total


def simpson(f, a, b, n):
    """Estimate the area under f from a to b using Simpson's rule. n must be even."""
    h = (b - a) / n
    total = 0
    for k in range(0, n, 2):
        left = a + k * h
        middle = a + (k+1) * h
        right = a + (k+2) * h
        total = total + f(left) + 4 * f(middle) + f(right)
    return h / 3 * total


def monte_carlo(f, a, b, n):
    """Estimate the area under f from a to b averaging f at n random points."""
    total = 0
    for i in range(n):
        x = random.uniform(a, b)
        total = total + f(x)
    average = total / n
    return average * (b -a)
