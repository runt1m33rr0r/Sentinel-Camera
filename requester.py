import requests
from utils import decode_encoding, encode_image
from datetime import datetime


LAST_NAME = ''


def get_user_data():
    encodings = []
    names = []

    people = requests.get('http://localhost:1234/faces/all').json()
    for person in people:
        encodings.append(decode_encoding(person['encoding']))
        names.append(person['name'])

    return {'encodings': encodings, 'names': names}


def alert(name, image):
    global LAST_NAME
    if name != LAST_NAME:
        print('alerting')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        req = requests.post('http://localhost:1234/alerts/add', json={
            "name": name,
            "image": encode_image(image),
            "timestamp": timestamp})
        LAST_NAME = name
