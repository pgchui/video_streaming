# video_streaming
## Description:
HTTP server using flask to stream video to a webpage from a local camera. Video frames captured using OpenCV. ZMQ is used to transfer frames from video capturig program to the flask server program.
## Required package:
* flask
* opencv-python
* pyzmq
## How to run:
1. `python zmq_vid_server.py`
1. `python flask_server.py`
