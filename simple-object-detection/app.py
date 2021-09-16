import cv2

# CONSTANT
# batas
threshold = 0
# nama window
windowName = 'image'

# ketika slider diubah
def on_change(val):
 
    imageCopy = img.copy()
 
    threshold = val
    cv2.putText(imageCopy, str(threshold), (0, imageCopy.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 4)
    gray = cv2.cvtColor(imageCopy, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    (T, thresh) = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours :
        area = cv2.contourArea(cnt)
        if area > 2000:
            cv2.drawContours(imageCopy, cnt, -1, (0, 255, 0), 3)

    cv2.imshow(windowName, imageCopy)


# load gambar
img = cv2.imread('traffic-sign.jpg')
 
 
# tampilkan gambar pertama
cv2.imshow(windowName, img)
# buat trackbar
cv2.createTrackbar('slider', windowName, 0, 255, on_change)


cv2.waitKey(0)
cv2.destroyAllWindows()