import numpy as np
import cv2 

## PARAMETERS
image = "./img/object_detection/people2.jpg"
face_detection_model = "./S3B-dnn_face_detection/face_detection_yunet_2022mar.onnx" # download from https://github.com/opencv/opencv_zoo/tree/master/models/face_detection_yunet
score_threshold = 0.9 # Filtering out faces of score < score_threshold (used to eliminate unlikely faces)
nms_threshold = 0.3 # Suppress bounding boxes of iou >= nms_threshold (used to eliminate same bboxes)
top_k = 5000 # Keep top_k bounding boxes before NMS.

def visualize(input, faces, thickness=2):
    if faces is None:
        print("No face found")
        return
    for face in faces:
        coords = face[:-1].astype(np.int32) # necessary to convert coordinates to integers before plotting

        # draw rectangles of face face
        cv2.rectangle(input, (coords[0], coords[1]), (coords[0] + coords[2], coords[1]+coords[3]), (0, 255, 0), thickness)

        # draw points of facial features
        cv2.circle(input, (coords[4], coords[5]), 2, (255, 0, 0), thickness) # right eye
        cv2.circle(input, (coords[6], coords[7]), 2, (0, 0, 255), thickness) # left eye
        cv2.circle(input, (coords[8], coords[9]), 2, (0, 255, 0), thickness) # nose tip
        cv2.circle(input, (coords[10], coords[11]), 2, (255, 0, 255), thickness) # right corner of mouth
        cv2.circle(input, (coords[12], coords[13]), 2, (0, 255, 255), thickness) # left corner of mouth

img = cv2.imread(cv2.samples.findFile(image))
imgWidth = int(img.shape[1])
imgHeight = int(img.shape[0])
detector = cv2.FaceDetectorYN.create(face_detection_model, "", (imgWidth, imgHeight), score_threshold, nms_threshold, top_k)

faces = detector.detect(img)[1]
visualize(img, faces)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
