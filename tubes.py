import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca citra
pic2 = cv2.imread('jennie.jpg')

# Tampilkan citra asli
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(pic2, cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')

# Sharpening menggunakan filter unsharp
sharp_filter = np.array([[-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]])
sharpened = cv2.filter2D(pic2, -1, sharp_filter)

# Tampilkan citra yang telah diberi efek sharpening
plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
plt.title('Gambar yang Ditajamkan')

# Blurring menggunakan filter Gaussian
gaussian_filter = cv2.getGaussianKernel(17, 7)
gaussian_filter = np.outer(gaussian_filter, gaussian_filter)
blurred = cv2.filter2D(pic2, -1, gaussian_filter)

# Tampilkan citra yang telah diberi efek blurring
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
plt.title('Gambar yang Diburamkan')

# Tampilkan plot
plt.show()