import cv2 

# Opening up image files
img = cv2.imread("../img/image_processing/orchid.png")

# Shape of an image. It returns a tuple of the number of rows, columns, an channels
# print(img.shape)

# Finding specific pixels
print(img[200, 150])

# Cropping
start_row, end_row = 0, 200
start_col, end_col = 0, 100
cropped = img[start_col:end_col, start_row:end_row]

cv2.imshow("image", cropped)
cv2.waitKey()