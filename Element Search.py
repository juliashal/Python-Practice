'''Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.'''

'''1 version'''


def element_search(num_list: list, x: int):
    return x in num_list


num_list = [1, 2, 5, 8, 30, 42, 43, 500]
num = 2

print(element_search(num_list, num))

'''2 version - Binary search'''


def binary_search(num_list: list[int], x: int):

    while len(num_list) != 1:
        list_len = len(num_list)
        middle_index = int(list_len/2)
        middle_element = num_list[middle_index]
        print(f"\nMiddle element = {middle_element}")
        print(f"Guess number X = {x}")

        if x > middle_element:
            num_list = num_list[middle_index:]
            print(f"x > middle_element = {x > middle_element}")
            print(f"Number {x} might be in in the list {num_list}")
        elif x < middle_element:
            num_list = num_list[:middle_index]
            print(f"x < middle_element = {x < middle_element}")
            print(f"Number {x} might be in in the list {num_list}")
        else:
            num_list = middle_element
            print(f"\nNumber {x} is in the list {num_list}")
            return True

    print(f"\nNumber {x} is NOT in the list {num_list}")
    return False

print(binary_search(num_list, num))
