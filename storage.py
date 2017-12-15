class Storage:
    __encodings = []
    __names = []

    @staticmethod
    def get_encodings():
        return Storage.__encodings

    @staticmethod
    def get_names():
        return Storage.__names

    @staticmethod
    def set_encodings(value):
        Storage.__encodings = value

    @staticmethod
    def set_names(value):
        Storage.__names = value
