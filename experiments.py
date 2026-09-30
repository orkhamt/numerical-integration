import math
import random
from integration import trapezoid, simpson, monte_carlo

exact = math.e - 1
calls = 0 

def counted_exponential(x):
    global calls
    calls = calls + 1
    return math.exp(x)


calls = 0
estimate = trapezoid(counted_exponential, 0, 1, 4)
error = abs(estimate - exact) / exact
print(f"trapezoid calls={calls} estimate={estimate:.6f} error={error:.2e}")


calls = 0
estimate = simpson(counted_exponential, 0, 1, 4)
error = abs(estimate - exact) / exact
print(f"simpson calls={calls} estimate={estimate:.6f} error={error:.2e}")


calls = 0
random.seed(0)
estimate = monte_carlo(counted_exponential, 0, 1, 4)
error = abs(estimate - exact) / exact
print(f"monte carlo calls={calls} estimate={estimate:.6f} error={error:.2e}")
