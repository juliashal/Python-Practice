'''For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
Happy coding!'''

import csv

with open("birthdays.csv", "r") as file:
    reader = csv.reader(file)

    dictionary = dict(reader)
    print(f"Welcome to the birthday dictionary. We know the birthdays of:\n")

    # List of all available birthdays
    for name, date in dictionary.items():
        print(name)

    while True:

        name = input(f"Who's birthday do you want to look up?:")

        if name in dictionary:
            print(f"{name}'s birthday is {dictionary[name]}")
            break
        else:
            print("We don't have this information. Try another name\n")
