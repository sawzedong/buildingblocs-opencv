import numpy as np
import cv2 
img = cv2.imread("../img/feature_detection/chessboard.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# apply corner detection
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None) # dilation for marking the corners
img[dst>0.01*dst.max()]=[0,0,255] # revert back w/ optimal threshold
cv2.imshow("dst", img)
cv2.waitKey()