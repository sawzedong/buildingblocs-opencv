# The AI of the Beholder: Seeing with Computer Vision 👀

This repository contains all the code we will be using throughout this BuildingBlocs 2023 Workshop.

## Navigating files

All the sections are numbered with the corresponding section number and header.
Feel free to upload your own images to the `img/` folder for testing!

## Dependencies

These codes minimally required `opencv-python` and `numpy` to run. This workshop uses `opencv-python==4.7.0`, so it may help to check the version you're using.

## Helpful links

OpenCV tutorials: [https://docs.opencv.org/4.7.0/d9/df8/tutorial_root.html](https://docs.opencv.org/4.7.0/d9/df8/tutorial_root.html)  
OpenCV documentation: [https://docs.opencv.org/4.7.0/](https://docs.opencv.org/4.7.0/)

### S1: Image Processing

- ?

### S2: Feature Extraction

- OpenCV Feature Detectors: [https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html](https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html)
- Harris Corner Detection: [https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#gac1fc3598018010880e370e2f709b4345](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#gac1fc3598018010880e370e2f709b4345)
- Shi-Tomasi Corner Detection: [https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541)
- Canny Edge Detection: [https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html)
- Simple Blob Detector: [https://docs.opencv.org/4.x/d0/d7a/classcv_1_1SimpleBlobDetector.html](https://docs.opencv.org/4.x/d0/d7a/classcv_1_1SimpleBlobDetector.html)


### S3A: Haar-cascade Object Detection

- OpenCV Tutorial: [https://docs.opencv.org/4.7.0/db/d28/tutorial_cascade_classifier.html](https://docs.opencv.org/4.7.0/db/d28/tutorial_cascade_classifier.html)
- OpenCV Pre-Trained Cascades: [https://github.com/opencv/opencv/tree/4.7.0/data/haarcascades](https://github.com/opencv/opencv/tree/4.7.0/data/haarcascades)

### S3B: DNN-based Face Detection

- OpenCV Tutorial: [https://docs.opencv.org/4.x/d0/dd4/tutorial_dnn_face.html](https://docs.opencv.org/4.x/d0/dd4/tutorial_dnn_face.html)
- FaceDetectorYN Documentation: [https://docs.opencv.org/4.x/df/d20/classcv_1_1FaceDetectorYN.html](https://docs.opencv.org/4.x/df/d20/classcv_1_1FaceDetectorYN.html)
- Model Download Link: [https://github.com/opencv/opencv_zoo/tree/master/models/face_detection_yunet](https://github.com/opencv/opencv_zoo/tree/master/models/face_detection_yunet)
- Scientific Paper: [https://doi.org/10.1007/s11633-023-1423-y](https://doi.org/10.1007/s11633-023-1423-y)

### S4: OpenCV GUI and Video

- ?

## Common issues

### 1. File loading issues

Issue: `...Can't find required data file...` or `...Can't read ONNX file...`, etc.  
Solution: Try running the scripts from the root file (i.e. the terminal should execute the files from the parent file)

### 2. Other issues?

Try using the Google Colab here instead: ...?
