# Sentinel-Camera

## Required hardware
- Recent NVIDIA GPU
- Recent Intel CPU
- Webcam

## Required software
- Python 3 x64
- Windows OS, could work on linux too

## Setup
- Download prebuilt wheels for [dlib](https://www.dropbox.com/s/rj9yf80vx2glw83/dlib-19.7.0-cp36-cp36m-win_amd64.whl?dl=0), [numpy](https://www.dropbox.com/s/vgag9wcs4pviqnu/numpy-1.13.3%2Bmkl-cp36-cp36m-win_amd64.whl?dl=0), [scipy](https://www.dropbox.com/s/i64t42kct3rdoou/scipy-1.0.0-cp36-cp36m-win_amd64.whl?dl=0), [pillow](https://www.dropbox.com/s/4qlom06k5twuxol/Pillow_SIMD-4.3.0.post0-cp36-cp36m-win_amd64.whl?dl=0), [opencv](https://www.dropbox.com/s/zeha86ofvobjz43/opencv_python-3.3.1%2Bcontrib-cp36-cp36m-win_amd64.whl?dl=0https://www.dropbox.com/s/vgag9wcs4pviqnu/numpy-1.13.3%2Bmkl-cp36-cp36m-win_amd64.whl?dl=0)
- run "pip install" for the downloaded wheels
- run "pip install flask click"
- run "pip install --no-deps face_recognition face_recognition_models"

## How to run
- run "python server.py" and the camera server should start on port 5000
