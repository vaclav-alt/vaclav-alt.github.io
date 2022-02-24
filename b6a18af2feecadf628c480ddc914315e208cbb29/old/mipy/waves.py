import numpy as np

def triangle_wave_i(x, i, a, f0):
    n = 2*i + 1
    return 8.0 * (-1)**i * np.sin(f0 * n * (x - a)) / (n * np.pi)**2

def square_wave_i(x, i, a, f0):
    n = 2*i + 1
    return 4.0 *  np.sin(f0 * n * (x-a)) / n / np.pi

def sawtooth_wave_i(x, i, a, f0):
    i = i + 1
    return 2.0 * (-1)**2 * np.sin(f0 * i * (x - a)) / i / np.pi

def sine_wave_i(x, i, a, f0):
    i = i + 1
    return np.sin(f0 * i * (x - a))


def wave(x, a = 0.0, b = np.pi, f0 = 1, kind = "sine", N = 1, start = 0, sum = True):
    switcher = {
        "triangle" : triangle_wave_i,
        "square"   : square_wave_i,
        "sawtooth"      : sawtooth_wave_i,
        "sine"     : sine_wave_i
    }
    fun = switcher.get(kind, sine_wave_i)
    
    f0 = f0 * 2.0 * np.pi / (b - a)
    xx, ii = np.meshgrid(x, range(start, start + N + 1))
    y = fun(xx, ii, a, f0)
    
    if sum:
        return np.sum(y, 0)
    else:
        return y