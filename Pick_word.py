'''In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 
Download this file and save it in the same directory as your Python code. '''


'''>>> Run the code below to download list of words

#Download file with words

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

>>> '''

from urllib.request import urlopen
import random

def random_word():
    with open("sowpods.txt","r") as file:
        file_lines = file.readlines()
        random_index = random.randint(1, len(file_lines))
        #print(f"Random index is {random_index}, Random word is {file_lines[random_index]}")

    return file_lines[random_index].strip()