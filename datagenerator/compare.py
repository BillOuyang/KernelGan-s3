import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as img
from scipy.ndimage import filters, measurements, interpolation
import glob
from scipy.io import loadmat

GT = loadmat('.\output_kernel\im_0_sf_4_4.mat')
predict = loadmat('.\output_kernel\_kernel_x2.mat')

plt.subplot(1, 2, 1)
plt.imshow(GT['ker'], cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(predict['Kernel'], cmap='gray')
plt.show()
print()