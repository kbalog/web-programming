"""Factorial
Ask the user for an integer `n` and compute the factorial for this number.
Hints:
  - Factorial: `0!=1`; `1!=1`; `2!=2*1=2`; `n!=n*(n-1)*(n-2)*...*1`
  - Use `int(input("Enter a number: "))` to manually input a number
"""

num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
    print("negative numbers do not have factorial")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
