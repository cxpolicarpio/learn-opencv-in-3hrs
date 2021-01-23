#bird's eye view

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 250, 350
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]]) #get the 4 corner points of the card, (you can open up image in paint, move your mouse around, it will give you the points)
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]]) #define the which corner are the points on above is refering to

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)