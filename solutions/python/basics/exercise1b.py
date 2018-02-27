""" Fibonacci
Ask the use for an integer `n` and print out the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number)
up to that number.  E.g., if `n=10`, print out `1 1 2 3 5 8`.
"""

n = int(input("Enter a number: "))
# n = 10
a, b = 0, 1
while b < n:
    print(b, end=' ')
    a, b = b, a+b
