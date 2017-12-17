import requests
from utils import decode_encoding, encode_image
from datetime import datetime


LAST_NAMES = []


def get_user_data():
    encodings = []
    names = []

    people = requests.get('http://localhost:1234/faces/all').json()
    for person in people:
        if person['encoding'] and person['name']:
            encodings.append(decode_encoding(person['encoding']))
            names.append(person['name'])

    return {'encodings': encodings, 'names': names}


def alert(names, image):
    global LAST_NAMES
    should_alert = False

    for name in names:
        if name not in LAST_NAMES:
            LAST_NAMES = names
            should_alert = True
            break

    if should_alert:
        print('alerting')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        req = requests.post('http://localhost:1234/alerts/add', json={
            "names": names,
            "image": encode_image(image),
            "timestamp": timestamp})
