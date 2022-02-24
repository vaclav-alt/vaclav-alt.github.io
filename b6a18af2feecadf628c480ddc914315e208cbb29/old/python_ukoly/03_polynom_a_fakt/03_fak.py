# faktorial
import math
import numpy as np
import matplotlib.pyplot as plt
from time import time

def measure_time(n, fun, n_tries = 10000):
    times = []
    for i in range(n_tries):
        start = time()
        fun(n)
        end = time()
        times.append(end - start)
    return sum(times)/n_tries

def faktorial1(n):
    if n > 1:
        return n * faktorial1(n-1)
    else:
        return 1

def faktorial2(n):
    if n > 1:
        res = 1
        for i in range(2, n+1):
            res *= i
        return res
    return 1

nrange = range(1,21)
times1 = [measure_time(n, faktorial1) for n in nrange]
times2 = [measure_time(n, faktorial2) for n in nrange]
times3 = [measure_time(n, math.factorial) for n in nrange]
times4 = [measure_time(n, np.math.factorial) for n in nrange]

plt.plot(nrange, times1, "-o", label="rekurze")
plt.plot(nrange, times2, "-o", label="for loop")
plt.plot(nrange, times3, "-o", label="math.factorial")
plt.plot(nrange, times4, "--o", label="numpy")
plt.xticks(nrange)
plt.xlabel("n")
plt.ylabel("time(n!) / s")
plt.legend()
plt.yscale('log')
plt.show()
