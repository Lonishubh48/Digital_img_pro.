import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
from my2dDFT import dft2d                   # importing 2dDFT function


# creating an image for different Pixel width and create vertical strips over the image

a = int(input('enter the image dimension =  '))  # taking image dimension from user
b = int(input('enter the width of the Pixel = '))  # taking pixel width from user
x = int(a / (2 * b))
arr1 = np.zeros([a, a])
# Creating vertical strip inside the image.
for i in range(x):
    for j in range(a):
        arr1[j][(2 * b * i):(2 * b * i) + b] = 1
plt.subplot(2, 3, 1)                                        #ploting vertical strip image
plt.imshow(arr1, cmap='gray', interpolation='nearest')
plt.title(" Vertical strip image")
arr2 = np.rot90(arr1)                                       # rotating image by <90
plt.subplot(2, 3, 2)
plt.imshow(arr2, cmap='gray', interpolation='nearest')
plt.title(" rotate image at <90 ")
arr3 = rotate(arr1, 45)                                     # rotating image by <45
plt.subplot(2, 3, 3)
plt.imshow(arr3, cmap='gray', interpolation='nearest')
plt.title(" rotate image at <45")

#taking 2d DFT of each images by calling 2DFT function
w1 = dft2d(arr1)
w2 = dft2d(arr2)
w3 = dft2d(arr3)

w1 = np.log(np.abs(w1) + 1)
w2 = np.log(np.abs(w2) + 1)
w3 = np.log(np.abs(w3) + 1)
# ploting the results of  processed image
plt.subplot(2, 3, 4)
plt.imshow(w1, cmap='gray', interpolation='nearest')
plt.title("Ver. image DFT ")
plt.subplot(2, 3, 5)
plt.imshow(w2, cmap='gray', interpolation='nearest')
plt.title("Hor.image DFT")
plt.subplot(2, 3, 6)
plt.imshow(w3, cmap='gray', interpolation='nearest')
plt.title("<45 image DFT ")
plt.show()