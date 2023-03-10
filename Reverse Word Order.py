'''Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.'''

sentence = "My name is Julia"

words_list = sentence.split()

'''1 version'''
reverse_words_list = [words_list[-(i+1)] for i in range(len(words_list))]

reverse_sentence = ' '.join(reverse_words_list)

print(reverse_sentence)

'''2 version'''

words_list.reverse()

reverse_sentence = ' '.join(words_list)

print(reverse_sentence)