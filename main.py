import cv2
import pickle
import cvzone
import numpy as np
from flask import Flask, Response, render_template, jsonify

app = Flask(__name__)

with open('data/parking_position', 'rb') as f:
    pos_list = pickle.load(f)

cap = cv2.VideoCapture('data/parking_video.mp4')

width, height = 105, 43


def checking_space(img, img_process):
    free_spaces = 0
    occupied_spaces = 0

    for pos in pos_list:
        x, y = pos
        img_crop = img_process[y : y + height, x : x + width]
        count = cv2.countNonZero(img_crop)

        if count < 850:
            status = 'space'
            color = (0, 255, 0)
            thickness = 5
            free_spaces += 1
        else:
            status = 'car'
            color = (0, 0, 255)
            thickness = 1
            occupied_spaces += 1

        cvzone.putTextRect(img, status, (x, y + height - 3), scale=1.2, thickness=2, offset=0)
        cv2.rectangle(img, (x, y), (x + width, y + height), color, thickness)

    return img, free_spaces, occupied_spaces


def process_frame():
    success, img = cap.read()
    if not success:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        return None

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)
    img_threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    img_median = cv2.medianBlur(img_threshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    img_dilate = cv2.dilate(img_median, kernel, iterations=1)

    return checking_space(img, img_dilate)


def generate_frames():
    while True:
        frame_data = process_frame()
        if frame_data is None:
            continue
        img, _, _ = frame_data
        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/space_count')
def space_count():
    frame_data = process_frame()
    if frame_data is None:
        return jsonify({'error': 'No frame available'}), 500
    _, free_spaces, occupied_spaces = frame_data
    return jsonify({'free': free_spaces, 'occupied': occupied_spaces})


if __name__ == '__main__':
    app.run(debug=True)
