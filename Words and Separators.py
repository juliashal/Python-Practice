'''Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.'''

def split_sentence(sentence: str):
    words = sentence.split()
    list_separators=[' ',',']
    separators = [i for i in sentence if i in list_separators]
    return words, separators

your_input = input("Type the sentence: ")

words, separators = split_sentence(your_input)

print(words)
print(separators)