import cv2 
import time 
import numpy as np

# Opening up image files
img = cv2.imread("S1-image_processing\orchid.png")

##########################################
# Image smoothing

# Blurring Images
kernel = (100, 100) # Experiment with these values
img_blur = cv2.blur(img, kernel)
cv2.imshow('image', img_blur)
cv2.waitKey()

# Image enhancement
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharpened_image = cv2.filter2D(img, -1, kernel)
cv2.imshow("sharpened", sharpened_image)
cv2.waitKey()