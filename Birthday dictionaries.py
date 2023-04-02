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
import json

with open("birthdays.csv", "r") as file:
    reader = csv.reader(file)
    dictionary = dict(reader)

# To practise using JSON file we'll save dictionary to JSON and create a JSON file in the directory
json_dict = json.dumps(dictionary, indent=4)
with open("birthdays.json", "w") as f:
    json.dump(json_dict, f)

#Read the file
with open("birthdays.json", "r") as f:
    dictionary_2 = json.load(f)

dictionary_2 = json.loads(dictionary_2)  # to create dictionary from string


print(f"Welcome to the birthday dictionary. We know the birthdays of:\n")

# List of all available birthdays
for name in dictionary_2.keys():
    print(name)

while True:

    name = input(f"Who's birthday do you want to look up?:")

    if name in dictionary_2.keys():
        print(f"{name}'s birthday is {dictionary_2[name]}")
        break
    else:
        print("We don't have this information. Try another name\n")
