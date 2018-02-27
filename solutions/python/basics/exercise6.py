""" Output formatting

Write a python class for string processing. It should have the following functions:
  - Return a string's lowercase
  - Return a string's uppercase
  - Format print two strings by using key
  - Change a camel-cased word like "WordVector" to "word_vector".
Hints:
  - Use `re.sub()` for camel-case conversion
  - Read [the Regular Expression Operations](https://docs.python.org/3/library/re.html)
"""
import re


class Str_process:
    def lowercase_string(self, string):
        return string.lower()

    def uppercase_string(self, string):
        return string.upper()

    def format_print(self, string1, string2):
        print('String1: {one}; String2: {two}.'.format(one=string1, two=string2))
        return

    def camel_string(self, string):
        """Splits a CamelCased string into a new one, capitalized, where words are separated by blanks."""
        s1 = re.sub('(.)([A-Z])', r'\1_\2', string)
        return s1.lower()


x = Str_process()
print(x.lowercase_string("MY"))
print(x.uppercase_string("sfhkds"))
x.format_print("a", "b")
print(x.camel_string("WordCatVector"))
