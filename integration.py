import random
import itertools

def trapezoid(f, a, b, n):
    """Estimate the area under f from a to b using n trapezoids."""
    h = (b-a) / n
    total = (f(a) + f(b)) / 2
    for k in range(1,n):
        total = total + f(a + k * h)
    return h * total


def simpson(f, a, b, n):
    """Estimate the area under f from a to b using Simpson's rule. n must be even."""
    if n % 2 != 0:
        raise ValueError("n must be even")
    h = (b - a) / n
    total = f(a) + f(b)
    for k in range(1, n):
        if k % 2 == 1:
            total = total + 4 * f(a + k * h)
        else:
            total = total + 2 * f(a + k * h)
    return h / 3 * total


def monte_carlo(f, a, b, n):
    """Estimate the area under f from a to b averaging f at n random points."""
    total = 0
    for i in range(n):
        x = random.uniform(a, b)
        total = total + f(x)
    average = total / n
    return average * (b -a)


def monte_carlo_nd(f, d, n):
    """Estimate the volume under f over the unit cube (0 to 1 in eahc direction) by averaging f at n random points."""
    total = 0
    for i in range(n):
        point = []
        for j in range(d):
            point.append(random.uniform(0, 1))
        total += f(point)
    return total / n


def trapezoid_2d(f, n):
    """Estimate the volume under f over the unit square (0 to 1 in each direction) using an n by n grid of trapezoids."""
    h = 1 / n
    total = 0
    for i in range(n + 1):
        for j in range(n + 1):
            weight = 1
            if i == 0 or i == n:
                weight = weight * 0.5
            if j == 0 or j == n:
                weight = weight * 0.5
            total = total + weight * f([i * h, j * h])
    return h * h * total


def simpson_2d(f, n):
    """Estimate the volume under f over the unit square (0 to 1 each direction) using Simpson's rule on an n by n grid. n must be even."""
    if n % 2 != 0:
        raise ValueError("n must be even")
    h = 1 / n
    total = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or i == n:
                weight_i = 1
            elif i % 2 == 1:
                weight_i = 4
            else:
                weight_i = 2
            if j == 0 or j == n:
                weight_j = 1
            elif j % 2 == 1:
                weight_j = 4
            else:
                weight_j = 2
            total = total + weight_i * weight_j * f([i * h, j * h])
    return (h/3) * (h/3) * total
            

def trapezoid_nd(f, d, n):
    """Estimate the volume under f over the unit cube (0 to 1 in each of d directions) using an n by n by ... grid of trapezoids."""
    h = 1 / n
    total = 0
    for labels in itertools.product(range(n + 1), repeat=d):
        weight = 1
        point = []
        for k in labels:
            if k == 0 or k == n:
                weight = weight * 0.5
            point.append(k * h)
        total = total + weight * f(point)
    return h ** d * total