import requests
from utils import decode_encoding, encode_image
from datetime import datetime
from config import ADD_ALERT_ROUTE, GET_DATA_ROUTE


LAST_NAMES = []


def get_user_data():
    encodings = []
    names = []

    people = requests.get(GET_DATA_ROUTE).json()
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
        req = requests.post(ADD_ALERT_ROUTE, json={
            "names": names,
            "image": encode_image(image),
            "timestamp": timestamp})
