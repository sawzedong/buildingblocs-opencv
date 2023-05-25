import numpy as np
import cv2 
import matplotlib.pyplot as plt 

obj_img = cv2.imread('../img/feature_detection/pineapple.png', cv2.IMREAD_GRAYSCALE)
scene_img = cv2.imread('../img/feature_detection/fruit_pile.png', cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(obj_img, None)
kp2, des2 = orb.detectAndCompute(scene_img, None)

# create Brute Force Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# match descriptors...
matches = bf.match(des1, des2)

# ...and then sort them
matches = sorted(matches, key = lambda x: x.distance)

res = cv2.drawMatches(obj_img, kp1, scene_img, kp2, matches[:10], None)

plt.imshow(res), plt.show()