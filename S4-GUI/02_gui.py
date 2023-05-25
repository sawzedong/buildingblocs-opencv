import cv2

img = cv2.imread("../img/image_processing/orchid.png")

gui = cv2.namedWindow("window")
def throwaway(x):
    pass

cv2.createTrackbar("trackbar", "window", 0, 100, throwaway)

while True:
    cv2.imshow("window", img)
    value = cv2.getTrackbarPos("trackbar", "window")
    print(value)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
