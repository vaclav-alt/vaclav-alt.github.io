import numpy as np
import matplotlib.pyplot as plt

maxit   = 80
escape  = 2.0
size    = (1920, 1920)
mydpi   = 100
figsize = (size[0]/mydpi, size[1]/mydpi)

real = np.linspace(-1.5, 0.5, size[0])
imag = np.linspace(-1, 1, size[1])

grid = np.column_stack([imag[::-1]]*size[0])*1.0j +  np.row_stack([real]*size[1])

narray = np.zeros(grid.shape, dtype = int)

grid = np.where(np.abs(grid) > escape, 0.0, grid)
c    = np.copy(grid)

for it in range(maxit):
    grid   = grid**2 + c
    narray = np.where(np.abs(grid) > escape, it, narray)

res = narray / np.max(narray)

cmap = "twilight_shifted"
plt.imshow(res, cmap = cmap)
plt.axis('off')
plt.show()
