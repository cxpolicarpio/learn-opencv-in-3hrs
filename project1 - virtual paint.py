import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

#todo: change
myColors = [[0, 110, 153, 19, 240, 255], #orange
            #[133, 56, 0, 159, 156, 255] #pink
            [140, 119, 176, 179, 244, 255]
           ]
myColorValues = [[51, 153, 255],    #bgr
                 [255, 0, 255],
                 [0, 255, 0]        #green
                ]

myPoints = [] #[x, y, colorId]

def findColor(img, myColors, myColorValues):
    # convert image to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)  # white is what we need, black will be disregarded
        x, y = getContours(mask)
        cv2.circle(imgResult, (int(x), y), 10, myColorValues[count], cv2.FILLED)
        #cv2.imshow(str(i), mask)
        if x!= 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #retrieve the extreme outer contours/corners

    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            #calculate the curve length:
            peri = cv2.arcLength(cnt, True) #closed, so we'll put True

            #approximate how many corner points:
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w / 2, y

def drawOnCanvas(myPoints, myColorValues):
    print("drawONCanvas")
    for point in myPoints:
        #print(int(point[0]), int(point[1]), point[2])
        cv2.circle(imgResult, (int(point[0]), point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", img)
    cv2.imshow("imgResult", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break