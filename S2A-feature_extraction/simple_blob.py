import cv2
import numpy as np;
 
 
# set up the detector with default parameters.
params = cv2.SimpleBlobDetector_Params()

# feel free to change the following parameters at your own discretion!

# threshold parameters
params.minThreshold = 10
params.maxThreshold = 200

# area parameters
params.filterByArea = True
params.minArea = 1500

# circularity parameters
params.filterByCircularity = True
params.minCircularity = 0.1

# convexity parameters
params.filterByConvexity = True
params.minConvexity = 0.87

# inertia parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01

# detect & mark blobs
image = cv2.imread("../img/feature_detection/blob.png", cv2.IMREAD_GRAYSCALE)
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(image)
img_with_kps = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# show result
cv2.imshow("Blobs", img_with_kps)
cv2.waitKey(0)