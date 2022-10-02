import numpy as np
import matplotlib.pyplot as plt
from my2dDFT import dft2d
from scipy.ndimage import rotate
# creating 2d cosine signal
arr=np.arange(0,256,1)                              # creating image array of size 256 x 256
M,N=np.meshgrid(arr,arr)
fm=int(input("enter the sinusoid frequency="))      # taking input frequency of signal from user
fs=2*fm                                             # making use nyquist sampling frequency
p=np.cos(2*np.pi*(M/fs))

# taking 2d DFT of different images by calling my2dft function.
f = dft2d(p)
q = dft2d(np.rot90(p))
w = dft2d(rotate(p,45))
w1 = dft2d(rotate(p,135))
# plotting the results
plt.subplot(2,4,1)
plt.imshow(p, cmap='gray', interpolation='nearest')             # showing cosine image in gray scale and interpolating
plt.title('cosine image')                                                                # it to nearest value
plt.subplot(2,4,2)
plt.imshow(np.rot90(p), cmap='gray', interpolation='nearest')   # rotating image to <90 & interpolating into nearest value
plt.title('image rotate at 90-degree')
plt.subplot(2,4,3)
plt.imshow(rotate(p,45), cmap='gray', interpolation='nearest')  # rotating image to <45 & interpolating into nearest value
plt.title('image rotate at 45-degree')
plt.subplot(2,4,4)
plt.imshow(rotate(p,135), cmap='gray', interpolation='nearest') # rotating image to<135 & interpolating into nearest value
plt.title('image rotate at 135-degree')
plt.subplot(2,4,5)
plt.imshow(np.log(np.abs(f)+1), cmap='gray', interpolation='nearest')# log function is used to increase the brightness
plt.title('DFT @0-degree')                                                # log(np.abs(f)+1) "+1" is used to avoid infinity

plt.subplot(2,4,6)
plt.imshow(np.log(np.abs(q)+1), cmap='gray', interpolation='nearest')
plt.title('DFT @90-degree')

plt.subplot(2,4,7)
plt.imshow(np.log(np.abs(w)+1), cmap='gray', interpolation='nearest')
plt.title('DFT@45-degree')

plt.subplot(2,4,8)
plt.imshow(np.log(np.abs(w1)+1), cmap='gray', interpolation='nearest')
plt.title('DFT @135-degree')

plt.show()