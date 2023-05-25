import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("S1-image_processing\orchid.png")

##########################################
# Plotting Histograms

colour = ("b", "g", "r")
for i, col in enumerate(colour):
    histr = cv2.calcHist(img, [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()

##########################################
# Image Recolouring

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray)
res = np.hstack((gray, equ))
cv2.imshow('transformed', res)

cv2.waitKey()

