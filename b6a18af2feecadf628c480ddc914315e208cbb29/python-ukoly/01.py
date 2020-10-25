from math import sqrt
n = 127

upper_limit = int(sqrt(n))
prime = True
for i in range(2, upper_limit+1):
    if (n % i) == 0:
        prime = False
        break

if prime:
    print("%d is a prime" % n)
else:
    print("%d is not a prime" % n)
