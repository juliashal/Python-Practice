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
from datetime import datetime

with open("birthdays.csv", "r") as file:
    fieldnames = ("name", "date")
    reader = csv.DictReader(file, fieldnames)

    # To practise using JSON file we'll save dictionary to JSON and create a JSON file in the directory
    json_dict = [row for row in reader]

with open("birthdays.json", "w") as f:
    json.dump(json_dict, f, indent=4)

# Read the file
with open("birthdays.json", "r") as f:
    data_dict = json.load(f)


print(f"Welcome to the birthday dictionary. We know the birthdays of:\n ")

name_dict = {}
month_dict = {}

for line in data_dict:
    print(line['name'])
    birth_date = datetime.strptime(line['date'], '%m/%d/%Y').date()
    name_dict[line["name"]] = birth_date

    #calculate how many birthdays in each month
    month_dict[birth_date.strftime("%B")] = month_dict.get(birth_date.strftime("%B"), 0) + 1

print(month_dict)

while True:

    name = input(f"Who's birthday do you want to look up?:")
    if name in name_dict:
        print(f"{name}'s birthday is {name_dict[name]}")
        break
    else:
        print("We don't have this information. Try another name\n")
