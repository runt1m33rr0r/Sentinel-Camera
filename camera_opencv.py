import cv2
from base_camera import BaseCamera
from ai import process_video_frame


class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)

        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, frame = camera.read()
            frame = process_video_frame(frame)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', frame)[1].tobytes()
