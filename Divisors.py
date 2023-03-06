'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number.For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

while True:
    number = input("Type a number :")
    if number.isnumeric():
        break

number=int(number)
list=[i for i in range(2,100) if i % number==0]

print(list)