'''Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message'''

while True:
    num = input("Type a numerator: ")
    if num.isnumeric():
        break

while True:
    denom = input("Type a denominator: ")
    if denom.isnumeric():
        break


num = int(num)
denom = int(denom)

if (num % denom) == 0:
    print("{0} devides evenly into {1}".format(num,denom))
else:
    print("{0} devides oddly into {1}".format(num,denom))


