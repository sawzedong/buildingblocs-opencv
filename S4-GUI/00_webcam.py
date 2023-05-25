import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
   print("Cannot open camera")
   
while True:
    ret, frame = cap.read() # Capture frame-by-frame

    if not ret: # if frame is read correctly ret is True
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'): # exits if Q key pressed
        break

cap.release()

