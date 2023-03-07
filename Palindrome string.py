'''Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)'''

while True:
    line = input("Type a word: ").upper()
    if line:
        break

reverse_list = [line[-i] for i in range(1, len(line)+1)]
reverse_line = ''.join(reverse_list) # join list back to string

print(reverse_line)

if line == reverse_line:
    print("Word {0} is a palindrome".format(line))
else:
    print("Word {0} is NOT a palindrome".format(line))
