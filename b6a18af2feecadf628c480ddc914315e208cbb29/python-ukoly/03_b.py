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

iteration = 1

while (delta > precision) and iteration <= max_iterations:
    # calculate the next pair of fibonacci numbers without a helper variable
    f1, f0 = (f1 + f0), f1

    # save the old estimate and get a new one
    phi_est_old = phi_est_new
    phi_est_new = f1 / f0
    # difference between estimates
    delta = abs(phi_est_new - phi_est_old)

    iteration += 1
else:
    print("Stopped at iteration %d" % (iteration-1))

print("Estimate:\t%.15f" % phi_est_new)
print("Exact value:\t%.15f" % phi)
dif = abs(phi-phi_est_new)
print("Difference:\t%.15f = %.5e" % (dif, dif))
