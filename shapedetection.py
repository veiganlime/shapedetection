import cv2

def get_contours(image):
    pass

image = cv2.imread("source/shapes_v2.png")
imageContour = image.copy()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_gray, (7, 7), 1)
imageCanny = cv2.Canny(image_blur, 50, 50)


