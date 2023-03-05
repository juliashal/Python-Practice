'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.'''


def list_cut(x=list):
    first_element = x[0]
    last_element = x[-1]
    return [first_element, last_element]


a = [5, 10, 15, 20, 25]
b = list_cut(a)
print(b)
