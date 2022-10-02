#Creating 2D DFT for given cosine signal
import numpy as np
import matplotlib.pyplot as plt
from my2dDFT import dft2d
from scipy import ndimage

arr=np.arange(0,256,1)
M,N=np.meshgrid(arr,arr)
fm=int(input("enter the sinusoid frequency="))
fs=2*fm
p=np.cos(2*np.pi*fm*(M/fs))
q=np.cos(2*np.pi*fm*(N/fs))
im1=dft2d(p)
im2=dft2d(q)
plt.subplot(241)
plt.imshow(p,cmap='gray', interpolation='nearest')
plt.title('0-degree')
plt.subplot(242)
plt.imshow(q,cmap='gray', interpolation='nearest')
plt.title('90-degree')
w= ndimage.rotate(p,45)
plt.subplot(243)
plt.imshow(w,cmap='gray', interpolation='nearest')
plt.title('45-degree')
w1 = ndimage.rotate(p,135)
plt.subplot(244)
plt.imshow(w1,cmap='gray', interpolation='nearest')
plt.title('135-degree')