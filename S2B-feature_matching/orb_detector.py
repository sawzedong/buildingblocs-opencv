import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread("../img/feature_detection/pineapple.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
keypoints = orb.detect(img, None)
keypoints, descs = orb.compute(img, keypoints)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

for kp in keypoints:
    x, y = np.intp(kp.pt[0]), np.intp(kp.pt[1])
    cv2.circle(img, (x, y), 4, 255, -1) # image, (x_coord, y_coord), size, color, filled/unfilled

plt.imshow(img), plt.show()