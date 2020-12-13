from flask import Flask, render_template, Response
import zmq
import numpy as np
import cv2

context = zmq.Context()
socket = context.socket(zmq.REQ)
print('FurniBOT ZMQ video client at port 5555 started')
socket.connect("tcp://localhost:5555")

app = Flask(__name__)
print('FurniBOT Flask http server at port 5000 started')

def gen_frames():
    while(True):
        socket.send_string('read')
        frame = socket.recv_pyobj()
        # cv2.imshow('frame2', frame)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # cv2.destroyAllWindows()
    # socket.disconnect("tcp://localhost:5555")

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)