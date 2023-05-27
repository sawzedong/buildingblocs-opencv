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

- OpenCV Documentation: [https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html](https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html)
- All the ColourConversionCodes: [https://docs.opencv.org/3.4/d8/d01/group**imgproc**color\_\_conversions.html](https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html)
- Image Blurring and Enhancement: [https://www.geeksforgeeks.org/image-enhancement-techniques-using-opencv-python/](https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html)

### S2A: Feature Extraction

- OpenCV Feature Detectors: [https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html](https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html)
- Harris Corner Detection: [https://docs.opencv.org/4.x/dd/d1a/group**imgproc**feature.html#gac1fc3598018010880e370e2f709b4345](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#gac1fc3598018010880e370e2f709b4345)
- Shi-Tomasi Corner Detection: [https://docs.opencv.org/4.x/dd/d1a/group**imgproc**feature.html#ga1d6bb77486c8f92d79c8793ad995d541](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541)
- Canny Edge Detection: [https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html)
- Simple Blob Detector: [https://docs.opencv.org/4.x/d0/d7a/classcv_1_1SimpleBlobDetector.html](https://docs.opencv.org/4.x/d0/d7a/classcv_1_1SimpleBlobDetector.html)

### S2B: Feature Matching

- OpenCV Tutorial: [https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html](https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html)

### S3A: Haar-cascade Object Detection

- OpenCV Tutorial: [https://docs.opencv.org/4.7.0/db/d28/tutorial_cascade_classifier.html](https://docs.opencv.org/4.7.0/db/d28/tutorial_cascade_classifier.html)
- OpenCV Pre-Trained Cascades: [https://github.com/opencv/opencv/tree/4.7.0/data/haarcascades](https://github.com/opencv/opencv/tree/4.7.0/data/haarcascades)

### S3B: DNN-based Face Detection

- OpenCV Tutorial: [https://docs.opencv.org/4.x/d0/dd4/tutorial_dnn_face.html](https://docs.opencv.org/4.x/d0/dd4/tutorial_dnn_face.html)
- FaceDetectorYN Documentation: [https://docs.opencv.org/4.x/df/d20/classcv_1_1FaceDetectorYN.html](https://docs.opencv.org/4.x/df/d20/classcv_1_1FaceDetectorYN.html)
- Model Download Link: [https://github.com/opencv/opencv_zoo/tree/master/models/face_detection_yunet](https://github.com/opencv/opencv_zoo/tree/master/models/face_detection_yunet)
- Scientific Paper: [https://doi.org/10.1007/s11633-023-1423-y](https://doi.org/10.1007/s11633-023-1423-y)

### S4: OpenCV GUI and Video

- OpenCV Tutorial: [https://docs.opencv.org/3.4/dc/d4d/tutorial_py_table_of_contents_gui.html](https://docs.opencv.org/3.4/dc/d4d/tutorial_py_table_of_contents_gui.html)

## Common issues

### 1. File loading issues

Issue: `...Can't find required data file...` or `...Can't read ONNX file...`, etc.

**Possible Problem 1:** Our code often uses `../<filepath>` as we assume it is run from the individual file itself.
**Solution:** You can replace `../` with `./` if you are running from the parent folder (e.g. using VSCode).

**Possible Problem 2:** Our code uses `<directory>/<filepath>`.  
**Solution**: If you are on a windows OS, kindly replace all `/` with `\\` instead.

### 2. Other issues?

Please ask our friendly Tech Facils during the event, or you can look for help online / reach out to your group facils.  
You can also try using the Google Colab here instead: [https://bit.ly/bbcs23-opencv-colab](https://bit.ly/bbcs23-opencv-colab)
