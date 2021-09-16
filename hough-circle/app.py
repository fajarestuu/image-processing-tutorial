import cv2 as cv
import numpy as np

# Nama file
filename = 'traffic-sign.jpg'

# Load gambar traffic-sign.jpg
src = cv.imread(filename)
 
# resize ke 30% ukuran aslinya
scale_percent = 30 # percent of original size
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv.resize(src, dim, interpolation = cv.INTER_AREA)

# ubah ke grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

# beri filter median blur
gray = cv.medianBlur(gray, 5)

# aplikasikan hough circle
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 0.5, 20,
                            param1=100, param2=30,
                            minRadius=50, maxRadius=70)

# Jika lingkaran ditemukan
if circles is not None:
    circles = np.uint16(np.around(circles))
    # Untuk setiap lingkaran, gambar lingkaran
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(resized, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv.circle(resized, center, radius, (0, 234, 255), 3)


cv.imshow("detected circles", resized)
cv.waitKey(0)