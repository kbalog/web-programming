import base64


def string_to_bytes(string):
    return string.encode(encoding="utf-8")


def encode(bytesString):
    # base64 encode
    encodestr = base64.b64encode(bytesString)
    return encodestr


def bytes_to_string(encodestr):
    return encodestr.decode()
