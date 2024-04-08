from math import log

# p.a. urokova mira v procentech
p = 10.
# mesicni vklad
v = 1000
# mesicni urocici koeficient
q = (1. + p / 100)**(1./12.)

# doba sporeni v lech
years = 3
# pocet urocicih obdobi (mesicu)
n = 12 * years

S = 0.0
for i in range(n):
    S += v
    S *= q

Sn = v * q * (q**n - 1.0) / (q - 1.0)
print("analyticke reseni:\t%.2f" % Sn)
print("vypocet v pythonu:\t%.2f" % S)

S = 0.0
target = 1e6
i = 0
while (S < target):
    S += v
    S *= q
    i += 1

i_analytical = log(S* (q-1) / (q * v) + 1) / log(q)

print("analyticky: castku %.0f Kc nasporime po %d mesicich, neboli %.1f letech" % (target, i_analytical, i_analytical / 12.))
print(" v pythonu: castku %.0f Kc nasporime po %d mesicich, neboli %.1f letech" % (target, i, i / 12.))
                                    
"""
Alternativni otazka: stihneme za zivot nasetrit x Kc?
"""
x = 1e8
years_in_life = 60
months_in_life = years_in_life * 12


S = 0.0
for i in range(1, months_in_life+1): 
    S += v
    S *= q
    if S >= x:
        break

if (i < months_in_life):
    print("Ano, za %d let stihneme nasetrit %d Kc." % (years_in_life, x))
else:
    print("Ne, za %d let rozhodne nestihneme nasetrit %d Kc." % (years_in_life, x))
