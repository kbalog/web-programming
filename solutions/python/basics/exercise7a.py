""" Read file
Write a script that performs the following operations on the `my_file.txt` file:
  - Open and read this txt file
  - Print out the first line
  - Count the number of words
  - Count the number of lines
  - Create a dictionary of words with their frequencies
"""
from collections import Counter

with open("my_file.txt", "r") as f:
    print(f.readline())

with open("my_file.txt", "r") as f:
    line_count = 0
    word_count = 0
    word_all = []
    for line in f:
        line = line.replace(",", "", len(line))
        words = line.split()
        word_all += words
        line_count += 1
        word_count += len(line)
    word_fre = Counter(word_all)

print("There are in total {} lines;".format(line_count))
print("There are in total {} words;".format(word_count))
print(dict(word_fre))
