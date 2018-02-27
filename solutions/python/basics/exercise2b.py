"""Exam scores

The following dictionary stores four students' exam scores for a given course:
`d = {'Adam':95, 'Lisa':85, 'Bart':59, 'Paul': 74}`.

Calculate the average, max, and min scores.
"""

d = {"Adam": 95, "Lisa": 85, "Bart": 59, "Paul": 74}

# Solution 1: searching for avg/min/max manually

sumv = 0.0
max_score = list(d.values())[0]
min_score = list(d.values())[0]
for _, i in d.items():
    sumv += i
    if i > max_score:
        max_score = i
    if i < min_score:
        min_score = i

print("Average score is:", sumv / len(d))
print("Max score is:", max_score)
print("Min score is:", min_score)


# Solution 2

v = d.values()
print("Average score is:", sum(v) / len(d))
print("Max score is:", max(v))
print("Min score is:", min(v))
