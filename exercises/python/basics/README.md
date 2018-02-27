# Python exercises, Part I. (basics)

## Exercise #0: Hello python!

Create a `hello.py` file with the following line as content:

```
print("Hello python!")
```

Run it on your own machine (`python hello.py`).


## Exercise #1a: Factorial

Ask the user for an integer `n` and compute the factorial for this number.

Hints:

  - Factorial: `0!=1`; `1!=1`; `2!=2*1=2`; `n!=n*(n-1)*(n-2)*...*1`
  - Use `int(input("Enter a number: "))` to manually input a number


## Exercise #1b: Fibonacci

Ask the use for an integer `n` and print out the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) up to that number.  E.g., if `n=10`, print out `1 1 2 3 5 8`.


## Exercise #2a: List filtering

Filter all the odd numbers from the list `[1,2,3,4,5]` and store them in a new list.


## Exercise #2b: Exam scores

The following dictionary stores four students' exam scores for a given course:
```
d = {"Adam": 95, "Lisa": 85, "Bart": 59, "Paul": 74}
```
Calculate the average, max, and min scores.


## Exercise #2c: List and Dictionary operation

Similar to the previous exercise, a dictionary stores five students' scores:
```
e = {"Adam": 95, "Lisa": 85, "Bart": 59, "Paul": 74, "Dave": 85}
```
Write a script that lists the name(s) of those who got 85 as score.


## Exercise #2d: Data structures

Copy the following lines and print out the values of these variables to see how these data structures work:

  - `A0 = dict(zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5)))`
  - `A1 = range(10)`
  - `A2 = sorted([i for i in A1 if i in A0])`
  - `A3 = sorted([A0[s] for s in A0])`
  - `A4 = [i for i in A1 if i in A3]`
  - `A5 = {i:i*i for i in A1}`
  - `A6 = [[i,i*i] for i in A1]`


## Exercise #3a: Fibonacci function

Write a function of Fibonacci which return Fibonacci sequence up to `n`.

  - Hint: Put the scripts you have created in Exercise 1b into a function structure


## Exercise #3b: Sorting

Write a function that takes a list of numbers as parameter, and returns the list sorted.

  - Hint: use `list.sort()` or implement on your own sorting (give it a try!)


## Exercise #3c: Reverse string

Write a function that takes a string as parameter and return the reversed string. E.g., given the input `abcde` it should return `edcba`.


## Exercise #4: Create modules

Create the two missing modules to make [exercise4.py](exercise4.py) run.

Hints:
  - In Python 2, there is a general string type for representing both text and binary data. But, in Python 3, str is used to represent `unicode` text and `bytes` is used to represent binary data. Between `unicode` and `bytes`, we use encode and decode to convert one to the other, i.e., `string.decode() = bytes; bytes.encode = string`
  - Use `base64` to encode and decode a binary string ([reference](https://docs.python.org/2/library/base64.html)).


## Exercise #5: CardHolder class

Write a Python class of CardHolder. It should initialize a (bank) card holder's name and balance.
Also, it should have functions for checking balance, and withdrawing and depositing a given amount.


## Exercise #6: Output formatting

Write a Python class for string processing. It should have the following functions:

  - Return a string's lowercase
  - Return a string's uppercase
  - Format print two strings by using key
  - Change a camel-cased word like "WordVector" to "word_vector".

Hints:

  - Use `re.sub()` for camel-case conversion
  - Read [the Regular Expression Operations](https://docs.python.org/3/library/re.html)


## Exercise #7a: Read file

Write a script that performs the following operations on the `my_file.txt` file:

  - Open and read this txt file
  - Print out the first line
  - Count the number of words
  - Count the number of lines
  - Create a dictionary of words with their frequencies


## Exercise #7b: JSON write

Make a dictionary from the following keys and values, and write that dictionary into a JSON file:

```
keys = [1,2,3,4,5]
values = ["I", "love", "python", "very", "much"]
```


## Exercise #8: Exceptions

Write a function to parse a website's title (e.g., [this](http://www.pythonscraping.com/pages/page1.html)).
Use try-except to capture the exceptions like the web can not be opened or the title does not exist.

It is recommended that you make use of existing packages (BeautifulSoup or urllib.request) in this exercise.
