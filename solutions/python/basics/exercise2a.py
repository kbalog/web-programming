"""List filtering

Filter all the odd numbers from the list `[1,2,3,4,5]` and store them in a new list.
"""
# first method
numbers = [1, 2, 3, 4, 5]

doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n)
print(doubled_odds)

# second method
numbers = [1, 2, 3, 4, 5]
doubled_odds = [n for n in numbers if n % 2 == 1]
print(doubled_odds)
