import cv2 
import time 

# Opening up image files
img = cv2.imread("../img/image_processing/orchid.png")
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyWindow("img")

##########################################
# Image Transformation

#1. Resizing

# Method 1 - Specifying width and height
width = 300
height = 300
resized_img = cv2.resize(img, (width, height))
cv2.imshow('resized', resized_img)
cv2.waitKey()

# Method 2 - Scale Factor 
scale_x = 1.2
scale_y = 1.2
resizefactor_img = cv2.resize(img, None, fx=scale_x, fy=scale_y)
cv2.imshow('scaleFactor', resizefactor_img)
cv2.waitKey()
cv2.destroyAllWindows()

# 2. Cropping 
start_row, start_col = 100, 100
end_row, end_col = 300, 300

cropped = img[start_row:end_row, start_col:end_col]
cv2.imshow("cropped", cropped)
cv2.waitKey()
