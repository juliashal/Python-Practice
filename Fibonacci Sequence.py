'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

'''1 version'''
def febonacci_seq (num: int):
    list = []
    for i in range(num):
        if i >= 2:
            next_element = list[i-1]+list[i-2]
            list.append(next_element)
        else:
            list.append(1)
    return list

'''2 version'''
def febonacci_seq_1 (num: int):
    list = [1]*num
    for i in range(2, num, 1):
        list[i] = list[i-1]+list[i-2]
    return list


while True:
    number = input("How many Fibonnaci numbers to generate? : ")
    if number.isnumeric():
        number=int(number)
        break

print(febonacci_seq_1(number))