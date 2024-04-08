def polynom(x, *coefs):
    val = coefs[-1]
    for c in coefs[-2::-1]:
        val *= x
        val += c
    return val


# koeficienty polynomu x^2
coefs = (0, 0, 1)

print(polynom(2, *coefs))
