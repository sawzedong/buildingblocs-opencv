import cv2
import os

# set up face cascade: initialise and load the cascade
face_cascade_name = os.path.join(cv2.data.haarcascades,'haarcascade_frontalface_alt.xml')
face_cascade = cv2.CascadeClassifier()
face_cascade.load(cv2.samples.findFile(face_cascade_name))

# load and process image
frame = cv2.imread('../img/object_detection/people1.jpg')
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame_gray = cv2.equalizeHist(frame_gray)
# NOTE: we apply the grayscale and histogram equalisation on a separate frame, so we can still display the original frame later

# detect and plot faces
faces = face_cascade.detectMultiScale(frame_gray)
for (x, y, w, h) in faces:
    frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 4)

# show results
cv2.imshow('Face detection', frame)
cv2.waitKey()