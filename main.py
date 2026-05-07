import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import random_noise
import os

# setup path
folder_project = os.path.dirname(__file__)
folder_assets = os.path.join(folder_project, 'assets')

if not os.path.exists(folder_assets):
    os.makedirs(folder_assets)

# load gambar
path_gambar = os.path.join(folder_assets, 'input.jpg')
img = cv2.imread(path_gambar)

if img is None:
    print("Gambar belum ada atau path salah, cek folder assets")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# tambah noise
noise_img = random_noise(img, mode='s&p', amount=0.05)
noise_img = (noise_img * 255).astype(np.uint8)

# denoising spatial (median filter)
spatial_result = cv2.medianBlur(noise_img, 5)

# denoising frequency
gray = cv2.cvtColor(noise_img, cv2.COLOR_RGB2GRAY)

f = np.fft.fft2(gray)
fshift = np.fft.fftshift(f)

baris, kolom = gray.shape
tengah_x, tengah_y = baris // 2, kolom // 2

mask = np.zeros((baris, kolom), np.uint8)
radius = 50

for i in range(baris):
    for j in range(kolom):
        if (i - tengah_x)**2 + (j - tengah_y)**2 <= radius**2:
            mask[i, j] = 1

fshift_filter = fshift * mask

f_ishift = np.fft.ifftshift(fshift_filter)
img_hasil = np.fft.ifft2(f_ishift)
img_hasil = np.abs(img_hasil)

frequency_result = np.clip(img_hasil, 0, 255).astype(np.uint8)

# simpan hasil
cv2.imwrite(os.path.join(folder_assets, 'noise.jpg'),
            cv2.cvtColor(noise_img, cv2.COLOR_RGB2BGR))

cv2.imwrite(os.path.join(folder_assets, 'spatial.jpg'),
            cv2.cvtColor(spatial_result, cv2.COLOR_RGB2BGR))

cv2.imwrite(os.path.join(folder_assets, 'frequency.jpg'),
            frequency_result)

print("hasil sudah disimpan di folder assets")

# tampilkan
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(img)
plt.axis('off')

plt.subplot(2,2,2)
plt.title("Noise")
plt.imshow(noise_img)
plt.axis('off')

plt.subplot(2,2,3)
plt.title("Spatial (Median)")
plt.imshow(spatial_result)
plt.axis('off')

plt.subplot(2,2,4)
plt.title("Frequency (Low-pass)")
plt.imshow(frequency_result, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()