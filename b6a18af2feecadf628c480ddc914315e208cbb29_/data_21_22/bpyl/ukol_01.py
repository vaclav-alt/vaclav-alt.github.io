from math import sqrt

def is_prime(n):
    upper_limit = int(sqrt(n))
    prime = True
    for i in range(2, upper_limit+1):
        if (n % i) == 0:
            prime = False
            break
    return prime


def get_n_primes(n, maxit = 1000):
    primes = []

    it = 1
    while len(primes) < n and it < maxit:
        it += 1
        is_prime = True
        for i in primes:
            if it % i == 0:
                is_prime = False

        if is_prime:
            primes.append(it)

    return primes


def get_primes_under_n(n):
    nums = list(range(2, n+1))

    for i, x in enumerate(nums):
        for j in range(i):
            y = nums[j]
            if y != 0:
                if x % y == 0:
                    nums[i] = 0
                    break

    return [x for x in nums if x != 0]
