import numpy as np
import cv2
from time import sleep
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
print('FurniBOT ZMQ video server at port 5555 started')
socket.bind("tcp://*:5555")

cap = cv2.VideoCapture(0)

while(True):
    

    message = socket.recv_string()
    if message == 'read':
        ret, frame = cap.read()
        # cv2.imshow('frame', frame)
        socket.send_pyobj(frame)
    if message == 'stop':
        socket.send_string('Stopping server')
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
socket.unbind("tcp://*:5555")