from my_encode import string_to_bytes, encode, bytes_to_string
from my_decode import decode

my_string = "String to be encoded!"

def main():
    print(my_string)
    my_bstring = string_to_bytes(my_string)
    print("Change my_string into bytes string:", my_bstring)
    en_bstring = encode(my_bstring)
    print("Encode my bytes string:", en_bstring)
    en_string = bytes_to_string(en_bstring)
    print("Change my encode bytes string into string", en_string)
    de_string = decode(en_string)
    print("Decode it, we have:", de_string)

if __name__ == '__main__':
    main()
