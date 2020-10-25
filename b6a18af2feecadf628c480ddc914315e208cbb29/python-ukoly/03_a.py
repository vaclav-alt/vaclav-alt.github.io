from math import sqrt
# exact solution
phi = 0.5 * (1 + sqrt(5))

max_iterations = 100

# desired precision
precision = 1e-10

# inital fibonacci numbers
f0 = 1
f1 = 1

# initial estimates of phi
phi_est_old = 0
phi_est_new = f1 / f0
# difference between estimates
delta = abs(phi_est_new - phi_est_old)

for i in range(1, max_iterations + 1):
    # calculate the next pair of fibonacci numbers without a helper variable
    f1, f0 = (f1 + f0), f1

    # save the old estimate and get a new one
    phi_est_old = phi_est_new
    phi_est_new = f1 / f0
    # difference between estimates
    delta = abs(phi_est_new - phi_est_old)

    """
    if delta < precision, desired precision is reached and calculation ends, 
    in other words the difference between the two estimates is smaller
    than 1e-10, which means that the first 10 digits are accurate
    """
    if delta < precision:
        break
else:
    print("Iterations exceeded before precision was reached")

print("Terminated after %d iterations" % i)
print("Estimate:\t%.15f" % phi_est_new)
print("Exact value:\t%.15f" % phi)
dif = abs(phi-phi_est_new)
print("Difference:\t%.15f = %.5e" % (dif, dif))
														    
