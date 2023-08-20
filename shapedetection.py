import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_contours(image):
        for cnt in contours:
        area = cv2.contourArea(cnt)
        print("Area: ", area)
        cv2.drawContours(imageContour, cnt, -1, (255,0,0), 3)
        perimeter = cv2.arcLength(cnt, True)
        print("Perimeter: ", perimeter)
        approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
        print("Corner Points: ", len(approx))
        objCorner = len(approx)
        x,y,w,h = cv2.boundingRect(approx)

        if objCorner == 3:
            objectType = 'Dreieck'

        elif objCorner == 4:
            objectType = 'Rechteck'

        elif objCorner > 4:
            objectType = 'Creis'

        else:
            objectType = "None"

        cv2.rectangle(imageContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(imageContour, objectType, (x+(w//2)-10, (y - 20)), cv2.FONT_HERSHEY_COMPLEX, 0.5 , (0, 0, 0), 2)

image = cv2.imread("source/shapes_v2.png")
imageContour = image.copy()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_gray, (7, 7), 1)
imageCanny = cv2.Canny(image_blur, 50, 50)


