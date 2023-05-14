import numpy as np
import cv2 

img = cv2.imread("../img/feature_detection/street.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect edges
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)