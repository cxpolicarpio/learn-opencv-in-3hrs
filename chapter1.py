import cv2
import numpy as np #for matrices

print("Package imported")

#display image:
# img = cv2.imread("Resources/lena.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)


#dispay video:
# cap = cv2.VideoCapture("Resources/test_video.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


#use camera:
#cap = cv2.VideoCapture(0)
#cap.set(3, 640) #width, id#3
#cap.set(4, 480) #height
#cap.set(10, 100) #brightness
#while True:
#    success, img = cap.read()
#    cv2.imshow("video", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break


img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) #(7, 7) -> has to be odd numbers
#imgCanny = cv2.Canny(img, 100, 100)
imgCanny = cv2.Canny(img, 150, 200) #edge detector
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) #for those edge that can't be detected because they are not connected, etc.
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) #opposite of imgDialation, make it thinner

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

