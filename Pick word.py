'''In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 
Download this file and save it in the same directory as your Python code. '''

#Download file wth words

from urllib.request import urlopen
import random


url = "http://norvig.com/ngrams/sowpods.txt"
save_as = "sowpods.txt"

# Download from URL
with urlopen(url) as file:
    content = file.read().decode()

# Save to file
with open(save_as, 'w') as download:
    download.write(content)

def random_word():
    with open("sowpods.txt","r") as file:
        file_lines = file.readlines()
        random_index = random.randint(1, len(file_lines))
        print(f"Random index is {random_index}, Random word is {file_lines[random_index]}")

random_word()