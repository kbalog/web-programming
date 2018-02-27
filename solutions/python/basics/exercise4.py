"""Write module
Write two modules to make E_4.py run.

Hint:
  - Use 'base64' to encode and decode a string.
  - In python 2, it has a general string type for representing both text and binary data.
  But in python3, is uses str to represent `unicode` text and `bytes` for binary data.
  Between `unicode` and `bytes`, we use encode and decode to convert one to the other,
  i.e., string.decode()=bytes; bytes.encode = string.
"""

from my_encode import string_to_bytes, encode, bytes_to_string
from my_decode import decode

my_string = "String to be encoded!"


def main():
    print(my_string)
    # string_to bytes decode my_string into bytes
    my_bstring = string_to_bytes(my_string)
    print("Change my_string into bytes string:", my_bstring)
    # use base64.b64encode to encode the binary string
    en_bstring = encode(my_bstring)
    print("Encode my bytes string:", en_bstring)
    # use base64.b64decode to decode the encoded binary string to my_bstring
    en_string = bytes_to_string(en_bstring)
    print("Change my encode bytes string into string", en_string)
    # decode my_bstring into text string de_string(the same with my_string)
    de_string = decode(en_string)
    print("Decode it, we have:", de_string)


if __name__ == '__main__':
    main()
