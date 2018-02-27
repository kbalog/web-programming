""" Reverse string
Write a function that takes a string as parameter and return the reversed string.
E.g., given the input `abcde` it should return `edcba`.
"""

string = 'abcdef'


def string_reverse1(string):
    return string[::-1]


def string_reverse2(string):
    t = list(string)
    l = len(t)
    for i, j in zip(range(l - 1, 0, -1), range(l // 2)):
        t[i], t[j] = t[j], t[i]
    return "".join(t)


def string_reverse3(string):
    if len(string) <= 1:
        return string
    return string_reverse3(string[1:]) + string[0]


from collections import deque


def string_reverse4(string):
    d = deque()
    d.extendleft(string)
    return ''.join(d)


def string_reverse5(string):
    # return ''.join(string[len(string) - i] for i in range(1, len(string)+1))
    return ''.join(string[i] for i in range(len(string) - 1, -1, -1))


print(string_reverse1(string))
print(string_reverse2(string))
print(string_reverse3(string))
print(string_reverse4(string))
print(string_reverse5(string))
