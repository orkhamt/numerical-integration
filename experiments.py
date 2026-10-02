import math
import random
import matplotlib.pyplot as plt
from integration import trapezoid, simpson, monte_carlo, monte_carlo_nd, trapezoid_2d, simpson_2d, trapezoid_nd, simpson_nd

exact = math.e - 1
calls = 0

def counted_exponential(x):
    global calls
    calls = calls + 1
    return math.exp(x)


trap_calls = []
trap_errors = []
for n in [4, 8, 16, 32, 64, 128]:
    calls = 0
    estimate = trapezoid(counted_exponential, 0, 1, n)
    error = abs(estimate - exact) / exact
    print(f"trapezoid calls={calls} estimate={estimate:.6f} error={error:.2e}")
    trap_calls.append(calls)
    trap_errors.append(error)


simp_calls = []
simp_errors = []
for n in [4, 8, 16, 32, 64, 128]:
    calls = 0
    estimate = simpson(counted_exponential, 0, 1, n)
    error = abs(estimate - exact) / exact
    print(f"simpson calls={calls} estimate={estimate:.6f} error={error:.2e}")
    simp_calls.append(calls)
    simp_errors.append(error)


mc_calls = []
mc_errors = []
for n in [4, 8, 16, 32, 64, 128]:
    total_error = 0
    for seed in range(100):
        calls = 0
        random.seed(seed)
        estimate = monte_carlo(counted_exponential, 0, 1, n)
        total_error = total_error + abs(estimate - exact) / exact
    average_error = total_error / 100
    print(f"monte carlo calls={calls} average error={average_error:.2e}")
    mc_calls.append(calls)
    mc_errors.append(average_error)


plt.loglog(trap_calls, trap_errors, "o-", label="trapezoid")
plt.loglog(simp_calls, simp_errors, "o-", label="simpson")
plt.loglog(mc_calls, mc_errors, "o-", label="monte carlo")
plt.xlabel("calls to f")
plt.ylabel("relative error")
plt.legend()
plt.savefig("error_vs_calls.png")


def counted_exponential_nd(point):
    global calls
    calls = calls + 1
    return math.exp(sum(point))

exact_2d = (math.e - 1) ** 2


trap_2d_calls = []
trap_2d_errors = []
for n in [4, 8, 16, 32, 64, 128]:
    calls = 0
    estimate = trapezoid_2d(counted_exponential_nd, n)
    error = abs(estimate - exact_2d) / exact_2d
    print(f"trapezoid 2d calls={calls} estimate={estimate:.6f} error={error:.2e}")
    trap_2d_calls.append(calls)
    trap_2d_errors.append(error)


simp_2d_calls = []
simp_2d_errors = []
for n in [4, 8, 16, 32, 64, 128]:
    calls = 0
    estimate = simpson_2d(counted_exponential_nd, n)
    error = abs(estimate - exact_2d) / exact_2d
    print(f"simpson 2d calls={calls} estimate={estimate:.6f} error={error:.2e}")
    simp_2d_calls.append(calls)
    simp_2d_errors.append(error)


mc_2d_calls = []
mc_2d_errors = []
# n chosen so Monte Carlo makes about as many calls as the grids, which make (n + 1)^2
for n in [16, 64, 256, 1024, 4096, 16384]:
    total_error = 0
    for seed in range(100):
        calls = 0
        random.seed(seed)
        estimate = monte_carlo_nd(counted_exponential_nd, 2, n)
        total_error = total_error + abs(estimate - exact_2d) / exact_2d
    average_error = total_error / 100
    print(f"monte carlo 2d calls={calls} average error={average_error:.2e}")
    mc_2d_calls.append(calls)
    mc_2d_errors.append(average_error)


plt.figure()
plt.loglog(trap_2d_calls, trap_2d_errors, "o-", label="trapezoid 2d")
plt.loglog(simp_2d_calls, simp_2d_errors, "o-", label="simpson 2d")
plt.loglog(mc_2d_calls, mc_2d_errors, "o-", label="monte carlo 2d")
plt.xlabel("calls to f")
plt.ylabel("relative error")
plt.legend()
plt.savefig("error_vs_calls_2d.png")


trap_all_calls = []
trap_all_errors = []
plt.figure()
for d in [1, 2, 3, 4]:
    exact_nd = (math.e - 1) ** d
    trap_nd_calls = []
    trap_nd_errors = []
    for n in [2, 4, 8, 16]:
        calls = 0
        estimate = trapezoid_nd(counted_exponential_nd, d, n)
        error = abs(estimate - exact_nd) / exact_nd
        print(f"trapezoid {d}d calls={calls} estimate={estimate:.6f} error={error:.2e}")
        trap_nd_calls.append(calls)
        trap_nd_errors.append(error)
    plt.loglog(trap_nd_calls, trap_nd_errors, "o-", label=f"trapezoid {d}d")
    trap_all_calls.append(trap_nd_calls)
    trap_all_errors.append(trap_nd_errors)
plt.xlabel("calls to f")
plt.ylabel("relative error")
plt.legend()
plt.savefig("trapezoid_by_dimension.png")


