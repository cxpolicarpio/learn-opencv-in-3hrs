#method proposed by viola and jones
#custom cascades

import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarsascade_frontalface_default.xml")
img = cv2.imread('Resources/lena.png')

cv2.imshow("Result", img)
cv2.waitKey(0)