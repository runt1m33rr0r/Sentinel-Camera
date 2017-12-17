class Storage:
    _encodings = []
    _names = []

    @staticmethod
    def get_encodings():
        return Storage._encodings

    @staticmethod
    def get_names():
        return Storage._names

    @staticmethod
    def set_encodings(value):
        Storage._encodings = value

    @staticmethod
    def set_names(value):
        Storage._names = value
