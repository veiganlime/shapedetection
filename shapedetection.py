import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_contours(image):
        for cnt in contours:
        area = cv2.contourArea(cnt)  #Diese Funktion wird verwendet, um die Fläche des Umrisses zu finden.
        print("Area: ", area)
        cv2.drawContours(imageContour, cnt, -1, (255,0,0), 3)  #Konturen zeichnen
        perimeter = cv2.arcLength(cnt, True)  #Überprüfen, ob die Konturen geschlosen sind
        print("Perimeter: ", perimeter)
        approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)  #Anzahl der Konturen zu finden
        print("Corner Points: ", len(approx))
        objCorner = len(approx)
        x,y,w,h = cv2.boundingRect(approx)  #erkannte Objekte gekenzeichnen

        if objCorner == 3:
            objectType = 'Dreieck'
        elif objCorner == 4:
            aspectRatio = float(w)/float(h)
            if aspectRatio > 0.95 and aspectRatio < 1.05:
                objectType = 'Quadrat'
            else:
                objectType = "Recheck"
        elif objCorner > 4:
            objectType = 'Creis'

        else:
            objectType = "None"

        cv2.rectangle(imageContour, (x, y), (x+w, y+h), (0, 255, 0), 2)  #Ein Rechteck wird um die identifizierten Objekte gezeichnet
        cv2.putText(imageContour, objectType, (x+(w//2)-10, (y - 20)), cv2.FONT_HERSHEY_COMPLEX, 0.5 , (0, 0, 0), 2)  #Beschriftung hinzufuegen

image = cv2.imread("source/shapes_v2.png")
imageContour = image.copy()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_gray, (7, 7), 1)
imageCanny = cv2.Canny(image_blur, 50, 50)

get_contours(imageCanny)



# Alle Bilder aufeinander anzeigen lassen.
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", image_gray)
cv2.imshow("Canny Image", imageCanny)
cv2.imshow("Contour Image", imageContour)
cv2.imwrite("source/shapeOutput.png", imageContour)
cv2.waitKey(0)
cv2.destroyAllWindows()
