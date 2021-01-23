# resize and crop image
import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
print(img.shape) # to find the size of the image
#(330, 330, 3) (height, width, number of channels=bgr)

imgResize = cv2.resize(img, (150, 150))
#imgResize = cv2.resize(img, (1000, 1000))

imgCropped = img[0:200, 200:300] #[height, width]
cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)