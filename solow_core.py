import numpy as np

def simulate_solow(s, alpha, delta, n, g, k0, T):

    k = np.zeros(T)
    y = np.zeros(T)

    k[0] = k0

    for t in range(T-1):

        y[t] = k[t]**alpha

        investment = s * y[t]
        break_even = (n + g + delta) * k[t]

        k[t+1] = k[t] + investment - break_even

    y[-1] = k[-1]**alpha

    return k, y
