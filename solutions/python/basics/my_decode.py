import base64


def decode(encodestr):
    decodestr = base64.b64decode(encodestr)
    return decodestr.decode()
