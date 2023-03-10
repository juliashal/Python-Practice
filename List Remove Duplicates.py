'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.'''

'''1 function - using a loop and constructing a list'''
def remove_duplicates_1(user_list: list):
    new_list = []
    for e in user_list:
        if e not in new_list:
            new_list.append(e)
    
    return new_list


'''2 function - using sets'''
def remove_duplicates_2(user_list: list):
    new_set = set(user_list)
    new_list = list(new_set)

    return new_list

user_list = [1,2,2,4,1,6,9,3,11,13,6]

print(remove_duplicates_1(user_list))

print(remove_duplicates_2(user_list))