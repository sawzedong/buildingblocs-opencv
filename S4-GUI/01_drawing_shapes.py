import cv2

img = cv2.imread("../img/image_processing/orchid.png")

# Drawing rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.imshow("image", img)
cv2.waitKey(0)

# Drawing line
cv2.line(img,(300,50),(400, 50),(255,0,0),3)
cv2.imshow("image", img)
cv2.waitKey(0)