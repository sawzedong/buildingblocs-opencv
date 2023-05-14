import numpy as np
import cv2 
from matplotlib import pyplot as plt

img = cv2.imread("../img/feature_detection/blocks.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect corners
corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = np.intp(corners)

# mark corners
for i in corners:
    x, y = i.ravel() 
    cv2.circle(img, (x,y), 15, 255, -1)

plt.imshow(img), plt.show()