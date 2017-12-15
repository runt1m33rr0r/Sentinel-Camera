import requests


def get_user_data():
    encodings = []
    names = []

    # people = requests.get('http://server:8080').json()['people']
    # parse request...

    return {'encodings': encodings, 'names': names}


def alert(name, image, timestamp):
    # alert the backend that a person has been detected
    pass
