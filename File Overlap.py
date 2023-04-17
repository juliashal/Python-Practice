'''Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.'''

url1 = "https://www.practicepython.org/assets/primenumbers.txt"
url2 = "https://www.practicepython.org/assets/happynumbers.txt"

import requests

r1 = requests.get(url1).text
r2 = requests.get(url2).text

list1 = r1.split()
list2 = r2.split()

overlap = [i for i in list1 if i in list2]

print(overlap)