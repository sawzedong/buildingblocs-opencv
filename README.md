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

- ?

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
