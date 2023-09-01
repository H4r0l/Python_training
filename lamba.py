#Problem: Sorting List of Strings

#You have a list of strings containing names. Write a program to sort the list #of names in ascending order based on the length of the names. If two names #have the same length, they should remain in the order they were originally in.

#Your task:

#Write a Python program that takes a list of names as input and sorts them using a lambda function for the sorting key.
#


def sort_names(names):
    return sorted(names, key=lambda x: len(x))

print(sort_names(["apple", "banana", "cherry", "orange", "kiwi"]))


