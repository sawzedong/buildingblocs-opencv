import numpy as np
import cv2 
import matplotlib.pyplot as plt 

obj_img = cv2.imread('../img/feature_detection/pineapple.png', cv2.IMREAD_GRAYSCALE)
scene_img = cv2.imread('../img/feature_detection/fruit_pile.png', cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(obj_img, None)
kp2, des2 = orb.detectAndCompute(scene_img, None)

FLANN_INDEX_LSH = 6
index_params = dict(
    algorithm = FLANN_INDEX_LSH,
    table_number = 6,
    key_size = 12,
    multi_probe_level = 1
)
search_params = dict(checks = 100)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

matchesMask = [[0, 0] for i in range(len(matches))]


for i,tup in enumerate(matches):
    if len(tup) == 2:
        m, n = tup
        if m.distance < 0.7 * n.distance:
            matchesMask[i] = [1, 0]

draw_params = dict(
    matchesMask = matchesMask,
)

res = cv2.drawMatchesKnn(obj_img, kp1, scene_img, kp2, matches, None, **draw_params)

plt.imshow(res), plt.show()