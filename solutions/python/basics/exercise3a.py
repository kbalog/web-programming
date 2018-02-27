""" Fibonacci function

Write a function of Fibonacci which return Fibonacci sequence up to `n`.
  - Hint: Put the scripts you have created in Exercise 1b into a function structure
"""


def fib(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


print(fib(100))