simp_all_calls = []
simp_all_errors = []
plt.figure()
for d in [1, 2, 3, 4]:
    exact_nd = (math.e - 1) ** d
    simp_nd_calls = []
    simp_nd_errors = []
    for n in [2, 4, 8, 16]:
        calls = 0
        estimate = simpson_nd(counted_exponential_nd, d, n)
        error = abs(estimate - exact_nd) / exact_nd
        print(f"simpson {d}d calls={calls} estimate={estimate:.6f} error={error:.2e}")
        simp_nd_calls.append(calls)
        simp_nd_errors.append(error)
    plt.loglog(simp_nd_calls, simp_nd_errors, "o-", label=f"simpson {d}d")
    simp_all_calls.append(simp_nd_calls)
    simp_all_errors.append(simp_nd_errors)
plt.xlabel("calls to f")
plt.ylabel("relative error")
plt.legend()
plt.savefig("simpson_by_dimension.png")


mc_all_calls = []
mc_all_errors = []
plt.figure()
for d in [1, 2, 3, 4]:
    exact_nd = (math.e - 1) ** d
    mc_nd_calls = []
    mc_nd_errors = []
    # grid_n is the grid size. Monte Carlo gets as many points as the grid makes calls.
    for grid_n in [2, 4, 8, 16]:
        n = (grid_n + 1) ** d
        total_error = 0
        for seed in range(100):
            calls = 0
            random.seed(seed)
            estimate = monte_carlo_nd(counted_exponential_nd, d, n)
            total_error = total_error + abs(estimate - exact_nd) / exact_nd
        average_error = total_error / 100
        print(f"monte carlo {d}d calls={calls} average error={average_error:.2e}")
        mc_nd_calls.append(calls)
        mc_nd_errors.append(average_error)
    plt.loglog(mc_nd_calls, mc_nd_errors, "o-", label=f"monte carlo {d}d")
    mc_all_calls.append(mc_nd_calls)
    mc_all_errors.append(mc_nd_errors)
plt.xlabel("calls to f")
plt.ylabel("relative error")
plt.legend()
plt.savefig("monte_carlo_by_dimension.png")


plt.figure(figsize=(10, 8))
for d in [1, 2, 3, 4]:
    # lists start at 0, so dimension d is at position d - 1
    i = d - 1
    plt.subplot(2, 2, d)
    plt.loglog(trap_all_calls[i], trap_all_errors[i], "o-", label="trapezoid")
    plt.loglog(simp_all_calls[i], simp_all_errors[i], "o-", label="simpson")
    plt.loglog(mc_all_calls[i], mc_all_errors[i], "o-", label="monte carlo")
    plt.title(f"{d}d")
    plt.xlabel("calls to f")
    plt.ylabel("relative error")
    plt.legend()
plt.tight_layout()
plt.savefig("error_vs_calls_by_dimension.png")


plt.figure(figsize=(10, 4))
panel = 0
for d in [6, 8]:
    panel = panel + 1
    exact_nd = (math.e - 1) ** d
    trap_nd_calls = []
    trap_nd_errors = []
    simp_nd_calls = []
    simp_nd_errors = []
    mc_nd_calls = []
    mc_nd_errors = []
    # only small grids, bigger ones take too long in 6d and 8d
    for grid_n in [2, 4]:
        calls = 0
        estimate = trapezoid_nd(counted_exponential_nd, d, grid_n)
        error = abs(estimate - exact_nd) / exact_nd
        print(f"trapezoid {d}d calls={calls} estimate={estimate:.6f} error={error:.2e}")
        trap_nd_calls.append(calls)
        trap_nd_errors.append(error)

        calls = 0
        estimate = simpson_nd(counted_exponential_nd, d, grid_n)
        error = abs(estimate - exact_nd) / exact_nd
        print(f"simpson {d}d calls={calls} estimate={estimate:.6f} error={error:.2e}")
        simp_nd_calls.append(calls)
        simp_nd_errors.append(error)

        n = (grid_n + 1) ** d
        total_error = 0
        # 10 runs instead of 100, or this takes too long
        for seed in range(10):
            calls = 0
            random.seed(seed)
            estimate = monte_carlo_nd(counted_exponential_nd, d, n)
            total_error = total_error + abs(estimate - exact_nd) / exact_nd
        average_error = total_error / 10
        print(f"monte carlo {d}d calls={calls} average error={average_error:.2e}")
        mc_nd_calls.append(calls)
        mc_nd_errors.append(average_error)
    plt.subplot(1, 2, panel)
    plt.loglog(trap_nd_calls, trap_nd_errors, "o-", label="trapezoid")
    plt.loglog(simp_nd_calls, simp_nd_errors, "o-", label="simpson")
    plt.loglog(mc_nd_calls, mc_nd_errors, "o-", label="monte carlo")
    plt.title(f"{d}d")
    plt.xlabel("calls to f")
    plt.ylabel("relative error")
    plt.legend()
plt.tight_layout()
plt.savefig("error_vs_calls_high_dimension.png")