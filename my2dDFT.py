# implimentation of 2dDFT function.
import numpy as np
def dft2d(f):
    # defining size of image
    M, N = f.shape

    # To centralise the frequency at the middle of the array
    for i in range(M):
        for j in range(N):
            f[i, j] = f[i, j] * ((-1) ** (i + j))

            # creating indices for frequency(u,v) and for each image pixels(N,M) and reshaping the arrays ,
    # allowing to compute the  multiplication faster.
    u = np.arange(M)
    v = np.arange(M)
    x = np.reshape(u, (M, 1))
    y = np.reshape(v, (M, 1))
    e1 = np.exp((-2j * np.pi * x * u) / N)  # computation of 2d DFT formula
    e2 = np.exp((-2j * np.pi * y * v) / M)
    f1 = e1.dot(f).dot(e2)

    return f1
