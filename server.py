from flask import Flask, render_template, Response, request, jsonify
from camera_opencv import Camera
from io import BytesIO
import base64
from ai import get_encodings, process_image
from storage import Storage
from requester import get_user_data


app = Flask(__name__)


def decode_image(encoded):
    bits = base64.b64decode(encoded)
    file = BytesIO(bits)
    return file


def encode_encoding(encoding):
    encoded = base64.b64encode(encoding)
    string = encoded.decode('utf-8')
    return string


@app.route('/')
def index():
    # Video streaming home page.
    return render_template('index.html')


def gen(camera):
    # Video streaming generator function.
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag.
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/encode', methods=['POST'])
def encode():
    data = request.json
    if data['image'] and len(data['image']) > 0:
        image = decode_image(data['image'])
        processed = process_image(image)

        encodings = get_encodings(processed)

        if len(encodings) > 0:
            encoded = encode_encoding(encodings[0])
            return jsonify({'encoding': encoded})

    return jsonify({'message': 'ivalid data'})


if __name__ == '__main__':
    Storage.set_encodings(get_user_data()['encodings'])
    Storage.set_names(get_user_data()['names'])

    gen(Camera())

    app.run(host='0.0.0.0', threaded=True)
