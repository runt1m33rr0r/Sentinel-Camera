import base64
from io import BytesIO
import numpy


def decode_image(encoded):
    bits = base64.b64decode(encoded)
    file = BytesIO(bits)
    return file


def encode_encoding(encoding):
    encoded = base64.b64encode(encoding)
    string = encoded.decode('utf-8')
    return string


def decode_encoding(encoding):
    decoded = base64.b64decode(encoding)
    result = numpy.frombuffer(decoded)
    return result
