'''Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!'''

def max_of_three(x1:int,x2:int,x3:int):
    if x1>=x2 and x1>=x3:
        print(f"{x1} is maximum among 3 numbers {x1}, {x2}, {x3}")
    elif x2>=x1 and x2>=x3:
        print(f"{x2} is maximum among 3 numbers {x1}, {x2}, {x3}")
    else:
        print(f"{x3} is maximum among 3 numbers {x1}, {x2}, {x3}")

max_of_three(1,12,23987)
max_of_three(111,111,111)
max_of_three(10,1,4)