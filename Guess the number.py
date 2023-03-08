'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

import random

num_to_guess = random.randint(1, 9)

guess_count = 0
check = 1


def guess_check(num_to_guess, user_guess):
    if user_guess < num_to_guess:
        print("Your guess is too low")
        return -1
    elif user_guess > num_to_guess:
        print("Your guess is too high")
        return 1
    else:
        print("Your guess is RIGHT")
        return 0


while check != 0:
    guess = input("Guess a number from 1 to 9: ")
    
    if guess.isnumeric() and (int(guess) in range(1, 10)):
        check = guess_check(num_to_guess, int(guess))
        guess_count += 1
    elif guess.lower() == 'exit':
        break
    

print("Number of guesses: {0}".format(guess_count))
