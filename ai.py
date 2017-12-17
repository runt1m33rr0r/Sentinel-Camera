import face_recognition
from PIL import Image
from io import BytesIO
import cv2
from storage import Storage
from requester import alert


def process_image(image):
    # size = 300, 300
    image = Image.open(image)
    image = image.convert('RGB')
    # image.thumbnail(size)
    new = BytesIO()
    image.save(new, 'jpeg')
    return new


def get_encodings(file):
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model='cnn')
    face_encodings = face_recognition.face_encodings(image, face_locations)
    return face_encodings


def process_video_frame(frame):
    should_alert = False
    names = Storage.get_names()
    encodings = Storage.get_encodings()

    if len(encodings) < 1 and len(names) < 1:
        return cv2.imencode('.jpg', frame)[1].tobytes()

    face_names = []

    # make frame smaller
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(encodings, encoding)

        match_idx = -1
        for i in range(len(matches)):
            if matches[i]:
                # a known face has been detected
                match_idx = i
                break

        if match_idx > -1:
            name = names[match_idx]
            face_names.append(name)
            should_alert = True
        else:
            face_names.append('Unknown')

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    frame = cv2.imencode('.jpg', frame)[1].tobytes()
    if should_alert:
        alert(face_names, frame)

    return frame
