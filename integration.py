def trapezoid(f, a, b, n):
    """Estimate the area under f from a to b using n trapezoids."""
    h = (b-a) / n
    total = 0
    for k in range(n):
        left = a + k * h
        right = a + (k+1) * h
        total = total + (f(left) + f(right)) / 2
    return h * total