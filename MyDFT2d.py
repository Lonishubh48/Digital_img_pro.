# Implimenting a 2D version of DFT
import matplotlib.pyplot as plt
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


# Genreating an array of zeros and taking DFT of it.

arr = np.zeros([1024, 1024])
arr[513, 513] = 1  # Zero frequency at (513,513)

# creating a square array of m points on a side of magnitude 1 centered in the array
m = int(input('enter the value for square array with side 1mag '))
arr[-(513 + m):(513 + m), -(513 + m):(513 + m)] = 1
plt.subplot(131)
plt.title("img array")
plt.imshow(np.real(arr), cmap='gray', interpolation='nearest')
f = dft2d(arr)  # taking dft by calling 2d DFT function
f = np.abs(f)  # taking absolute value to show dft in processed img
# ploting the results
plt.subplot(132)
plt.imshow(f, cmap='gray', interpolation='nearest')
plt.title("2d DFT")
plt.subplot(133)
plt.imshow(np.log(f + 1), cmap='gray', interpolation='nearest')
plt.title("Refined DFT")
plt.show()