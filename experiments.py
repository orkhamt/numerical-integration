from integration import trapezoid, simpson, monte_carlo

calls = 0 

def counted_square(x):
    global calls
    calls = calls + 1
    return x ** 2

trapezoid(counted_square, 1, 3, 4)
print("calls:", calls)

calls = 0

simpson(counted_square, 1, 3, 4)
print("simpson calls:", calls)

calls = 0

monte_carlo(counted_square, 1, 3, 4)
print("monte carlo calls:", calls)