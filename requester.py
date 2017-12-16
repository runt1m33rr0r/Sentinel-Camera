import requests
from utils import decode_encoding


def get_user_data():
    encodings = []
    names = []

    people = requests.get('http://localhost:1234/faces/all').json()
    for person in people:
        encodings.append(decode_encoding(person['encoding']))
        names.append(person['name'])

    return {'encodings': encodings, 'names': names}


def alert(name, image, timestamp):
    # print(name)
    # alert the backend that a person has been detected
    pass
