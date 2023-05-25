import cv2
import numpy as np

# Opening up image files
img = cv2.imread("S1-image_processing\orchid.png")

##########################################
# Image Recolouring

#1. Recolour 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Exploring Other Colour Spaces
#   1. cv2.COLOR_BGR2HSV
#   2. cv2.COLOR_BGR2Lab
#   3. cv2.COLOR_BGR2RGB

cv2.imshow("recoloured", gray)
cv2.waitKey()


##########################################
# Image Masking

# Image Mask
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of pink cololur in HSV
lower_pink = np.array([120, 0, 0])
upper_pink = np.array([255, 255, 255])

# create a mask
mask = cv2.inRange(hsv, lower_pink, upper_pink)

# Bitwise and mask
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Mask", result)
cv2.waitKey()


