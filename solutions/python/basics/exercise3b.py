""" Sorting

Write a function that takes a list of numbers as parameter, and returns the list sorted.
  - Hint: use `list.sort()` or implement on your own sorting (give it a try!)
"""


def Sort(my_list):
    return sorted(my_list)


print(Sort([2, 1, 4]))


def insert_sort(lists):
    # insert sort
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


print(insert_sort([2, 1, 4]))


def bubble_sort(lists):
    # Bubble sort
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def select_sort(lists):
    # select sort
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


print(select_sort([4, 2, 1]))
