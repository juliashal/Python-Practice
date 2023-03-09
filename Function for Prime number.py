'''Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.'''


def prime_check(x=int):
    dividors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    mods = [x % d for d in dividors]
    if x in dividors:
        print("It's a prime number")
    elif (mods.count(0) > 0):
        index_divs = [i for i in range(len(mods)) if mods[i]==0] #find indexes where mod=0
        divs = [dividors[index] for index in index_divs] #find dividors
        print("It's not a prime number")
        print("Dividors: {0}".format(divs))
    else:
        print("It's a prime number")


while True:
    number = input("Type a number: ")
    if number.isnumeric():
        break

number = int(number)
prime_check(number)
